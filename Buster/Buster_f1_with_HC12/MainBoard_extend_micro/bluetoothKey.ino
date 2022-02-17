/*
bluetoothKey.ino
Gatsby Jan
gatsby.jan@ppt.com.tw

Copyright (c) 2018 phoenix pioneer technology

Permission is hereby granted, free of charge, to any person obtaining a copy of this software 
and associated documentation files (the "Software"), to deal in the Software without restriction, 
including without limitation the rights to use, copy, modify, merge, publish, distribute, 
sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is 
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or 
substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING 
BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND 
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, 
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
*/

#include "bluetoothKey.h"
#include <SoftwareSerial.h>

SoftwareSerial BtkeySerial(15, 14); // RX, TX
uint8_t buff[4] = {0};
uint8_t idx = 0;
ReciveState flag = Wait;
uint32_t checksum = 0;
uint32_t time = 0;

uint16_t cmd_queue[CMD_QUEUE_MAX] = {0};
uint8_t queue_len = 0;

int16_t btkey_init()
{
  for(int i = 0; i < CMD_QUEUE_MAX; i++)
  {
    cmd_queue[i] = 0;
  }
  for(int i = 0; i < 4; i++)
  {
    buff[i] = 0;
  }
  BtkeySerial.begin(115200);
}

uint16_t btkey_update(){
  // timeout after 100ms
  if ((millis() - time) > 1000 && flag != Wait){
    flag = Wait;
    checksum = 0;
    idx = 0;
  }

  while (BtkeySerial.available())
  {
    uint8_t c = BtkeySerial.read();
    Serial.print("flag: ");
    Serial.print(flag);
    Serial.print(", c: ");
    Serial.println(c);
    switch (flag)
    {
    case Wait:
      if (c == 0xFF)
      {
        checksum = 0;
        flag = RobotID;
        time = millis();
      }
      break;

    case RobotID:
      buff[idx++] = c;
      checksum += c;
      time = millis();
      flag = Command;
      break;

    case Command:
      buff[idx++] = c;
      checksum += c;
      time = millis();
      flag = idx > 2 ? Checksum : Command;
      break;

    case Checksum:
      Serial.print("c"); Serial.println(c);
      Serial.print("checksum"); Serial.println(checksum& 0xff);
      // packet is complete and it's boardcast or for us
      if(c == (checksum & 0xff) && \
        (buff[0] == ROBOT_ID || buff[0] == 0)){
          Serial.println("yes");
        if(queue_len < CMD_QUEUE_MAX){
          cmd_queue[queue_len++] = buff[1] | (buff[2] << 8);
        }else{ // queue is full
          // discard the oldest command
          for(uint8_t i = 0; i < queue_len - 1; i++){
            cmd_queue[i] = cmd_queue[i + 1];
          }
          queue_len--;
          cmd_queue[queue_len++] = buff[1] | (buff[2] << 8);
        }
        
      }
      flag = Wait;
      idx = 0;
      checksum = 0;
      time = millis();
      break;
    }
  }
}

uint16_t btkey_getBtKey()
{
  if(queue_len == 0){
    return 0;
  }
  queue_len--;
  return cmd_queue[queue_len];
}
