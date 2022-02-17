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

// For HC-06

SoftwareSerial BtkeySerial(BTKEY_RX_PIN, BTKEY_TX_PIN); // RX, TX

int16_t btkey_init(uint8_t id)
{
  if(id == PP_SENSOR_TYPE_BTKEY){
    pp_sensor[id].isEnable = 1;
    btkey_enable(id);
  }
  return 0;

}

int16_t btkey_enable(uint8_t id)
{
  BtkeySerial.begin(9600);
}

int16_t btkey_disable(uint8_t id)
{
  
}

uint16_t btkey_getBtKey(uint8_t id)
{
  uint8_t keyTmp = 0;

  if(id != PP_SENSOR_TYPE_BTKEY){
    return 0;
  }
  
  if (BtkeySerial.available()) {
    keyTmp = BtkeySerial.read();
    if ( keyTmp >= BTKEY_CMD_START && keyTmp < BTKEY_CMD_MAX){
      BtkeySerial.write(keyTmp);
      return keyTmp;
    }
  }
  
  return 0;
}

uint16_t btkey_sendData(uint8_t data)
{
  return 0;
}

