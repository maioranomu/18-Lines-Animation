import os,time,random
def clear(): time.sleep(0.1); os.system("cls")
truck1,truck2,truck3,b1,b2,b3,counter,s1,s2,s3,s4,sky1,sky2,sky3,sky4,c11,c12,c13,c14,c21,c22,c23,c24 = ("   ________________","  | ##### TRUCK  |o\\","  |_________________|","_"*2,"_"*11,"_"*100," ","(|)","(/)","(-)","(\\)"," "*20," "*20," "*20," "*20,"    ___  ___  "," __/   \\/   \\ ","/            \\","\\____________/","  ___  _____  "," /   \\/     \\ ","/            \\","\\____________/");sprites = [f"{b1}{s}{b2}{s}{b3}" for s in (s1, s2, s3, s4)]
while 1:
    for s in sprites:
        clear(); counter += "_"
        if len(counter) % 10 == 0:
            cl, bc = random.randint(0, 2), random.randint(10, 14)
            sky1, sky2, sky3, sky4 = (sky1+c11+" "*bc, sky2+c12+" "*bc, sky3+c13+" "*bc, sky4+c14+" "*bc) if cl==1 else ((sky1+c21+" "*bc, sky2+c22+" "*bc, sky3+c23+" "*bc, sky4+c24+" "*bc) if cl==2 else (sky1,sky2,sky3,sky4))
        truck1, truck2, truck3, s = " "+truck1, " "+truck2, " "+truck3, counter+s;print("\n".join([sky1, sky2, sky3, sky4, truck1, truck2, truck3, s]))
