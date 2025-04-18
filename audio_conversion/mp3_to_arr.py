from pydub import AudioSegment
import argparse
import os
import numpy as np
import tempfile

def trim_silence(data: bytes, silence_values=(128, 0)) -> bytes:
    """Trim leading and trailing silence values."""
    start, end = 0, len(data)
    while start < end and data[start] in silence_values:
        start += 1
    while end > start and data[end - 1] in silence_values:
        end -= 1
    return data[start:end]

def safe_preview(audio: AudioSegment, sample_rate: int):
    """Play or export preview depending on sample rate support."""
    if sample_rate >= 8000:
        try:
            from pydub.playback import play
            print("[INFO] Previewing audio playback...")
            play(audio)
        except Exception as e:
            print(f"[WARN] Playback failed: {e}")
    else:
        preview_path = "preview.wav"
        audio.export(preview_path, format="wav")
        print(f"[INFO] Sample rate too low for live playback. Preview saved to: {preview_path}")

def convert_mp3_to_array(mp3_path, output_header, array_name="audio_data", sample_rate=1000):
    print(f"[INFO] Converting '{mp3_path}' at {sample_rate} Hz...")

    # Load and preprocess
    audio = AudioSegment.from_mp3(mp3_path)
    audio = audio.set_channels(1)
    audio = audio.set_frame_rate(sample_rate)
    audio = audio.set_sample_width(1)  # 8-bit PCM
    audio = audio.low_pass_filter(sample_rate // 2)
    audio = audio.normalize(headroom=0.1)
    # audio = audio.fade_in(30).fade_out(100)  # Optional fade

    # Preview the audio or export preview.wav
    safe_preview(audio, sample_rate)

    raw_data = audio.raw_data
    trimmed = trim_silence(raw_data, silence_values=(128, 0))

    if not trimmed:
        raise ValueError("Trimmed data is empty. Try reducing trim aggressiveness or checking the source file.")

    print(f"[INFO] Final length after trim: {len(trimmed)} bytes")

    # Convert raw bytes to NumPy array for analysis
    samples = np.frombuffer(trimmed, dtype=np.int8)
    min_val, max_val = samples.min(), samples.max()
    print(f"[DEBUG] Sample range: min={min_val}, max={max_val}")

    # Safely convert signed to unsigned 8-bit PCM
    if min_val < 0:
        print("[INFO] Converting signed 8-bit to unsigned 8-bit...")
        samples = (samples.astype(np.int16) + 128).clip(0, 255).astype(np.uint8)
    else:
        print("[INFO] Audio is already unsigned.")
        samples = samples.astype(np.uint8)

    unsigned_data = samples.tobytes()

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