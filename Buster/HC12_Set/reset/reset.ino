#include <SoftwareSerial.h>
//SoftwareSerial HC12(7,6); // HC-12 TX Pin, HC-12 RX Pin
SoftwareSerial HC12(15,14);
void setup() {
  Serial.begin(115200);             // Serial port to computer
  HC12.begin(115200);               // Serial port to HC12
}
void loop() {
  while (HC12.available()) {        // If HC-12 has data
    Serial.write(HC12.read());      // Send the data to Serial monitor
  }
  while (Serial.available()) {      // If Serial monitor has data
    HC12.write(Serial.read());      // Send that data to HC-12
  }
}
