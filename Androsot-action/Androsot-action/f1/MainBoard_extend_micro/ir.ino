/*
ir.ino

Gatsby Jan
gatsby.jan@ppt.com.tw

Copyright (c) 2018 Phoenix Pioneer technology

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

#include "ir.h"

// For module GP2Y0A41SK0F (sharp)

uint16_t ir_init(uint8_t id)
{
  if((id == PP_SENSOR_TYPE_IR_0) ||
    (id == PP_SENSOR_TYPE_IR_1)){
    pp_sensor[id].isEnable = 1;
    ir_enable(id);
  }
  return 0;
}

uint16_t ir_enable(uint8_t id)
{
  analogReference(EXTERNAL);
  
  return 0;
}

uint16_t ir_disable(uint8_t id)
{
  return 0;
}

int16_t ir_getDirValue(uint8_t id)
{
  switch(id){
    case PP_SENSOR_TYPE_IR_0:
      if(pp_sensor[id].isEnable == 1) {
        return 13 * pow(analogRead(IR_PIN_0) * 0.0048828125, -1);
      }
    break;

    case PP_SENSOR_TYPE_IR_1:
      if(pp_sensor[id].isEnable == 1) {
        return 13 * pow(analogRead(IR_PIN_1) * 0.0048828125, -1);
      }
    break;
  }
  return -1;
}

