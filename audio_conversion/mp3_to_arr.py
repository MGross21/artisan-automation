from pydub import AudioSegment
import argparse
import os

def convert_mp3_to_array(mp3_path, output_header, array_name="audio_data"):
    # Convert MP3 to 8-bit mono WAV using pydub (requires ffmpeg)
    audio = AudioSegment.from_mp3(mp3_path)
    audio = audio.set_channels(1).set_frame_rate(8000).set_sample_width(1)  # mono, 8kHz, 8-bit
    raw_data = audio.raw_data

    print(f"[INFO] Audio length: {len(raw_data)} bytes")

    # Write C header file
    with open(output_header, 'w') as f:
        f.write(f'#ifndef {array_name.upper()}_H\n')
        f.write(f'#define {array_name.upper()}_H\n\n')
        f.write(f'#include <avr/pgmspace.h>\n\n')
        f.write(f'const unsigned char {array_name}[] PROGMEM = {{\n')

        # Write hex values
        for i, byte in enumerate(raw_data):
            if i % 12 == 0:
                f.write('    ')
            f.write(f'0x{byte:02X}, ')
            if (i + 1) % 12 == 0:
                f.write('\n')
        f.write('\n};\n')
        f.write(f'const unsigned int {array_name}_len = {len(raw_data)};\n\n')
        f.write(f'#endif // {array_name.upper()}_H\n')

    print(f"[DONE] C header saved to: {output_header}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert MP3 to C array for Arduino")
    parser.add_argument("input", help="Path to input .mp3 file")
    parser.add_argument("output", help="Output header file (.h)")
    parser.add_argument("--name", help="C array name", default="audio_data")

    args = parser.parse_args()
    convert_mp3_to_array(args.input, args.output, args.name)
