from enum import IntEnum, unique
import serial
import time
import struct

@unique
class CommandID(IntEnum):
    Forward = 1
    Backward = 2
    MoveLeft = 4
    MoveRight = 8
    TurnLeft = 16
    TurnRight = 32
    SlideLeft = 64
    SlideRight = 128
    Kick = 256
    Start = 512

class Robot:
    def __init__(self, id, port, baudrate=115200) -> None:
        assert id > 0 and id < 256, 'ID must be between 1 and 255'
        self.id = id
        self.com = serial.Serial(port, baudrate=baudrate)
        time.sleep(1)

    def __del__(self):
        self.com.close()

    def start(self):
        self.send_pkt(CommandID.Start)
    
    def forward(self):
        self.send_pkt(CommandID.Forward)

    def backward(self):
        self.send_pkt(CommandID.Backward)

    def move_left(self):
        self.send_pkt(CommandID.MoveLeft)

    def move_right(self):
        self.send_pkt(CommandID.MoveRight)

    def turn_left(self):
        self.send_pkt(CommandID.TurnLeft)

    def turn_right(self):
        self.send_pkt(CommandID.TurnRight)

    def slide_left(self):
        self.send_pkt(CommandID.SlideLeft)

    def slide_right(self):
        self.send_pkt(CommandID.SlideRight)

    def kick(self):
        self.send_pkt(CommandID.Kick)

    def send_pkt(self, cmd):
        pkg = struct.pack('BBB', 0xff, self.id, cmd)
        cs = 0xff & sum(pkg)
        self.com.write(pkg)
        time.sleep(0.2)
        self.com.write(struct.pack('B', cs))
    
# test program
if __name__ == '__main__':
    robot = Robot(1, 'COM14')
    robot.start()

    for i in range(10):
        robot.forward()