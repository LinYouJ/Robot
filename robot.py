import numpy as np
from math import atan2,degrees,sin,cos
from time import sleep
class Robot():
    def __init__(self,name=None):
        self.name=name
        self.Robot_cpos=np.array([0,0],dtype="float16")
        
    def getCenter(self):
        return self.Robot_cpos
    
    def turnTO(self,direction):
        if(direction=='right'):
            #self.Robot_fpos
            print("向右調整")
        elif(direction=="left"):
            print("向左調整")

    def move(self,pathlen):
        if(pathlen<10): 
            print("停止，開始瞄準")
            return 1
        elif(pathlen<15): 
            print('開始減速')
            return 2
        else: 
            print("前進")
            return 0

    def kickball(self,robotpos,gatepos,ballpos,hyptlen):
        GB_deg=degrees(atan2(ballpos[1]-gatepos[1],ballpos[0]-gatepos[0]))
        BR_deg=degrees(atan2(robotpos[1]-ballpos[1],robotpos[0]-ballpos[0]))
        kick_area=-1*hyptlen*sin(BR_deg)
        if(BR_deg<GB_deg and kick_area>5):
            print("右側移")
        elif(BR_deg>GB_deg and kick_area>5):
            print("左側移")
        else:
            sleep(3)
            if(BR_deg<GB_deg):
                print("右踢")
            elif(BR_deg>GB_deg):
                print("左踢")

class Enemy():
    def __init__(self):
        self.enemy_pos=np.array([50,50],dtype="float16")
    def coordinate(self):
        return self.enemy_pos