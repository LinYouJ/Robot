import numpy as np
import math
from object.ball import Ball
from object.robot import Robot


ball=Ball()
robot=Robot()
Gate=np.array([1,1])

def aim_Gate():
    Robotcenter=robot.getCenter()
    Robotfront=robot.getFront()
    Ballpoint=ball.ballPos()
    ctr2ball=math.hypot(Ballpoint[0]-Robotcenter[0],Ballpoint[1]-Robotcenter[1])
    RB_deg=math.degrees(math.atan2(Robotcenter[1]-Ballpoint[1],Robotcenter[0]-Ballpoint[0]))
    if(RB_deg<0):
        RB_deg+=360
    Robotdeg=math.degrees(math.atan2(Robotfront[1]-Robotcenter[1],Robotfront[0]-Robotcenter[0])) 
    if(Robotdeg<0):
        Robotdeg+=360
    RBdiff=Robotdeg-RB_deg
    if(RBdiff>0 and RBdiff<=180):
        robot.turnTO("right")
        aim_Gate()
    elif(RBdiff<0 or RBdiff>180):
        robot.turnTO("left")
        aim_Gate()
    else:
        result=robot.move(ctr2ball)
        if(result==1):
            robot.kickball()
        else:
            aim_Gate()

while(1):
    #測試
    # start=str(input("輸入y或Y開始執行動作:"))
    # if(start!='y' and start!='Y'):
    #     break
    # robot.Robot_cpos[0],robot.Robot_cpos[1]=input("input robotcentr coordinate:").split()
    # robot.Robot_fpos[0],robot.Robot_fpos[1]=input("input robotfront coordinate:").split()
    # ball.ball_pos[0],ball.ball_pos[1]=input("input ball coordinate:").split()
    #主程式
    Robotcenter=robot.getCenter()
    Robotfront=robot.getFront()
    Ballpoint=ball.ballPos()
    Targetpoint=ball.targetPos(Gatepoint=Gate)
    #距離區
    ctr2tar=math.hypot(Targetpoint[0]-Robotcenter[0],Targetpoint[1]-Robotcenter[1])
    ctr2front=math.hypot(Robotfront[0]-Robotcenter[0],Robotfront[1]-Robotcenter[1])
    tar2front=math.hypot(Robotfront[0]-Targetpoint[0],Robotfront[1]-Targetpoint[1])
    diff_cos=(ctr2tar**2+ctr2front**2-tar2front**2)/(2*ctr2front*ctr2tar)
    #角度區
    RT_deg=math.degrees(math.atan2(Targetpoint[1]-Robotcenter[1],Targetpoint[0]-Robotcenter[0]))
    if(RT_deg<0):
        RT_deg+=360
    Robotdeg=math.degrees(math.atan2(Robotfront[1]-Robotcenter[1],Robotfront[0]-Robotcenter[0]))
    if(Robotdeg<0):
        Robotdeg+=360
    RTdiff=Robotdeg-RT_deg
    theta=0

    #運算區
    print("目標點位置[%.2f,%.2f]"%(RT_deg,ctr2tar)) 
    if(RT_deg==90):
        print("目標在正向y軸")
        result=robot.y_walk(ctr2tar)
        if(result==1):
            aim_Gate()

    elif(RT_deg>=0 and RT_deg<90): 
        print("目標在第一象限")
        theta=RT_deg
        if(theta>80 and theta<95): #y軸運算
            if(RTdiff<10 and RTdiff>-10):
                result=robot.y_walk(ctr2tar)  
                if(result==1):
                    aim_Gate()
            elif(RTdiff>10 and RTdiff<180):
                robot.turnTO('right')
            else:
                robot.turnTO('left')
        else:           #x軸運算
            if(Robotdeg<10 and (Robotdeg-360)>-10):
                robot.x_walk(theta)   
            elif(Robotdeg>10 and RTdiff<180):
                robot.turnTO('right')
            else:
                robot.turnTO('left')
        

    elif(RT_deg>90 and RT_deg<=180):
        print("目標在第二象限")
        theta=180-RT_deg
        if(theta>80 and theta<95): #y軸運算
            if(RTdiff<10 and RTdiff>-10):
                result=robot.y_walk(ctr2tar)
                if(result==1):
                    aim_Gate()
            elif(RTdiff>10 and RTdiff<180):
                robot.turnTO('right')
            else:
                robot.turnTO('left')
        else:             #x軸運算
            if(Robotdeg>170 and Robotdeg<190):
                robot.x_walk(theta)  
            elif(RTdiff>(theta+10) and RTdiff<180):
                robot.turnTO('right')
            else:
                robot.turnTO('left')
    
    print("=================")



