/*
ultrasound.ino
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

#include "ultrasound.h"

// For module HY-SRF05 / HY-SRF04

NewPing *sonar_0 = 0;
NewPing *sonar_1 = 0;
NewPing *sonar_2 = 0;
NewPing *sonar_3 = 0;

uint16_t us_init(uint8_t id)
{
  if(id == PP_SENSOR_TYPE_ULTRASONIC_0 ||
    id == PP_SENSOR_TYPE_ULTRASONIC_1 ||
    id == PP_SENSOR_TYPE_ULTRASONIC_2 ||
    id == PP_SENSOR_TYPE_ULTRASONIC_3 
    ){
    pp_sensor[id].isEnable = 1;
    us_enable(id);
  }
  
  return 0;
}

int16_t us_enable(uint8_t id)
{
  switch(id){
    case PP_SENSOR_TYPE_ULTRASONIC_0:
      sonar_0 = new NewPing(US_TRIGGER_0, US_ECHO_0, US_DISTANCE_MAX);
    break;

    case PP_SENSOR_TYPE_ULTRASONIC_1:
      sonar_1 = new NewPing(US_TRIGGER_1, US_ECHO_1, US_DISTANCE_MAX);
    break;

    case PP_SENSOR_TYPE_ULTRASONIC_2:
      sonar_2 = new NewPing(US_TRIGGER_2, US_ECHO_2, US_DISTANCE_MAX);
    break;

    case PP_SENSOR_TYPE_ULTRASONIC_3:
      sonar_3 = new NewPing(US_TRIGGER_3, US_ECHO_3, US_DISTANCE_MAX);
    break;
    
  }
  
  return -1;
}

uint16_t us_disable(uint8_t id)
{
  return 0;
}

uint16_t us_getDistance(uint8_t id)
{
  switch(id){
    case PP_SENSOR_TYPE_ULTRASONIC_0:
      if(pp_sensor[id].isEnable == 1){
        return sonar_0->ping_cm();
      }
    break;

    case PP_SENSOR_TYPE_ULTRASONIC_1:
      if(pp_sensor[id].isEnable == 1){
        return sonar_1->ping_cm();
      }
    break;

    case PP_SENSOR_TYPE_ULTRASONIC_2:
      if(pp_sensor[id].isEnable == 1){
        return sonar_2->ping_cm();
      }
    break;

    case PP_SENSOR_TYPE_ULTRASONIC_3:
      if(pp_sensor[id].isEnable == 1){
        return sonar_3->ping_cm();
      }
    break;
  }
  return -1;
}


