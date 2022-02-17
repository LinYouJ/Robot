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

#include "ultrasound.h"
#include "acceler.h"
#include "bluetoothKey.h"
#include "custom.h"


volatile uint8_t btn_mode = BTN_MODE_NONE;

uint8_t auto_edge_cnt = 0;
uint8_t auto_turn_cnt = 0;
uint8_t auto_fight_cnt = 0;
int16_t auto_distance_0 = NO_DETECT, auto_distance_1 = NO_DETECT;
int16_t auto_acce_x, auto_acce_y, auto_acce_z;
int16_t auto_ir_data_0, auto_ir_data_1;
int16_t auto_time_cnt = 0;
uint32_t auto_millis_cnt = 0;

void custom_setup()
{
}

void custom_loop()
{ 
  uint16_t btn_key = 0; 

  
  uart_disableMotor();

  // wait the key to start machine
  while((btn_key = GP_getkeyStatus()) < 1) {  
    if(uart_isConnectToPC() != 0){
      return;
    }
  }
  
  while(uart_isUartMode == 0){  
    custom_gamepadKeyFun();
    
    if(uart_isConnectToPC() != 0){
      return;
    }    
  } 
}

int16_t custom_gamepadKeyFun()
{  
  uint16_t btn_key = 0, btn_dir = 0, btn_dirL = 0, btn_dirR = 0;
  int16_t acce_z;
  
  if((btn_dir = GP_getDir4Way()) != 0){
    Serial.print("GPDIRKEY=");  Serial.println(btn_key); 
    do{
      switch(btn_dir){
        case BTN_DIR_RIGHT://按鍵-右
          do {
            SetFrameRun(14, 75); //(動作編號是幾號，從A動作啦到B動作要花多久ms)
            SetFrameRun(12, 45);
          } while((btn_dir = GP_getDir4Way()) == BTN_DIR_RIGHT);
          SetFrameRun(1, 10);
         
        break;
        
        case BTN_DIR_BACKWARD://按鍵-後
        {
          uint8_t jumpFlag = 0;
             SetFrameRun(2, 120);
             SetFrameRun(3, 100);
             //SetFrameRun(8, 30);
          do {
            SetFrameRun(8, 80);
            SetFrameRun(9, 130);
            if((btn_dir = GP_getDir4Way()) != BTN_DIR_BACKWARD){
              jumpFlag = 1;
              break;
            }
            SetFrameRun(10, 80);
            SetFrameRun(11, 130);
          } while((btn_dir = GP_getDir4Way()) == BTN_DIR_BACKWARD);
          
          if(jumpFlag == 1){
            SetFrameRun(9, 30);
            SetFrameRun(10, 60);
          }else {
            SetFrameRun(11, 30);
            SetFrameRun(8, 60);
          }
        }  
        SetFrameRun(1, 10);
      
        break;
        
        case BTN_DIR_LEFT://按鍵-左
          do {
             SetFrameRun(13, 75);
             SetFrameRun(12, 45);
           } while((btn_dir = GP_getDir4Way()) == BTN_DIR_LEFT);
          SetFrameRun(1, 10);
          
        break;
        
        case BTN_DIR_FORWARD://按鍵-前
        {
          uint8_t jumpFlag = 0;
          
          SetFrameRun(2, 140);
          SetFrameRun(3, 100);
         // SetFrameRun(4, 15);
          do {
            SetFrameRun(4, 60);
            SetFrameRun(5, 110);
            
            if((btn_dir = GP_getDir4Way()) != BTN_DIR_FORWARD){
              jumpFlag = 1;
              break;
            }
            SetFrameRun(6, 60);
            SetFrameRun(7, 110);
          } while((btn_dir = GP_getDir4Way()) == BTN_DIR_FORWARD);
          
          if(jumpFlag == 1){
            SetFrameRun(5, 30);
            SetFrameRun(6, 60);
          }else {
            SetFrameRun(7, 30);
            SetFrameRun(4, 60);
          }
        } 
        SetFrameRun(1, 10);
        
        break;   
      }
      btn_dir = 0;
    } while((btn_dir = GP_getDir4Way()) != 0);
    
  }

  
  if((btn_key = GP_getkeyStatus()) != 0){
    do{
      switch(btn_key){
        
        case BTN_KEY_TRIANGLE://按鍵-三角

         do{     
  
         }while((btn_dir = GP_getkeyStatus()) == BTN_KEY_TRIANGLE); 

         break;
  
        case BTN_KEY_CIRCLES://按鍵-圈圈
 
          do {

          } while((btn_dir = GP_getkeyStatus()) == BTN_KEY_CIRCLES); 

        break;

        case BTN_KEY_CROSS://按鍵-叉叉
          do {

          } while((btn_dir = GP_getkeyStatus()) == BTN_KEY_CROSS);
                 
        break;

        case BTN_KEY_SQUARE://按鍵-方塊
              SetFrameRun(35, 100);
              SetFrameRun(36, 150);
              SetFrameRun(37, 250);
              //SetFrameRun(38, 200);//
              SetFrameRun(39, 0); 
              SetFrameRun(40, 100);//  SetFrameRun(40, 200);
              SetFrameRun(41, 200);//SetFrameRun(41, 350);
              SetFrameRun(37, 50);//SetFrameRun(37, 250);
              SetFrameRun(1,10);//SetFrameRun(1, 200);
          do {

          } while((btn_dir = GP_getkeyStatus()) == BTN_KEY_SQUARE);

        break;      

        case BTN_KEY_L1://按鍵-L1

          do {
            SetFrameRun(43, 200);
            SetFrameRun(12, 45);
          } while((btn_dir = GP_getkeyStatus()) == BTN_KEY_L1);
          SetFrameRun(1, 10);
            
        break;

        case BTN_KEY_R1://按鍵-R1

          do {
            SetFrameRun(44, 200);
            SetFrameRun(12, 45);
          } while((btn_dir = GP_getkeyStatus()) == BTN_KEY_R1);
          SetFrameRun(1, 10); 

        break;

        case BTN_KEY_L2://按鍵-L2
            SetFrameRun(26, 100);
          do {
            SetFrameRun(27, 50);
            SetFrameRun(28, 90);
            SetFrameRun(29, 60);
            SetFrameRun(30, 110);
            SetFrameRun(31, 80);
            SetFrameRun(26, 90);   
          } while((btn_dir = GP_getkeyStatus()) == BTN_KEY_L2);
          SetFrameRun(1, 10);
        break;

        case BTN_KEY_R2://按鍵-R2
            SetFrameRun(26, 100);
          do {
            SetFrameRun(32, 50);
            SetFrameRun(33, 90);
            SetFrameRun(30, 60);
            SetFrameRun(29, 110);
            SetFrameRun(34, 80);
            SetFrameRun(26, 90);  
          } while((btn_dir = GP_getkeyStatus()) == BTN_KEY_R2);
          SetFrameRun(1, 10);  
        break;

        case BTN_KEY_SELECT://按鍵-SELECT
          uart_disableMotor();
        break;
        
        case BTN_KEY_START://按鍵-START
          SetFrameRun(19, 500);
          SetFrameRun(1, 100);
        break;
        
        case BTN_KEY_L3://按鍵-左邊香菇頭L3

          SetFrameRun(20, 200);
          SetFrameRun(21, 350);
          SetFrameRun(22, 450);
          SetFrameRun(23, 400);
          SetFrameRun(24, 350);
          delay(300);
          SetFrameRun(25, 200);
          break;

        case BTN_KEY_R3://按鍵-右邊香菇頭R3

          SetFrameRun(15, 350);
          SetFrameRun(16, 650);
          SetFrameRun(17, 700);
          delay(100);
          SetFrameRun(25, 200);
      
        break;
      }
    } while((btn_key = GP_getkeyStatus()) != 0);  
  }
  return 0;
}
