from pydub import AudioSegment
import argparse
import os

def trim_silence(data: bytes, silence_values=(128, 0)) -> bytes:
    """Trim leading and trailing silence values."""
    start, end = 0, len(data)
    while start < end and data[start] in silence_values:
        start += 1
    while end > start and data[end - 1] in silence_values:
        end -= 1
    return data[start:end]

def convert_mp3_to_array(mp3_path, output_header, array_name="audio_data", sample_rate=1000):
    print(f"[INFO] Converting '{mp3_path}' at {sample_rate} Hz...")

    # Load and preprocess
    audio = AudioSegment.from_mp3(mp3_path)
    audio = audio.set_channels(1)
    audio = audio.set_frame_rate(sample_rate)
    audio = audio.set_sample_width(1)          # 8-bit signed PCM
    audio = audio.low_pass_filter(sample_rate // 2)
    audio = audio.normalize(headroom=0.1)

    raw_data = audio.raw_data
    trimmed = trim_silence(raw_data, silence_values=(128, 0))

    if not trimmed:
        raise ValueError("Trimmed data is empty. Try reducing trim aggressiveness or checking the source file.")

    print(f"[INFO] Final length: {len(trimmed)} bytes")

    # Convert signed 8-bit PCM to unsigned 8-bit (0–255)
    unsigned_data = bytes((sample + 128) % 256 for sample in trimmed)

    # Ensure output path exists
    os.makedirs(os.path.dirname(output_header), exist_ok=True)

    # Write C header file
    with open(output_header, 'w') as f:
        f.write(f'// Auto-generated from {os.path.basename(mp3_path)}\n')
        f.write(f'#ifndef {array_name.upper()}_H\n')
        f.write(f'#define {array_name.upper()}_H\n\n')
        f.write('#include <avr/pgmspace.h>\n\n')
        f.write(f'const unsigned char {array_name}[] PROGMEM = {{\n')

        for i, byte in enumerate(unsigned_data):
            if i % 12 == 0:
                f.write('    ')
            f.write(f'0x{byte:02X}')
            if i != len(unsigned_data) - 1:
                f.write(', ')
            if (i + 1) % 12 == 0:
                f.write('\n')
        if len(unsigned_data) % 12 != 0:
            f.write('\n')

        f.write('};\n')
        f.write(f'const unsigned int {array_name}_len = {len(unsigned_data)};\n\n')
        f.write(f'#endif // {array_name.upper()}_H\n')

    print(f"[DONE] Header saved to: {output_header}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert MP3 to a flash-safe C array for Arduino")
    parser.add_argument("input", help="Path to input MP3 file")
    parser.add_argument("output", help="Output .h file")
    parser.add_argument("--name", help="C array name", default=None)
    parser.add_argument("--rate", type=int, default=1000, help="Sample rate in Hz (default: 1000)")

    args = parser.parse_args()
    if args.name is None:
        args.name = os.path.splitext(os.path.basename(args.input))[0].replace("-", "_").replace(" ", "_")

    convert_mp3_to_array(args.input, args.output, args.name, args.rate)