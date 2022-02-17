#include <SoftwareSerial.h>
SoftwareSerial HC12(7,6); // HC-12 TX Pin, HC-12 RX Pin
void setup() {
  Serial.begin(9600);             // Serial port to computer
  HC12.begin(115200);               // Serial port to HC12

}
void loop() {

  while (Serial.available()) {      // If Serial monitor has data
    int tmp = Serial.read()-'0';
    Serial.print(tmp);
    HC12.write(tmp);      // Send that data to HC-12
  }
}
