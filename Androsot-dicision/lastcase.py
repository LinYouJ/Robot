import numpy as np
from math import degrees,atan2,dist
from ball import Ball
from robot import Robot
from detect2 import detect
from time import sleep
from random import randint
import cv2
#blue = 左, green = 右
detect_=detect()
robot=Robot()
ball=Ball()
robot.stand()
result = 0
decision = False 
aim_gate = False

def determine():
    global aim_gate
    #計算角度與距離
    Robotcenter = robot.getCenter()
    Robotdeg = robot.deg 
    if Robotdeg > 0:
        Robotdeg = 180-Robotdeg
    if Robotdeg < 0:
        Robotdeg = -180-Robotdeg
    RT_deg = degrees(atan2(Targetpoint[0] - Robotcenter[0], Targetpoint[1] - Robotcenter[1]))  
    RB_deg = degrees(atan2(Ballpoint[0] - Robotcenter[0], Ballpoint[1] - Robotcenter[1]))
    ctr2Tar = dist(Robotcenter, Targetpoint)
    print(f"進攻機器人{robot.id}") 
    print(f"機器人中心點{Robotcenter}")
    print(f"機器人面向角{Robotdeg}")
    print(f"機器人對目標角度{RT_deg}")
    print(f"機器人對球角度{RB_deg}")
    print(f"目標點位置{Targetpoint}")
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

while True: 
    #取得兩色塊座標與角度
    #y_center, b_center, deg, img=detect_.get_color_position()
    #顯示畫面
    # cv2.circle(img,y_center,5,(0,255,255),2)
    # cv2.circle(img,b_center,5,(255,0,0),2)  
    # cv2.imshow('checkImg',img)
    # cv2.waitKey(3)

    #測試
    a_center = (120,70)
    b_center = (90,80)
    c_center = (60,50)
    deg = [90,160,-120]
    


    LOCATION = {}          #取得機器人座標
    LOCATION['robot1'] = np.array(a_center, dtype=float)
    LOCATION['robot2'] = np.array(b_center, dtype=float)
    LOCATION['robot3'] = np.array(c_center, dtype=float)

    initLoc=detect_.init_location   #取得場地座標
    R_BOTTOM=[]      #A=右上 , B=左上 , C=左下 , D=右下 , R_BOTTOM=左下座標
    D_X,B_X,C_Y,A_Y,R_BOTTOM=detect_.x_l,detect_.x_r,detect_.y_t,detect_.y_b,detect_.coordinate
    
    Gate_R = np.array([R_BOTTOM[0],(R_BOTTOM[1]+A_Y)*0.5],dtype="float16")     #選擇球門
    Gate_L = np.array([initLoc[0],(initLoc[1]+B_X)*0.5],dtype="float16") 
    Gate=Gate_R

    GroundCenter = np.array([(D_X+B_X)*0.5,(A_Y+C_Y)*0.5],dtype=float)       #取得物件座標
    Targetpoint = ball.targetPos(Gatepoint=Gate)
    Ballpoint = ball.ballPos()
    
    #判斷各機器人動作
    robot.id = 3    #C
    order = randint(0,1)
    robot.slide(order)
    print(robot.id)

    EX_ATTACK = []      #A,B
    EX_DISTANCE = []
    DISTANCE = []
    if len(EX_ATTACK) == 0:  #第一次迴圈
        DISTANCE.append(dist(LOCATION['robot1'],Ballpoint))
        DISTANCE.append(dist(LOCATION['robot2'],Ballpoint))
        robot.id = DISTANCE.index(min(DISTANCE)) + 1
        robot.deg = deg[robot.id]
        robot.Robot_cpos = LOCATION[f'robot{robot.id}']   
        determine()  #主攻者進攻
        sleep(0.5)
        robot.id = DISTANCE.index(max(DISTANCE)) + 1
        robot.deg = deg[robot.id]
        Targetpoint = ball.attack_track(Gate,robot.Robot_cpos)  #副攻跟隨主攻手
        robot.Robot_cpos = LOCATION[f'robot{robot.id}']
        determine()  #副攻者進攻
        sleep(0.5)
        if DISTANCE.index(min(DISTANCE)) == 0:
            EX_ATTACK.append(LOCATION['robot1'])
            EX_ATTACK.append('1')
        elif DISTANCE.index(min(DISTANCE)) == 1:
            EX_ATTACK.append(LOCATION['robot2'])
            EX_ATTACK.append('2')
        EX_DISTANCE = DISTANCE
    else:
        DISTANCE[0] = dist(LOCATION['robot1'],Ballpoint)
        DISTANCE[1] = dist(LOCATION['robot2'],Ballpoint)
        if np.isnan(DISTANCE[0]) or np.isnan(DISTANCE[1]):  #有機器人跌倒
            print("FALL DOWN")
            continue  #等待機器人站起 #有NaN無法比大小           
        else:
            robot.id = DISTANCE.index(min(DISTANCE)) + 1
            robot.deg = deg[robot.id]
            robot.Robot_cpos = LOCATION[f'robot{robot.id}']
            determine()  #主攻者進攻
            sleep(0.5)
            robot.id = DISTANCE.index(max(DISTANCE)) + 1
            robot.deg = deg[robot.id]
            robot.Robot_cpos = LOCATION[f'robot{robot.id}']
            Targetpoint = ball.attack_track(Gate,robot.Robot_cpos)  #副攻跟隨主攻手
            determine()  #副攻者進攻
            sleep(0.5)
            if DISTANCE.index(min(DISTANCE)) == 0:
                EX_ATTACK[0] = LOCATION['robot1']
                EX_ATTACK[1] = '1'
            elif DISTANCE.index(min(DISTANCE)) == 1:
                EX_ATTACK[0] = LOCATION['robot2']
                EX_ATTACK[1] = '2'
            EX_DISTANCE = DISTANCE

    #顯示數值
    print("取得完成")
    print(A_Y)
    print(B_X)
    print(C_Y)
    print(D_X)
    print(R_BOTTOM)
    print(f"左下原點{initLoc}")
    print(f"球場中心點:{GroundCenter}")   
    print(f"右球門{Gate_R}")
    print(f"左球門{Gate_L}")
    print("-----開始判斷------")

    print("========迴圈結束======")
    sleep(2)








