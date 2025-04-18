from pydub import AudioSegment
import argparse
import os

def trim_silence(data: bytes, silence_values=(128, 0)) -> bytes:
    """Trims leading and trailing bytes equal to values in silence_values."""
    start = 0
    end = len(data)

    while start < end and data[start] in silence_values:
        start += 1

    while end > start and data[end - 1] in silence_values:
        end -= 1

    return data[start:end]

def convert_mp3_to_array(mp3_path, output_header, array_name="audio_data"):
    print(f"[INFO] Converting: {mp3_path}")

    # Load and convert MP3 to 8-bit mono 8kHz
    audio = AudioSegment.from_mp3(mp3_path)
    audio = audio.set_channels(1).set_frame_rate(8000).set_sample_width(1)
    raw_data = audio.raw_data

    # Trim silence
    trimmed_data = trim_silence(raw_data, silence_values=(128, 0))
    length = len(trimmed_data)
    print(f"[INFO] Trimmed length: {length} bytes (from {len(raw_data)} bytes)")

    if length == 0:
        raise ValueError("Trimmed audio is empty. File may be silent or overly trimmed.")

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_header), exist_ok=True)

    # Generate header file
    with open(output_header, 'w') as f:
        f.write(f'// Auto-generated from {os.path.basename(mp3_path)}\n')
        f.write(f'#ifndef {array_name.upper()}_H\n')
        f.write(f'#define {array_name.upper()}_H\n\n')
        f.write(f'#include <avr/pgmspace.h>\n\n')
        f.write(f'const unsigned char {array_name}[] PROGMEM = {{\n')

        # Write data with proper formatting and no trailing comma
        for i, byte in enumerate(trimmed_data):
            if i % 12 == 0:
                f.write('    ')
            f.write(f'0x{byte:02X}')
            if i < length - 1:
                f.write(', ')
            if (i + 1) % 12 == 0:
                f.write('\n')
        if length % 12 != 0:
            f.write('\n')

        f.write('};\n')
        f.write(f'const unsigned int {array_name}_len = {length};\n\n')
        f.write(f'#endif // {array_name.upper()}_H\n')

    print(f"[DONE] Header saved to: {output_header}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert MP3 to C array for Arduino playback")
    parser.add_argument("input", help="Path to input .mp3 file")
    parser.add_argument("output", help="Output C header file (.h)")
    parser.add_argument("--name", help="C array name", default=None)

    args = parser.parse_args()

    # Auto-generate a safe array name from file if not provided
    if args.name is None:
        args.name = os.path.splitext(os.path.basename(args.input))[0].replace("-", "_").replace(" ", "_")

    convert_mp3_to_array(args.input, args.output, args.name)