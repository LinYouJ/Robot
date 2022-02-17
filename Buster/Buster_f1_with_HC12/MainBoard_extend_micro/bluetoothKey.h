#ifndef __BLUETOOTHKEY_H__
#define __BLUETOOTHKEY_H__

#define BTKEY_TX_PIN  14
#define BTKEY_RX_PIN  15

int16_t btkey_init();
uint16_t btkey_update();
uint16_t btkey_getBtKey();

#define ROBOT_ID 1 // 1-256
#define CMD_QUEUE_MAX 20

/*
0xFF - Starting byte
RobotID: 8bit
Command_LSB: 8bit
Command_MSB: 8bit
CheckSum: 8bit

=> Total: 40bit (5byte)
*/

enum ReciveState {
  Wait = 0,
  RobotID,
  Command,
  Checksum
};

#endif
