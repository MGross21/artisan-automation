# Artisan Automation

Design, Robotics, Engineering, Art and Motion Competition

[See Event Here](https://intheloop.engineering.asu.edu/2025/04/18/attend-the-dream-competition-seminar-april-25/)

## How to Convert Audio

```bash
python -m venv venv && venv/Scripts/activate  # Create and activate python virtual environmnet
pip install -r requirements.txt  # Install Required Packages
```

### Using Custom MP3-to-Byte Conversion Script

```bash
python audio_conversion/mp3_to_arr.py audio_conversion/asu_fight_song.mp3 arduino_code/song.h --name asu_fight_song --rate 1000
```

### Using Audio-to-Arduino Library

```bash
python audio-to-arduino/audio-to-arduino.py media/asu_fight_song.mp3 --tempo 132
```
