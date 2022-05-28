#include <SoftwareSerial.h>   
SoftwareSerial BT(11, 10); // Tx, Rx

char var;  

void setup() {
  Serial.begin(9600);  
  Serial.println("BT is ready!");
  BT.begin(38400);
}

void loop() {
  if (Serial.available()) {
    var = Serial.read();
    BT.print(var);
  }

  if (BT.available()) {
    var = BT.read();
    Serial.print(var);
  }
}
