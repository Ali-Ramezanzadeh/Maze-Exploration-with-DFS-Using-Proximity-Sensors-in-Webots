"""my_controller controller."""
def delay(ms):
    initTime = robot.getTime()      # Store starting time (in seconds)
    while robot.step(timestep) != -1:
        if (robot.getTime() - initTime) * 1000.0 > ms: # If time elapsed (converted into ms) is greater than value passed in
            break

from controller import Robot,DistanceSensor,Motor
import time
import numpy as np 
# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())
MAX_SPEED = 6.28

leftMotor = robot.getDevice('left wheel motor')
rightMotor = robot.getDevice('right wheel motor')

leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))




#daryaft sensor haye morede nazar
Ps_front_right = robot.getDevice('ps0')
Ps_front_right.enable(timestep)

Ps_front_left = robot.getDevice('ps7')
Ps_front_left.enable(timestep)

#Ps_right = robot.getDevice('ps2')
#Ps_right.enable(timestep)

#Ps_left = robot.getDevice('ps5')
#Ps_left.enable(timestep)

Ps_back_left = robot.getDevice('ps4')
Ps_back_left.enable(timestep)

Ps_back_right = robot.getDevice('ps3')
Ps_back_right.enable(timestep)

#variable haye baraye tain jahati ke mikhaym berim
f=0
b=0
r=0
l=0

#moteghayer haye komaki baraye map kardan
f2=0
b2=0
r2=0
l2=0


#shomarande ha baraye tain rahe rafte shode nesbat be jahate aval
F=0
L=0
B=0
R=0


#moteghayer haye komaki baraye map kardan
F2=0
L2=0
B2=0
R2=0


#variabe ha baraye taskhis jabejayi rafte shode
dx=0
dy=0
D = 1
i=0

#zaviye nesbat be jahate avaliye robot
deg=0
deg2=0
#zarib control konande tanasobi baraye calibration
k=0

#define map 
map=np.zeros((4 , 4))

#moshakhas kardane satro sotone matris baraye makane avaliye
#deghat shavad a1=0 yani robot roberoye akharin divar
#va a2=0 yani divar dar kenare chap tarin divar dar halate shoro
a1 = 0
a2 = 0

#[Front,Back,Right,Left]
List=[]

leftMotor.setVelocity(0)
rightMotor.setVelocity(0)
# Main loop:
# - perform simulation steps until Webots is stopping the controller
#shart i<60 baraye 2 bar map kardan baraye deghate balatar ast
#har bar ke map ra tey mikonad 30 bar be samt haye mokhtalef harekat mikonad
#baraye hamin sharte bargasht be noghteye aval i<30
#baraye 2 bar map kardan i<60
while robot.step(timestep) != -1 and i<30:   

    
    #check front wall
    
    leftMotor.setVelocity(0.5 * MAX_SPEED)
    rightMotor.setVelocity(0.5 * MAX_SPEED)
    delay(1600)
    
    psValue0=Ps_front_right.getValue()
    
    if psValue0>100:
        f=0
 
        psValue0=Ps_front_right.getValue()
        psValue2=Ps_front_left.getValue()
        while abs(psValue0 - psValue2)>1:
            psValue0=Ps_front_right.getValue()
            psValue2=Ps_front_left.getValue()
            #print(psValue0,psValue2)
        
            k = psValue0 - psValue2
            k = k/1000
            leftMotor.setVelocity(k * MAX_SPEED)
            rightMotor.setVelocity(-k * MAX_SPEED)
            delay(10)
    else:
        f=1

    #check back wall
        
    leftMotor.setVelocity(-0.5 * MAX_SPEED)
    rightMotor.setVelocity(-0.5 * MAX_SPEED)
    delay(2800)
    
    psValue1=Ps_back_left.getValue()
    
    if psValue1>100:
        b=0
        psValue3=Ps_back_right.getValue()
        psValue4=Ps_back_left.getValue()
        
        #calibration loop    
        while abs(psValue3 - psValue4)>1:
            psValue3=Ps_back_right.getValue()
            psValue4=Ps_back_left.getValue()
            #print(psValue3,psValue4)
        
            k = psValue3 - psValue4
            k = k/1000
            leftMotor.setVelocity(-k * MAX_SPEED)
            rightMotor.setVelocity(k * MAX_SPEED)
            delay(10)
    else:
        b=1
    #back to the center 
    
    leftMotor.setVelocity(0.5 * MAX_SPEED)
    rightMotor.setVelocity(0.5 * MAX_SPEED)
    delay(1500)
    
    
    # 90 degree
    
    
    leftMotor.setVelocity(0.5 * MAX_SPEED)
    rightMotor.setVelocity(-0.5 * MAX_SPEED)
    delay(750)
    
    #check right wall
    
    leftMotor.setVelocity(0.5 * MAX_SPEED)
    rightMotor.setVelocity(0.5 * MAX_SPEED)
    delay(1600)
    
    psValue0=Ps_front_right.getValue()
    
    if psValue0>100:
        r=0
        psValue0=Ps_front_right.getValue()
        psValue2=Ps_front_left.getValue()
        #calibration loop
        while abs(psValue0 - psValue2)>1:
            psValue0=Ps_front_right.getValue()
            psValue2=Ps_front_left.getValue()
            #print(psValue0,psValue2)
        
            k = psValue0 - psValue2
            k = k/1000
            leftMotor.setVelocity(k * MAX_SPEED)
            rightMotor.setVelocity(-k * MAX_SPEED)
            delay(10)
    else:
        r=1  
    #check left wall
    
    leftMotor.setVelocity(-0.5 * MAX_SPEED)
    rightMotor.setVelocity(-0.5 * MAX_SPEED)
    delay(3300)
    
    psValue1=Ps_back_left.getValue()
    
    if psValue1>80:
        l=0
        psValue3=Ps_back_right.getValue()
        psValue4=Ps_back_left.getValue()
       #calibration loop     
        while abs(psValue3 - psValue4)>1:
            psValue3=Ps_back_right.getValue()
            psValue4=Ps_back_left.getValue()
            #print(psValue3,psValue4)
        
            k = psValue3 - psValue4
            k = k/1000
            leftMotor.setVelocity(-k * MAX_SPEED)
            rightMotor.setVelocity(k * MAX_SPEED)
            delay(10)
    else:
        l=1   
    #back to the center 
    
    leftMotor.setVelocity(0.5 * MAX_SPEED)
    rightMotor.setVelocity(0.5 * MAX_SPEED)
    delay(1500)
    
    # 90 degree back to the first direction
    
    
    leftMotor.setVelocity(-0.5 * MAX_SPEED)
    rightMotor.setVelocity(0.5 * MAX_SPEED)
    delay(750)
    
    #Calibration loop for rotational and distance error

    if l == 0 and f == 0:
        leftMotor.setVelocity(0.5 * MAX_SPEED)
        rightMotor.setVelocity(0.5 * MAX_SPEED)
        delay(2000)
        
        leftMotor.setVelocity(-0.5 * MAX_SPEED)
        rightMotor.setVelocity(0.5 * MAX_SPEED)
        delay(750)
        
        leftMotor.setVelocity(0.5 * MAX_SPEED)
        rightMotor.setVelocity(0.5 * MAX_SPEED)
        delay(2000)
        
        psValue0=Ps_front_right.getValue()
        psValue2=Ps_front_left.getValue()
        while abs(psValue0 - psValue2)>1:
            psValue0=Ps_front_right.getValue()
            psValue2=Ps_front_left.getValue()
            #print(psValue0,psValue2)
        
            k = psValue0 - psValue2
            k = k/1000
            leftMotor.setVelocity(k * MAX_SPEED)
            rightMotor.setVelocity(-k * MAX_SPEED)
            delay(10)
                
                
        leftMotor.setVelocity(-0.5 * MAX_SPEED)
        rightMotor.setVelocity(0.5 * MAX_SPEED)
        delay(750)
            
            
        leftMotor.setVelocity(0.5 * MAX_SPEED)
        rightMotor.setVelocity(0.5 * MAX_SPEED)
        delay(1480)
        
        
        leftMotor.setVelocity(-0.5 * MAX_SPEED)
        rightMotor.setVelocity(0.5 * MAX_SPEED)
        delay(750)
        
        
        psValue3=Ps_back_right.getValue()
        psValue4=Ps_back_left.getValue()
            
        while abs(psValue3 - psValue4)>1:
            psValue3=Ps_back_right.getValue()
            psValue4=Ps_back_left.getValue()
            #print(psValue3,psValue4)
        
            k = psValue3 - psValue4
            k = k/1000
            leftMotor.setVelocity(-k * MAX_SPEED)
            rightMotor.setVelocity(k * MAX_SPEED)
            delay(10)
            
            
        
        leftMotor.setVelocity(0.5 * MAX_SPEED)
        rightMotor.setVelocity(0.5 * MAX_SPEED)
        delay(1480)
        
        leftMotor.setVelocity(-0.5 * MAX_SPEED)
        rightMotor.setVelocity(0.5 * MAX_SPEED)
        delay(750)
        
    
    
    F2=F
    L2=L
    B2=B
    R2=R    
    #commands for go to the next square
    #left_front_right_back    
        
    if l == 1:
        leftMotor.setVelocity(-0.5 * MAX_SPEED)
        rightMotor.setVelocity(0.5 * MAX_SPEED)
        delay(750)
        i = i+1
        leftMotor.setVelocity(0.5 * MAX_SPEED)
        rightMotor.setVelocity(0.5 * MAX_SPEED)
        delay(3700)
 
        #baraye tashkhis jahati ke rafte shode nesbat be jahate
        #avaliye robot va zakhire sazi jahat haye rafte shode
        
        if deg%360 == 0:
            L=L+1
        elif deg%360 == 90:
            F = F+1
        elif deg%360 == 180:
            R = R +1
        else:
            B = B +1
        #meghdar taghir dar jahate avaliye baad az raftan be khone baad
        
        deg= deg +270
        
        #append List be map asli

        
        
        
        
    elif f == 1:
     
        leftMotor.setVelocity(0.5 * MAX_SPEED)
        rightMotor.setVelocity(0.5 * MAX_SPEED)
        delay(3700)
        i = i+1
        if deg%360 == 0:
            F=F+1
        elif deg%360 == 90:
            R = R+1
        elif deg%360 == 180:
            B = B +1
        else:
            L = L +1

            
    elif r == 1:
     
        leftMotor.setVelocity(0.5 * MAX_SPEED)
        rightMotor.setVelocity(-0.5 * MAX_SPEED)
        delay(750)
        
        leftMotor.setVelocity(0.5 * MAX_SPEED)
        rightMotor.setVelocity(0.5 * MAX_SPEED)
        delay(3700)
        

        i = i+1
        
        
        if deg%360 == 0:
            R=R+1
        elif deg%360 == 90:
            B = B+1
        elif deg%360 == 180:
            L = L +1
        else:
            F = F +1
        
        deg = deg +90
        
    elif b == 1:
        leftMotor.setVelocity(0.5 * MAX_SPEED)
        rightMotor.setVelocity(-0.5 * MAX_SPEED)
        delay(1500)
        
        leftMotor.setVelocity(0.5 * MAX_SPEED)
        rightMotor.setVelocity(0.5 * MAX_SPEED)
        delay(3700)
       
      
        i = i+1
        if deg%360 == 0:
            B=B+1
        elif deg%360 == 90:
            L = L+1
        elif deg%360 == 180:
            F = F +1
        else:
            R = R +1
            
        deg = deg + 180
            
    #dastoor baraye taskhis divar ha nesbat be jahate avaliye        
    if deg2%360 == 0:   
            f2=f+1
            b2=b+1
            r2=r+1
            l2=l+1
            List=[f2,b2,r2,l2]
            
    elif deg2%360 == 90:    
            f2=l+1
            b2=r+1
            r2=f+1
            l2=b+1
            List=[f2,b2,r2,l2]
            
    elif deg2%360 == 180:
        
            f2=b+1
            b2=f+1
            r2=l+1
            l2=r+1
            List=[f2,b2,r2,l2]
            
    else:
            f2=r+1
            b2=l+1
            r2=b+1
            l2=f+1
            List=[f2,b2,r2,l2]
     
    deg2=deg
            
    #vared kardan moshkhasate bolook dar deraye morede nazar                 
    result = 0       
    result = ''.join(str(x) for x in List)  
    del List[:] 
    map[a1][a2]=result
    
    
    
    
   #baraye inke taskhis dade shavad ke be makan avakiye bargashte
   #mizane jabe jayi bayad sefr shavad
   #vaghti D=0 yani jabe jayi sefr shode 
   #va robot az loop kharej mishavad
   #dx = abs(L-R)  
   #dy = abs(B-F)
   #D = dx + dy
   #ama raveshe bala vaghti robot vasate maze bashe kafi nist
   
   
   
   
   #code baraye taskhis deraye kononi robot pas az anjame harekat
    if F-F2 == 1:
        a1 = a1 -1
    elif B-B2 == 1:
        a1 = a1+1
    elif L-L2 == 1:
        a2 = a2 -1
    else:
        a2 = a2 + 1
        
    
    #print(L,R,B,F)
    pass
    
leftMotor.setVelocity(0 * MAX_SPEED)
rightMotor.setVelocity(0 * MAX_SPEED) 



#code baraye keshidane shematic naghshe 
s=' ' 
row=[]

print(map)
for h in range(4):
    if h==0 or h==2:
        for o in range(4):
            s=str(int(map[h][o]))
            if int(s[0]) == 1:
                row.append('* * * * ')
            else:
                if o == 0:
                    if int(s[2]) ==1 and int(s[3])==1:
                        row.append('*     * ')
                    elif int(s[3])==1:
                        row.append('*       ')
                else:
                    if int(s[2]) == 1:
                        row.append('      * ')
                    else:
                        row.append('        ')
                
                
                
        print("".join(row))
        row.clear()
      
    for o in range(4):
        s=str(int(map[h][o]))
        if o == 0:
            if int(s[2]) ==1 and int(s[3])==1:
                row.append('*     * ')
            elif int(s[3])==1:
                row.append('*       ')
        else:
            if int(s[2]) == 1:
                row.append('      * ')
            else:
                row.append('        ')
                
    print("".join(row))
    row.clear()
    
    
    for o in range(4):
        s=str(int(map[h][o]))
        if o == 0:
            if int(s[2]) ==1 and int(s[3])==1:
                row.append('*     * ')
            elif int(s[3])==1:
                row.append('*       ')
        else:
            if int(s[2]) == 1:
                row.append('      * ')
            else:
                row.append('        ')
                
    print("".join(row))
    row.clear()
    
    
    
    if h==0 or h==2 or h==3:    
        for o in range(4):
       
            s=str(int(map[h][o]))
            if int(s[1]) == 1:
                row.append('* * * * ')
            else:
                if o == 0:
                    if int(s[2]) ==1 and int(s[3])==1:
                        row.append('*     * ')
                    elif int(s[3])==1:
                        row.append('*       ')
                else:
                    if int(s[2]) == 1:
                        row.append('      * ')
                    else:
                        row.append('        ')
        print("".join(row))
        row.clear()

        
                
        