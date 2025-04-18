#include "song.h"

void setup() {
  pinMode(9, OUTPUT);
}

void loop() {
  for (unsigned int i = 0; i < song_len; i++) {
    analogWrite(9, song[i]); // send 8-bit value to PWM
    delayMicroseconds(125);  // 8000 Hz sample rate
  }
}