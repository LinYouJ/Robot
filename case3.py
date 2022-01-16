import numpy as np
import math
from object.ball import Ball
from object.robot import Robot

robot=Robot()
ball=Ball()
Gate=np.array([0,0]) #假設座標

def aim_Gate(): 
        #正踢
        Robotcenter=robot.getCenter() #更新座標
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

def aim_Target(rotate):
    if(rotate=="right"): #右轉限定
        if(diff_cos<0.9 and diff_cos>-1):
            robot.turnTO('right')
        else:
            result=robot.move(ctr2Tar)
            if(result==1):
                aim_Gate()
    elif(rotate=="left"): #左轉限定
        if(diff_cos<0.9 and diff_cos>-1):
            robot.turnTO("left")
        else:
            result=robot.move(ctr2Tar)
            if(result==1):
                aim_Gate()

while(1):
    #測試
    # start=str(input("輸入任意Y 或 y開始動作:"))
    # if(start!='Y' and start!='y'):
    #     break
    # robot.Robot_cpos[0],robot.Robot_cpos[1]=input("input robot center coordinate:").split()
    # robot.Robot_fpos[0],robot.Robot_fpos[1]=input("input robot front coordinate:").split()
    # ball.ball_pos[0],ball.ball_pos[1]=input("input ball coordinate:").split()
    
    #主程式
    Robotcenter=robot.getCenter()
    Robotfront=robot.getFront()
    Ballpoint=ball.ballPos()
    Targetpoint=ball.targetPos(Gatepoint=Gate)
    RT_deg=math.degrees(math.atan2(Targetpoint[1]-Robotcenter[1],Targetpoint[0]-Robotcenter[0]))  
    if(RT_deg<0):
        RT_deg=RT_deg+360
    Robotdeg=math.degrees(math.atan2(Robotfront[1]-Robotcenter[1],Robotfront[0]-Robotcenter[0])) 
    if(Robotdeg<0):
        Robotdeg=Robotdeg+360
    RTdiff=Robotdeg-RT_deg
    ctr2Tar=math.hypot(Targetpoint[0]-Robotcenter[0],Targetpoint[1]-Robotcenter[1])
    ctr2front=math.hypot(Robotfront[0]-Robotcenter[0],Robotfront[1]-Robotcenter[1])
    front2Target=math.hypot(Targetpoint[0]-Robotfront[0],Targetpoint[1]-Robotfront[1])
    diff_cos=(ctr2Tar**2+ctr2front**2-front2Target**2)/(2*ctr2Tar*ctr2front)
    # print(RT_deg)
    # print(Robotdeg)
    # print(Targetpoint)

    #運算區
    print("目標點位置[%.2f,%.2f]"%(RT_deg,ctr2Tar)) 
    if(RT_deg==90):
        print("目標在正向y軸")
        if(RTdiff>10 and RTdiff<=180):
            aim_Target("right")
        else:
            aim_Target("left")
    elif(RT_deg>=0 and RT_deg<90):
        print("目標在第一象限")
        if(RTdiff>=0 and RTdiff<180):
            aim_Target("right")
        else:
            aim_Target("left")      
    elif(RT_deg>90 and RT_deg<=180):
        print("目標在第二象限")
        if(RTdiff>=0 and RTdiff<180):
            aim_Target("right")
        else:
            aim_Target("left") 
    elif(RT_deg>180 and RT_deg<=270):
        print("目標在第三象限")
        if(abs(RTdiff)>=0 and abs(RTdiff)<180):
            aim_Target("left")
        else:
            aim_Target("right")
    elif(RT_deg>270 and RT_deg<359):
        print("目標在第四象限")
        if(abs(RTdiff)>=0 and abs(RTdiff)<180):
            aim_Target("left")
        else:
            aim_Target("right")    
    print("=================")

