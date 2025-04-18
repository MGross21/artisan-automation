#include "song.h"
#include <avr/pgmspace.h>

void setup() {
  pinMode(9, OUTPUT);
}

void loop() {
  for (unsigned int i = 0; i < asu_fight_song_len; i++) {
    uint8_t val = pgm_read_byte(&asu_fight_song[i]);
    analogWrite(9, val);
    delayMicroseconds(125);  // 8000 Hz playback
  }

  delay(1000); // pause before repeating
}