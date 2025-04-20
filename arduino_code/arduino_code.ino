#include "song.h"
#include <avr/pgmspace.h>

void setup() {
  pinMode(9, OUTPUT);
}

void loop() {
  for (unsigned int i = 0; i < asu_fight_song_len; i++) {
    uint8_t val = pgm_read_byte(&asu_fight_song[i]);
    tone(9, val, 1);  // Play tone on pin 9 with frequency 'val' for 1 ms
    delayMicroseconds(1000);  // 1000 Hz playback
  }

  delay(1000); // pause before repeating


// #include "pitches.h"

// #define BUZZER_PIN 3

// int melody[] = {
//   NOTE_C2, NOTE_FS2, NOTE_G2, NOTE_FS2, NOTE_G2, NOTE_DS2, NOTE_D2, NOTE_DS2, NOTE_C2, NOTE_CS2, NOTE_C2, NOTE_F2, NOTE_C2, NOTE_DS2, NOTE_C2, NOTE_CS2, NOTE_D2, NOTE_CS2, NOTE_D2, NOTE_CS2, NOTE_E2, NOTE_FS2, NOTE_F2, NOTE_FS2, NOTE_G2, NOTE_FS2, NOTE_F2, NOTE_E2, NOTE_FS2, NOTE_G2, NOTE_C2, NOTE_FS2, NOTE_F2, NOTE_DS2, NOTE_D2, NOTE_DS2, NOTE_D2, NOTE_C2, NOTE_F2, NOTE_FS2, NOTE_F2, NOTE_DS2
// };

// int durations[] = {
//   4, 16, 16, 16, 4, 2, 16, 1, 16, 16, 1, 4, 1, 1, 1, 16, 16, 16, 16, 1, 16, 16, 16, 16, 16, 16, 16, 1, 16, 1, 1, 16, 16, 16, 2, 4, 1, 1, 16, 16, 1, 16
// };

// void setup() {
//   pinMode(BUZZER_PIN, OUTPUT);
// }

// void loop() {
//   PlayMusic(melody, durations, sizeof(melody) / sizeof(int));
//   delay(5000); // Wait 5 seconds before replaying
// }

// void PlayMusic(int melody[], int durations[], int size) {
//   for (int note = 0; note < size; note++) {
//     int duration = 1000 / durations[note];
//     tone(BUZZER_PIN, melody[note], duration);
//     int pauseBetweenNotes = duration * 1.30;
//     delay(pauseBetweenNotes);
//     noTone(BUZZER_PIN);
//   }
// }