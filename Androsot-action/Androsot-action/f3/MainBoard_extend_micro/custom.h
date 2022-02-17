#ifndef __CUSTOM_H__
#define __CUSTOM_H__

// for input mode
enum{
  BTN_MODE_GAMEPAD = 0,
  BTN_MODE_BT,
  BTN_MODE_AUTO,
  BTN_MODE_NONE
};


// for auto mode
enum{
  AUTOKEY_DIR_RIGHT = 1,
  AUTOKEY_DIR_BACKWARD, // 2
  AUTOKEY_DIR_LEFT,     // 3
  AUTOKEY_DIR_FORWARD,  // 4
  AUTOKEY_TRIANGLE,     // 5
  AUTOKEY_CIRCLES,      // 6
  AUTOKEY_CROSS,        // 7
  AUTOKEY_SQUARE,       // 8
  AUTOKEY_L1,           // 9
  AUTOKEY_R1,           // 10
  AUTOKEY_L2,           // 11
  AUTOKEY_R2,           // 12
  AUTOKEY_SELECT,       // 13
  AUTOKEY_START,        // 14
  AUTOKEY_L3,           // 15
  AUTOKEY_R3,           // 16
  AUTOKEY_MAX
};

// for auto mode 
#define SENSOR_IR_EDGE  120
#define SENSOR_SONAR_FIGHT  40

#define AUTO_GET_DATA_CNT_MAX 4

#define AUTO_ACCE_Z_FACE_DOWM_MAX 580
#define AUTO_ACCE_Z_FACE_UP_MAX 420


#endif
