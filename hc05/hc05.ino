#include<Wire.h>
#include<SoftwareSerial.h>
/*   
FIRA01 Master
Address +ADDR:98d3:91:fd7dca

FIRA09 Server
 +ADDR:98d3:c1:fd3900 
*/

/*
FIRA03 Master
+ADDR:98d3:11:fc12ed
pswd:101010

FIRA10-10 Server
+ADDR:98d3:11:fc12e9
pswd:101010
*/
/*
FIRA02-2
+ADDR:98d3:c1:fd385f
pswd:020202

FIRA05 Server
+ADDR:98d3:b1:fd3ba4
*/


SoftwareSerial BTSerial(10, 11);  //hc05 rx ; hc05 tx

void setup(){
    pinMode(9 ,OUTPUT);
    digitalWrite(9, HIGH);
    Serial.begin(9600);
    Serial.println("Enter AT commands");
    BTSerial.begin(38400);
}

void loop(){
    if (BTSerial.available()){
        Serial.write(BTSerial.read());
    }
    if (Serial.available()){
        BTSerial.write(Serial.read());
    }
}
