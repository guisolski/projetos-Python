import os
import msvcrt
import time
import sys

def getKey():
    return str(msvcrt.getch()).replace("b","").replace("'","")
def clear():
    os.system('cls' if os.name=='nt' else 'clear')
def drawCube(a):
    print("[]") if a else print("[]",end="")
def drawFloor(n, jump):
    print("_"*n) if not jump else print(' ','_'*n)
def drawBullet(bullet):
    if bullet == 0:
        return 10
    print(' '*bullet,'.')
    return bullet
def gameDynamic(bullet, jump,points):
    if bullet == 0 and not jump:
         print("Morreu")
         sys.exit()
         return points
    elif bullet == 0 and jump:
        return points +1
    return points
floor,bullet,points = 10,10,0

while True:
    jump = False
    if msvcrt.kbhit():
           key = getKey()
           print(key)
           if key == ' ':
                jump = True
    clear()
    points = gameDynamic(bullet,jump,points)
    bullet = drawBullet(bullet)
    drawCube(jump)
    drawFloor(floor, jump)
    print(points)
    time.sleep(0.3)
    bullet -= 1
