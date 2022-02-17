#ifndef __CUSTOM_H__
#define __CUSTOM_H__

// for input mode
enum{
  BTN_MODE_GAMEPAD = 0,
  BTN_MODE_BT,
  BTN_MODE_AUTO,
  BTN_MODE_NONE
};

#define FORWARD 1
#define BACKWARD 2
#define MOVE_LEFT 4
#define MOVE_RIGHT 8
#define TURN_LEFT 16
#define TURN_RIGHT 32
#define SLIDE_LEFT 64
#define SLIDE_RIGHT 128
#define KICK 256
#define START 512

#endif
