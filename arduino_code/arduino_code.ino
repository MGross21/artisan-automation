/* 
  Tetris theme - (Korobeiniki) 
  Connect a piezo buzzer or speaker to pin 11 or select a new pin.
  More songs available at https://github.com/robsoncouto/arduino-songs                                            
                                              
                                              Robson Couto, 2019
*/

#include "pitches.h"
#include <Servo.h>
#define REST 0

// Configuration
int tempo = 144; 
int buzzer = 6; // Pin for the buzzer
int motor = 8;  // Pin for the motor

Servo servo1;
int servo1Pin = 3; // Pin for the right-side servo
Servo servo2;
int servo2Pin = 5; // Pin for the left-side servo

void moveServoPosition(int pos1, int pos2, const char* positionName) {
  Serial.print("Moving to position ");
  Serial.println(positionName);
  servo1.write(pos1);
  servo2.write(pos2);
}

void movePos1() {
  moveServoPosition(75, 0, "1"); // Forward tilt position
}

void movePos2() {
  moveServoPosition(35, 40, "2"); // Backward tilt position
}

// Melody and durations
int melody[] = {
  NOTE_E5, 4,  NOTE_B4,8,  NOTE_C5,8,  NOTE_D5,4,  NOTE_C5,8,  NOTE_B4,8,
  NOTE_A4, 4,  NOTE_A4,8,  NOTE_C5,8,  NOTE_E5,4,  NOTE_D5,8,  NOTE_C5,8,
  NOTE_B4, -4,  NOTE_C5,8,  NOTE_D5,4,  NOTE_E5,4,
  NOTE_C5, 4,  NOTE_A4,4,  NOTE_A4,4, REST,4,

  REST,8, NOTE_D5, 4,  NOTE_F5,8,  NOTE_A5,4,  NOTE_G5,8,  NOTE_F5,8,
  NOTE_E5, -4,  NOTE_C5,8,  NOTE_E5,4,  NOTE_D5,8,  NOTE_C5,8,
  NOTE_B4, 4,  NOTE_B4,8,  NOTE_C5,8,  NOTE_D5,4,  NOTE_E5,4,
  NOTE_C5, 4,  NOTE_A4,4,  NOTE_A4,4, REST, 4,

  NOTE_E5,2, NOTE_C5,2,
  NOTE_D5,2, NOTE_B4,2,
  NOTE_C5,2, NOTE_A4,2,
  NOTE_B4,1,

  NOTE_E5,2, NOTE_C5,2,
  NOTE_D5,2, NOTE_B4,2,
  NOTE_C5,4, NOTE_E5,4, NOTE_A5,2,
  NOTE_GS5,1,

  NOTE_E5, 4,  NOTE_B4,8,  NOTE_C5,8,  NOTE_D5,4,  NOTE_C5,8,  NOTE_B4,8,
  NOTE_A4, 4,  NOTE_A4,8,  NOTE_C5,8,  NOTE_E5,4,  NOTE_D5,8,  NOTE_C5,8,
  NOTE_B4, -4,  NOTE_C5,8,  NOTE_D5,4,  NOTE_E5,4,
  NOTE_C5, 4,  NOTE_A4,4,  NOTE_A4,4, REST,4,

  REST,8, NOTE_D5, 4,  NOTE_F5,8,  NOTE_A5,4,  NOTE_G5,8,  NOTE_F5,8,
  REST,8, NOTE_E5, 4,  NOTE_C5,8,  NOTE_E5,4,  NOTE_D5,8,  NOTE_C5,8,
  REST,8, NOTE_B4, 4,  NOTE_C5,8,  NOTE_D5,4,  NOTE_E5,4,
  REST,8, NOTE_C5, 4,  NOTE_A4,8,  NOTE_A4,4, REST, 4,
};

int notes = sizeof(melody) / sizeof(melody[0]) / 2; 
int wholenote = (60000 * 4) / tempo;

void playSong() {
  int divider = 0, noteDuration = 0;

  // Start the motor
  digitalWrite(motor, HIGH);

  for (int thisNote = 0; thisNote < notes * 2; thisNote += 2) {
    divider = melody[thisNote + 1];
    if (divider > 0) {
      noteDuration = wholenote / divider;
    } else if (divider < 0) {
      noteDuration = (wholenote / abs(divider)) * 1.5;
    }

    // Alternate servo motion
    if ((thisNote / 16) % 2 == 0) { // Alternate every sixteen notes
      movePos1();
    } else {
      movePos2();
    }

    tone(buzzer, melody[thisNote], noteDuration * 0.9);
    delay(noteDuration);
    noTone(buzzer);
  }

  // Stop the motor
  digitalWrite(motor, LOW);
}

void setup() {
  pinMode(buzzer, OUTPUT);
  pinMode(motor, OUTPUT);

  servo1.attach(3);
  servo2.attach(5);

  Serial.begin(9600);
  Serial.println("Starting Tetris Theme...");

  delay(1000); // add a delay to allow the servos to initialize
  playSong();
  
}

void loop() {

}
