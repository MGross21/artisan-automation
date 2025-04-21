void setup() {
    for (int pin = 0; pin <= 13; pin++) { // Assuming an Arduino Uno with pins 0-13
        pinMode(pin, OUTPUT);
        digitalWrite(pin, HIGH);  // Set each pin HIGH
    }
    Serial.begin(9600);
    Serial.println("All pins are HIGH");
}

void loop() {}
