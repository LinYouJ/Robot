/*
acceler.ino
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

#include "acceler.h"

// For GY-61  (ADXL335)

int16_t acce_init(uint8_t id)
{
  if(id == PP_SENSOR_TYPE_ACCELER){
    pp_sensor[id].isEnable = 1;
    acce_enable(id);
  }
  return 0;
}

int16_t acce_enable(uint8_t id)
{
  analogReference(EXTERNAL);
  
  return 0;
}

int16_t acce_disable(uint8_t id)
{
  return 0;
}

int16_t acce_getDirValue(uint8_t id, uint8_t dir)
{
  if(id == PP_SENSOR_TYPE_ACCELER &&
    pp_sensor[id].isEnable == 1) {
    
    switch(dir){
      case ACCE_DIR_X:
        return analogRead(ACCE_X_PIN) - 512;
      break;

      case ACCE_DIR_Y:
        return analogRead(ACCE_Y_PIN) - 512;
      break;

      case ACCE_DIR_Z:
        return analogRead(ACCE_Z_PIN) - 512;
      break;

    }
  }
  return -1;
}

