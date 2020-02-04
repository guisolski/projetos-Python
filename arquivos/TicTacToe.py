import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def Draw_map(m):
    cls()
    line = 0
    for i in m:
        line +=1
        col = 0
        for j in i:
            col += 1
            if j == None and line < 3:
                print("",end="_")
            elif j == None and line >= 3:
                print("",end=" ")
            else:
                print(j,end="")
            if col < 3:
                print("|",end="")
        print("")

def CheckVictory(board, x, y):
    if board[0][y] == board[1][y] == board [2][y]:
        return True
    elif board[x][0] == board[x][1] == board [x][2]:
        return True
    elif x == y and board[0][0] == board[1][1] == board [2][2]:
        return True
    elif x + y == 2 and board[0][2] == board[1][1] == board [2][0]:
        return True
    return False    
def CheckDraw(m):
    k = 0
    for i in m:
        if None not in i:
            k += 1 
    return k >= 3
    
Matrix_map = [
    [None,None,None],
    [None,None,None],
    [None,None,None]
    ]
values = ['X','O']
value = 0
Draw_map(Matrix_map)
while True:
    line = int(input("Line: ").strip())
    col  = int(input("Col: ").strip())    
    Matrix_map[line][col] = (values[value] if Matrix_map[line][col] == None else Matrix_map[line][col])
    Draw_map(Matrix_map)
    if CheckVictory(Matrix_map,line,col):
        print("Win ",values[value])
        break
    if CheckDraw(Matrix_map):
        print("Draw")
        break
    value = (1 if value == 0 else  0 )
