import os
import sys

def clear():
    os.system('cls' if os.name=='nt' else 'clear')
def Draw_map(m):
    clear()
    line = 0
    for i in m:
        line +=1
        col = 0
        for j in i:
            col += 1
            if j == None:
                print("_" if line < 3 else " ",end="")
            else:
                print(j,end="")
            if col < 3:
                print("|",end="")
        print("")
def CheckVictory(m, x, y):
    if x == None and y == None :
        return False 
    if m[0][y] == m[1][y] == m [2][y]:
        return True
    elif m[x][0] == m[x][1] == m [x][2]:
        return True
    elif x == y and m[0][0] == m[1][1] == m [2][2]:
        return True
    elif x + y == 2 and m[0][2] == m[1][1] == m [2][0]:
        return True
    return False    
def CheckDraw(m):
    k = 0
    for i in m:
        if None not in i:
            k += 1 
    return k >= 3
def Check(m,line,col):
    return CheckDraw(m) == False and CheckVictory(m,line,col) == False
def stop():
    clear()
    print("Input error")
    sys.exit()

Matrix_map,values,value,line,col = [[None,None,None],[None,None,None],[None,None,None]],['X','O'],0,None,None

Draw_map(Matrix_map)

while Check(Matrix_map,line,col):
    try:
        line = int(input("Line: ").strip())
        col  = int(input("Col: ").strip())    
    except:
        stop()
    Matrix_map[line][col],value = (values[value] if Matrix_map[line][col] == None else Matrix_map[line][col]), (1 if value == 0 else  0 )

    Draw_map(Matrix_map)

print("Draw") if CheckDraw(Matrix_map) else print("Win ",values[1 if value == 0 else  0 ])
