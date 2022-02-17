#ifndef __BLUETOOTHKEY_H__
#define __BLUETOOTHKEY_H__

#define BTKEY_TX_PIN  15
#define BTKEY_RX_PIN  14

int16_t btkey_init(uint8_t id);
int16_t btkey_enable(uint8_t id);
int16_t btkey_disable(uint8_t id);




enum{
  BTKEY_CMD_START = 'A',
  BTKEY_CMD_RIGHT,        // 'B'
  BTKEY_CMD_BACKWARD,     // 'C'
  BTKEY_CMD_LEFT,         // 'D'
  BTKEY_CMD_FORWARD,      // 'E'
  BTKEY_CMD_SIDE_KICK,    // 'F'
  BTKEY_CMD_RIGHT_HOOK,   // 'G'
  BTKEY_CMD_SEAT,         // 'H'
  BTKEY_CMD_LEFT_HOOK,    // 'I'
  BTKEY_CMD_LEFT_SIDEWAY, // 'J'
  BTKEY_CMD_RIGHT_SIDEWAY,// 'K'
  BTKEY_CMD_LEFT_PUNCH,   // 'L'
  BTKEY_CMD_RIGHT_PUNCH,  // 'M'
  BTKEY_CMD_SELECT,       // 'N'
  BTKEY_CMD_GETUP_FORWARD,// 'O'
  BTKEY_CMD_GETUP_BACKWARD,// 'P'
  BTKEY_CMD_MAX
};

#endif
