from pydub import AudioSegment
import argparse
import os

def trim_silence(data: bytes, silence_values=(128, 0)) -> bytes:
    """Trims leading and trailing bytes equal to values in silence_values."""
    start = 0
    end = len(data)

    # Trim from the start
    while start < end and data[start] in silence_values:
        start += 1

    # Trim from the end
    while end > start and data[end - 1] in silence_values:
        end -= 1

    return data[start:end]

def convert_mp3_to_array(mp3_path, output_header, array_name="audio_data"):
    print(f"[INFO] Converting {mp3_path}...")
    
    # Load and convert MP3
    audio = AudioSegment.from_mp3(mp3_path)
    audio = audio.set_channels(1).set_frame_rate(8000).set_sample_width(1)  # mono, 8kHz, 8-bit
    raw_data = audio.raw_data

    # Trim leading/trailing silence
    trimmed_data = trim_silence(raw_data, silence_values=(128, 0))
    print(f"[INFO] Trimmed length: {len(trimmed_data)} bytes (from {len(raw_data)})")

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_header), exist_ok=True)

    # Write C header
    with open(output_header, 'w') as f:
        f.write(f'// Auto-generated from {os.path.basename(mp3_path)}\n')
        f.write(f'#ifndef {array_name.upper()}_H\n')
        f.write(f'#define {array_name.upper()}_H\n\n')
        f.write(f'#include <avr/pgmspace.h>  // Store data in flash memory\n\n')
        f.write(f'const unsigned char {array_name}[] PROGMEM = {{\n')

        # Format as hex array (12 values per line)
        for i, byte in enumerate(trimmed_data):
            if i % 12 == 0:
                f.write('    ')
            f.write(f'0x{byte:02X}')
            if i != len(trimmed_data) - 1:
                f.write(', ')
            if (i + 1) % 12 == 0:
                f.write('\n')

        if len(trimmed_data) % 12 != 0:
            f.write('\n')
        f.write('};\n')
        f.write(f'const unsigned int {array_name}_len = {len(trimmed_data)};\n\n')
        f.write(f'#endif // {array_name.upper()}_H\n')

    print(f"[DONE] Header saved to: {output_header}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert MP3 to C array for Arduino playback")
    parser.add_argument("input", help="Path to input MP3 file")
    parser.add_argument("output", help="Output C header file (.h)")
    parser.add_argument("--name", help="C array name", default=None)

    args = parser.parse_args()

    # If --name not provided, use filename as array name
    if args.name is None:
        args.name = os.path.splitext(os.path.basename(args.input))[0].replace("-", "_").replace(" ", "_")

    convert_mp3_to_array(args.input, args.output, args.name)