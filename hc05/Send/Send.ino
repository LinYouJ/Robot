#include <SoftwareSerial.h>
SoftwareSerial BTSerial(11,10); // HC-05 TX Pin, HC-05 RX Pin
void setup() {
  Serial.begin(9600);             // Serial port to computer
  BTSerial.begin(38400);               // Serial port to HC05

}
void loop() {
  while (Serial.available()) {      // If Serial monitor has data
    int tmp = Serial.read()-'0';
    Serial.print(tmp);
    BTSerial.write(tmp);      // Send that data to HC-05
    delay(10);
  }
}
