#include<Wire.h>
#include<SoftwareSerial.h>

//SoftwareSerial BTSerial(10, 11);  //hc05 rx ; hc05 tx
SoftwareSerial BTSerial(15, 14);
void setup(){
    //pinMode(9 ,OUTPUT);
    //digitalWrite(9, HIGH);
    Serial.begin(9600);
    Serial.println("Enter AT commands");
    BTSerial.begin(115200);
}

void loop(){
    if (BTSerial.available()){
        //char tmp = BTSerial.read();
        Serial.write(BTSerial.read());
        delay(10);
    }
    if (Serial.available()){
        BTSerial.write(Serial.read());
        delay(10);
    }
}
