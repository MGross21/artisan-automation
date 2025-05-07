# Artisan Automation

Design, Robotics, Engineering, Art and Motion (DREAM) Competition

[Event Announcement](https://intheloop.engineering.asu.edu/2025/04/18/attend-the-dream-competition-seminar-april-25/)

🏆🥇 **Awarded First Place and a $1,000 Prize.**

## Event Recap

Check out the highlights from the DREAM Competition on social media:

- [LinkedIn](https://www.linkedin.com/posts/school-of-manufacturing-systems-and-networks_asuengineering-design-robotics-activity-7324208506419453957-uM9B?utm_source=share&utm_medium=member_desktop&rcm=ACoAADIqOI4BuuBIn9Lw3VbPEu5bQkc3evp5cIs)  
- [Instagram](https://www.instagram.com/p/DJK45kJuQgY/)

## Team Members

- **Michael Gross**  
    [GitHub](https://github.com/MGross21) | [LinkedIn](https://www.linkedin.com/in/mhgross)

- **Praneeth Boddeti**  
    [GitHub](https://github.com/pbleedblue) | [LinkedIn](https://www.linkedin.com/in/praneeth-boddeti)

- **Jacob Pisors**  
    [GitHub](https://github.com/JPisors) | [LinkedIn](https://www.linkedin.com/in/jacob-pisors)

## Introduction

We invite you to journey back to 1954—the year the world witnessed the first autonomous robot take its historic steps. Fast forward 70 years, and we find ourselves navigating the intricate relationship between human ingenuity and artificial intelligence.

Amid sensational headlines about robots and AI, a fascinating synergy emerges—a partnership where humans and robots complement each other. Robots excel in endurance during long work sessions, while human creativity thrives in adaptability and innovation.

This harmonious collaboration is the essence of our Continuum Crate.

## Unveiling the DREAM of our *Continuum Crate*

Our creation doesn't just showcase technology—it narrates a vision of our future. Inside this seemingly simple crate lies the essence of tomorrow—a world where robots and humans don’t merely coexist but co-create.

ASU's mascot, Sparky, and the Robot unite to hold the "MSN" banner—not as rivals, but as partners in collaboration.

**Design**: We've crafted a deceptively simple exterior that transforms into a moment of wonder. The minimalist, modular box opens to reveal something unexpected—a theatrical "Voila!"

**Robotics**: This seamless experience required a symphony of disciplines—mechanical engineering principles, robotics, cutting-edge manufacturing, and intricate mechatronics all working in harmony.

**Engineering**: Behind this elegant simplicity lies remarkable complexity—five distinct manufacturing techniques converging to create something greater than the sum of its parts.

**Art**: Watch as human and robot unite, in waving the MSN flag—a powerful metaphor for collaboration across areas like manufacturing and even your future homes.

**Manufacturing**: What you will witness isn't just a demonstration—it's a window into tomorrow. The Continuum Crate doesn't ask you to fear the future but to embrace it. This isn't about replacement; it's about enhancement—humans and robots writing the next chapter of innovation together.

![Continuum Crate](media/continuum_crate.gif)

## ASU Design Aspirations

**Fusing Intellectual Disciplines**: By integrating mechatronics, manufacturing, and robotics, this project exemplifies the fusion of diverse intellectual fields.

**Conducting Use-Inspired Research**: The human-robot and human-AI collaboration showcased here highlights the potential for impactful research as people, machines, and AI become increasingly interconnected.

**Valuing Entrepreneurship**: This creation demonstrates how three ASU students, with no formal arts background, leveraged their knowledge to innovate and bring their vision to life.

**Practicing Principled Innovation**: By portraying robots as joyful and expressive companions rather than mere tools, this project fosters a principled dialogue about the evolving relationship between humans and machines.

## Using MP3-to-Bytes Conversion Script

To convert an MP3 file into a byte array for use in Arduino projects, follow these steps:

1. **Create a Python virtual environment**:

```bash
python -m venv venv
```

2. **Activate the virtual environment**:

```bash
venv/Scripts/activate
```

3. **Install the required packages**:

```bash
pip install -r requirements.txt
```

4. **Run the conversion script**:

```bash
python <conversion-script> <input> <output> <flags>
```

- **Input**: An MP3 file (e.g., `asu_fight_song.mp3`).
- **Output**: A C header file (e.g., `song.h`) with the byte array.
- **Flags**:
    - `--name`: Specifies the variable name for the byte array.
    - `--rate`: Sets the sampling rate for the conversion.

This tool simplifies embedding audio data into Arduino projects for playback or other uses.

```bash
python audio_conversion/mp3_to_arr.py \
    audio_conversion/asu_fight_song.mp3 \
    arduino_code/song.h \
    --name asu_fight_song \
    --rate 1000
```

This will generate a [`song.h`](arduino_code/song.h) file containing the byte array representation of the MP3 file, which can be included in your Arduino project.

```c
#include "song.h"

// Rest of your code here
```
