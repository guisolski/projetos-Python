import os
import msvcrt
import time
import sys

def getKey():
    return str(msvcrt.getch()).replace("b","").replace("'","").replace("\n"," ").replace(" ","").strip()
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def draw(x,y,n):
    clear()
    for i in range(n):
        print("_"*x+"."+"_"*(n-x-1)) if y == i else print("_"*n)
    

x,y,n = 0,0,5
draw(x,y,n)

while True:
    if msvcrt.kbhit():
        key = getKey()
        if key == 'a':
            x = x-1 if x >= 1 else x
        elif key == 'd':
            x = x+1 if x <= n-2 else x
        elif key == 'w':
            y = y-1 if y >= 1 else y
        elif key == 's':
            y = y+1 if y <= n-2 else y
    draw(x,y,n)
    time.sleep(0.2)
