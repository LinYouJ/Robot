import numpy as np
from math import degrees,atan2,dist
from ball import Ball
from robot import Robot
from detect import detect
from time import sleep
from motion import Robot as RB
import cv2
#blue = 左, green = 右
detect_=detect()
robot=Robot()
ball=Ball()
robot.stand()
decision = False 
result = 0 
aim_gate = False
while True: 
    #取得兩色塊座標與角度
    y_center, b_center, deg, img=detect_.get_color_position()

    #顯示畫面
    cv2.circle(img,y_center,5,(0,255,255),2)
    cv2.circle(img,b_center,5,(255,0,0),2)  
    cv2.imshow('checkImg',img)
    cv2.waitKey(3)

    #取得場地座標
    initLoc=detect_.init_location
    #A=右上 , B=左上 , C=左下 , D=右下 , R_BOTTOM=左下座標
    R_BOTTOM=[]
    D_X,B_X,C_Y,A_Y,R_BOTTOM=detect_.x_l,detect_.x_r,detect_.y_t,detect_.y_b,detect_.coordinate
    
    #選擇進攻球門
    Gate_R = np.array([R_BOTTOM[0],(R_BOTTOM[1]+A_Y)*0.5],dtype="float16")
    Gate_L = np.array([initLoc[0],(initLoc[1]+B_X)*0.5],dtype="float16") 
    Gate=Gate_R
    #取得物件座標
    GroundCenter = np.array([(D_X+B_X)*0.5,(A_Y+C_Y)*0.5],dtype=float)
    Targetpoint = ball.targetPos(Gatepoint=Gate)
    Ballpoint = ball.ballPos()
    
   #輸入進攻機器人座標
    Ycenter = np.array(y_center,dtype="float16")
    Bcenter = np.array(b_center,dtype="float16")
    robot.Robot_cpos[0],robot.Robot_cpos[1]=(Ycenter+Bcenter)*0.5
    Robotcenter = robot.getCenter()

    #計算角度與距離
    Robotdeg = deg 
    if Robotdeg > 0:
        Robotdeg = 180-Robotdeg
    if Robotdeg < 0:
        Robotdeg = -180-Robotdeg
    RT_deg = degrees(atan2(Targetpoint[0] - Robotcenter[0], Targetpoint[1] - Robotcenter[1]))  
    RB_deg = degrees(atan2(Ballpoint[0] - Robotcenter[0], Ballpoint[1] - Robotcenter[1]))
    ctr2Tar = dist(Robotcenter, Targetpoint)

    #顯示數值
    print("取得完成")
    print(A_Y)
    print(B_X)
    print(C_Y)
    print(D_X)
    print(R_BOTTOM)
    print(f"左下原點{initLoc}")
    print(f"球場中心點:{GroundCenter}")  
    print(f"進攻機器人{robot.id}")
    print(f"綠色色塊[{y_center}],藍色色塊[{b_center}]")  
    print(f"機器人中心點{Robotcenter}")
    print(f"機器人面向角{Robotdeg}")
    print(f"機器人對目標角度{RT_deg}")
    print(f"機器人對球角度{RB_deg}")
    print(f"目標點位置{Targetpoint}")
    print(f"右球門{Gate_R}")
    print(f"左球門{Gate_L}")
    print("-----開始判斷------")

    #運算區
    RTdiff = Robotdeg - RT_deg
    RBdiff = Robotdeg - RB_deg
    print(f"RTdiff={RTdiff}")
    print(f"RBdiff={RBdiff}")
    if not aim_gate:  #瞄準目標點
        if Robotdeg * RT_deg < 0:
            if Robotdeg < 0:
                if Robotdeg < -90:
                    robot.turnTO('right')
                elif Robotdeg >-90:
                    robot.turnTO('left')
            elif Robotdeg >= 0:
                if Robotdeg < 90:
                    robot.turnTO('right')
                elif Robotdeg > 90:
                    robot.turnTO('left')
        else:   
            if RTdiff > 10:
                robot.turnTO('right')
            elif RTdiff < -10:
                robot.turnTO('left')
            else:
                result=robot.move(ctr2Tar)
                if result == 1:
                    aim_gate = True

    elif aim_gate:  #瞄準球門
        if Robotdeg * RB_deg < 0:
            if Robotdeg < 0:
                if Robotdeg < -90:
                    robot.turnTO('right')
                elif Robotdeg >-90:
                    robot.turnTO('left')
            elif Robotdeg >= 0:
                if Robotdeg < 90:
                    robot.turnTO('right')
                elif Robotdeg > 90:
                    robot.turnTO('left')
        else:   
            if RBdiff > 10:
                robot.turnTO('right')
            elif RBdiff < -10:
                robot.turnTO('left')
            else:
                result=robot.move(ctr2Tar)
                if result == 1:
                    robot.kickball()
                    aim_gate = False


    print("========迴圈結束======")
    sleep(2)


