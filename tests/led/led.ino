void setup() {
    pinMode(LED_BUILTIN, OUTPUT); // Set the onboard LED pin as output
    Serial.begin(9600); // Initialize serial communication at 9600 baud
}

void loop() {
    // Blink the onboard LED and print status to Serial
    digitalWrite(LED_BUILTIN, HIGH); // Turn the LED on
    Serial.println("LED is ON");
    delay(1000); // Wait for 1 second

    digitalWrite(LED_BUILTIN, LOW); // Turn the LED off
    Serial.println("LED is OFF");
    delay(1000); // Wait for 1 second
}