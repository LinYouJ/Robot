import numpy as np
from math import atan2,degrees,sin
from time import sleep
from motion import Robot as RB

class Robot():
    def __init__(self,id=1,port='COM14'):
        self.id = id
        self.action = RB(self.id,port)
        self.Robot_cpos=np.array([0,0],dtype="float16")
        self.deg = None
    def stand(self):
        self.action.start()

    def getCenter(self):
        return self.Robot_cpos
    
    def turnTO(self,direction):
        if(direction=='right'):
            print("向右調整")
            self.action.turn_right()
        elif(direction=="left"):
            print("向左調整")
            self.action.turn_left()

    def move(self,pathlen):
        if(pathlen<10): 
            print("停止，開始瞄準")
            return 1
        elif(pathlen<15): 
            print('開始減速')
            self.action.forward()
            return 2
        else: 
            print("前進")
            self.action.forward()
            return 0

    def slide(self,order):
        if order == 0:
            self.action.move_right()
            print('右滑')
        elif order == 1:
            self.action.move_left()
            print('左滑')

    def kickball(self,robotpos,gatepos,ballpos,hyptlen):
        GB_deg=degrees(atan2(ballpos[1]-gatepos[1],ballpos[0]-gatepos[0]))
        BR_deg=degrees(atan2(robotpos[1]-ballpos[1],robotpos[0]-ballpos[0]))
        kick_area=-1*hyptlen*sin(BR_deg)
        if(BR_deg<GB_deg and kick_area>5):
            print("右側移")
            self.action.move_right()
        elif(BR_deg>GB_deg and kick_area>5):
            print("左側移")
            self.action.move_left()
        else:
            sleep(1)
            print("左踢")
            self.action.kick()
