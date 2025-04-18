# artisan-automation

Art+Manufacturing ASU Competition

## Additional Required Packages

```bash
ffmpeg
```

# How to Use

```bash
python -m venv venv && venv/Scripts/activate  # Create and activate python virtual environmnet
pip install -r requirements.txt  # Install Required Packages
python audio_conversion/mp3_to_arr.py audio_conversion/asu_fight_song.mp3 arduino_code/song.h --name asu_fight_song # Run CLI Conversion
```
