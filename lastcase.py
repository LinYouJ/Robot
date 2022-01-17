import numpy as np
import math
from object.ball import Ball
from object.robot import Robot
from object.robot import Enemy

robot=Robot()
ball=Ball()
enemy=Enemy()
Gate=np.array([0,-170]) 
top_left=np.array([-90,170])  #客場球門左右角落
top_right=np.array([90,170])

def aim_Gate(): 
        #正踢
        ##更新座標##
        print("更新座標點")
        # robot.Robot_cpos[0],robot.Robot_cpos[1]=input("input robot center coordinate:").split()
        # robot.Robot_fpos[0],robot.Robot_fpos[1]=input("input robot front coordinate:").split()
        # ball.ball_pos[0],ball.ball_pos[1]=input("input ball coordinate:").split()
        # enemy.enemy_pos[0],enemy.enemy_pos[1]=input("input enemy coordinate:").split()
        ##
        Robotcenter=robot.getCenter() 
        Robotfront=robot.getFront()
        Ballpoint=ball.ballPos()
        if(Gate[1]*-1) >=0:   #座標固定時，進攻方向改變
            Robotcenter*=-1
            Robotfront*=-1
            Ballpoint*=-1
        ctr2ball=math.hypot(Ballpoint[0]-Robotcenter[0],Ballpoint[1]-Robotcenter[1])
        RB_deg=math.degrees(math.atan2(Ballpoint[1]-Robotcenter[1],Ballpoint[0]-Robotcenter[0]))
        if(RB_deg<0):
            RB_deg+=360
        Robotdeg=math.degrees(math.atan2(Robotfront[1]-Robotcenter[1],Robotfront[0]-Robotcenter[0])) 
        if(Robotdeg<0):
            Robotdeg+=360
        RBdiff=Robotdeg-RB_deg
        print("座標差:%d"%RBdiff)
        if(RBdiff<15 and RBdiff>-15):
            result=robot.move(ctr2ball)
            if(result==1):
                robot.kickball(Robotcenter,Gate,Ballpoint,ctr2ball)
            else:
                aim_Gate()
        elif(RBdiff>0 and RBdiff<=180):
            robot.turnTO("right")
            aim_Gate()
        else:
            robot.turnTO("left")
            aim_Gate()
            
def aim_Target(rotate):
    if(rotate=="right"): #右轉限定
        if(diff_cos<0.9 and diff_cos>-1):
            robot.turnTO('right')
        else:
            result=robot.move(ctr2Tar)
            scout=scouting()
            if(result==1 or result==2):
                if(result==1 and scout=='safe'):
                    aim_Gate()
                elif(scout=='danger'):
                    print("路線不通")
                    return 1 #更改目標點
                else:
                    print("繼續通行")

    elif(rotate=="left"): #左轉限定 
        if(diff_cos<0.9 and diff_cos>-1):
            robot.turnTO("left")
        else:
            result=robot.move(ctr2Tar)
            scout=scouting()
            if(result==1 or result==2):
                if(result==1 and scout=='safe'):
                    aim_Gate()
                elif(scout=='danger'):
                    print("路線不通")
                    return 1  #更改目標點
                else:
                    print("繼續通行")
            
def scouting():
    global Ballpoint
    enemypoint=enemy.coordinate()
    GE_VEC=np.array([enemypoint[0]-Gate[0],enemypoint[1]-Gate[1]])
    GE_VEC_LEN=math.hypot(GE_VEC[0],GE_VEC[1])
    GB_VEC=np.array([Ballpoint[0]-Gate[0],Ballpoint[1]-Gate[1]])
    GB_VEC_LEN=math.hypot(GB_VEC[0],GB_VEC[1])
    GB_dot_GE=((GB_VEC[0]*GE_VEC[0])+(GB_VEC[1]*GE_VEC[1]))
    ORTH_VEC_LEN=(GB_dot_GE/GB_VEC_LEN) #正射影長
    GBE_theta=math.acos(GB_dot_GE/(GE_VEC_LEN*GB_VEC_LEN))
    if(ORTH_VEC_LEN<=GB_VEC_LEN and GE_VEC_LEN*math.sin(GBE_theta)<=8):  #敵人至踢球路徑的距離
        return 'danger'
    else:
        return 'safe'

decide=0   
while True: 
    #測試
    # start=str(input("輸入任意Y 或 y開始動作:"))
    # if(start!='Y' and start!='y'):
    #     break
    # robot.Robot_cpos[0],robot.Robot_cpos[1]=input("input robot center coordinate:").split()
    # robot.Robot_fpos[0],robot.Robot_fpos[1]=input("input robot front coordinate:").split()
    # ball.ball_pos[0],ball.ball_pos[1]=input("input ball coordinate:").split()
    # enemy.enemy_pos[0],enemy.enemy_pos[1]=input("input enemy coordinate:").split()

    #主程式
    Robotcenter=robot.getCenter()
    Robotfront=robot.getFront()
    Ballpoint=ball.ballPos()
    Targetpoint=ball.targetPos(Gatepoint=Gate)
    enemypoint=enemy.coordinate()

    if(Gate[1]*-1) >=0:   #座標固定時，進攻方向改變
        Robotcenter*=-1
        Robotfront*=-1
        Ballpoint*=-1
        Targetpoint*=-1
        enemypoint*=-1
        top_left*=-1
        top_right*=-1

    if(decide==1): #更改目標點
        print("更改目標點") #以邊界角為目標點
        LEFT_LEN=math.hypot(top_left[0]-Robotcenter[0],top_left[1]-Robotcenter[1])
        RIGHT_LEN=math.hypot(top_right[0]-Robotcenter[0],top_right[1]-Robotcenter[1])
        if(LEFT_LEN<RIGHT_LEN):
            Targetpoint=top_left
        else:
            Targetpoint=top_right

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
    #print(Targetpoint)

    #運算區
    print("目標點位置[%.2f,%.2f]"%(RT_deg,ctr2Tar)) 
    if(RT_deg==90):
        print("目標在正向y軸")
        if(RTdiff>10 and RTdiff<=180):
            decide=aim_Target("right")   
        else:
            decide=aim_Target("left")
    elif(RT_deg>=0 and RT_deg<90):
        print("目標在第一象限")
        if(RTdiff>=0 and RTdiff<180):
            decide=aim_Target("right")
        else:
            decide=aim_Target("left")      
    elif(RT_deg>90 and RT_deg<=180):
        print("目標在第二象限")
        if(RTdiff>=0 and RTdiff<180):
            decide=aim_Target("right")
        else:
            decide=aim_Target("left") 
    elif(RT_deg>180 and RT_deg<=270):
        print("目標在第三象限")
        if(abs(RTdiff)>=0 and abs(RTdiff)<180):
            decide=aim_Target("left")
        else:
            decide=aim_Target("right")
    elif(RT_deg>270 and RT_deg<359):
        print("目標在第四象限")
        if(abs(RTdiff)>=0 and abs(RTdiff)<180):
            decide=aim_Target("left")
        else:
            decide=aim_Target("right")  
    
    #decide重置
    decide=0
    print("=================")

