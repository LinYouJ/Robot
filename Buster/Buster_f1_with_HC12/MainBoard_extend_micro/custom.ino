/*
custom.ino

Gatsby Jan
gatsby.jan@ppt.com.tw

Copyright (c) 2018 ~ 2019 CreatorArk technology

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
#include "custom.h"

volatile uint8_t btn_mode = BTN_MODE_NONE;

void custom_setup()
{
  btkey_init();
}

void custom_loop()
{

  uart_disableMotor();

  

  while (uart_isUartMode == 0)
  {
    btkey_update();
    custom_func();

    if (uart_isConnectToPC() != 0)
    {
      return;
    }
  }
}

void custom_func(){
  uint16_t cmd = btkey_getBtKey();
  uint16_t btn_dir;
  if(cmd){
    Serial.println(cmd);
  }
  
  switch (cmd)
  {
  case FORWARD: // UP
    SetFrameRun(2, 140);
    SetFrameRun(3, 100);

    SetFrameRun(4, 60);
    SetFrameRun(5, 110);

    SetFrameRun(5, 30);
    SetFrameRun(6, 60);

    SetFrameRun(1, 10);
    break;

  case BACKWARD: // DOWN
    SetFrameRun(2, 120);
    SetFrameRun(3, 100);

    SetFrameRun(8, 80);
    SetFrameRun(9, 130);

    SetFrameRun(9, 30);
    SetFrameRun(10, 60);

    SetFrameRun(1, 10);
    break;

  case MOVE_LEFT: // LEFT
    SetFrameRun(13, 75);
    SetFrameRun(12, 45);

    SetFrameRun(1, 10);
    break;

  case MOVE_RIGHT: //RIGHT

    SetFrameRun(14, 75);
    SetFrameRun(12, 45);

    SetFrameRun(1, 10);
    break;

  case TURN_LEFT: //L1
    SetFrameRun(43, 200);
    SetFrameRun(12, 45);

    SetFrameRun(1, 10);
    break;

  case TURN_RIGHT: // R1
    SetFrameRun(44, 200);
    SetFrameRun(12, 45);

    SetFrameRun(1, 10);
    break;

  case SLIDE_LEFT: // L2
    SetFrameRun(26, 100);

    SetFrameRun(27, 50);
    SetFrameRun(28, 90);
    SetFrameRun(29, 60);
    SetFrameRun(30, 110);
    SetFrameRun(31, 80);
    SetFrameRun(26, 90);

    SetFrameRun(1, 10);
    break;

  case SLIDE_RIGHT: // R2
    SetFrameRun(26, 100);

    SetFrameRun(32, 50);
    SetFrameRun(33, 90);
    SetFrameRun(30, 60);
    SetFrameRun(29, 110);
    SetFrameRun(34, 80);
    SetFrameRun(26, 90);

    SetFrameRun(1, 10);
    break;

  case KICK: // Square
    SetFrameRun(35, 100);
    SetFrameRun(36, 150);
    SetFrameRun(37, 250);
    SetFrameRun(39, 0);
    SetFrameRun(40, 100);
    SetFrameRun(41, 200);
    SetFrameRun(37, 50);
    SetFrameRun(1, 10);
    break;

  case START:
    SetFrameRun(19, 500);
    SetFrameRun(1, 100);
    break;
  
  default:
    break;
  }
}
