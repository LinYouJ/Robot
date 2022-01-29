import numpy as np
import math
class Ball():
    def __init__(self):
        self.ball_pos=np.array([690,490],dtype="float16")
        self.target_pos=np.array([0,0],dtype="float16")
    
    def ballPos(self):
        return self.ball_pos
    
    def targetPos(self,Gatepoint):
        GB_vec=np.array([self.ball_pos[0]-Gatepoint[0],self.ball_pos[1]-Gatepoint[1]],dtype="float16")
        GB_unit=GB_vec/math.hypot(self.ball_pos[0]-Gatepoint[0],self.ball_pos[1]-Gatepoint[1])
        GB_unit*=5
        self.target_pos[0]=self.ball_pos[0]+GB_unit[0]
        self.target_pos[1]=self.ball_pos[1]+GB_unit[1]
        return self.target_pos