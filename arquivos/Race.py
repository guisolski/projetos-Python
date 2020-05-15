  
import os
import msvcrt
import time
from random import randint


def getKey():
    return str(msvcrt.getch()).replace("b","").replace("'","")
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def track_draw(track):
    for line in track:
        for value in line:
            print(value,end="")
        print("")
def move_car(track,car,pos_old):
    for pos in car:
        track[pos[0]][pos_old] = "_____"
    for index in range(len(car)):
        pos = car[index]
        if index == 0:
            track[pos[0]][pos[1]] = " _   "
        elif index == 1:
            track[pos[0]][pos[1]] = "| |  "
        elif index == 2:
            track[pos[0]][pos[1]] = " -   "
    return track

def change_pos(car,value):
    for index in range(len(car)):
        car[index][1] = value
    return car
    
def move(key, pos,list_of_pos):
    if key == 'a':
        pos = pos -1 if pos-1>0 else 0
    elif key =='d':
        pos = pos + 1 if pos+1 < len(list_of_pos) else pos
    return pos

def creted_enemy(pos_of_tracks,list_of_enemys):
    x = pos_of_tracks[randint(0,2)]
    for car in list_of_enemys:
        for part in car:
            if x == part[1]:
                return creted_enemy(pos_of_tracks,list_of_enemys)
    return [[0,x],[1,x],[2,x]]

def generet_enemys(list_of_enemys,min_max_enemy,pos_of_tracks):
    length = len(list_of_enemys)    
    if length >= min_max_enemy["min"] and length < min_max_enemy["max"]:
        list_of_enemys.append(creted_enemy(pos_of_tracks,list_of_enemys))
    return list_of_enemys

def move_enemy(list_of_enemys):
    for car in list_of_enemys:
        for parts in car:
            parts[0] += 1
    return list_of_enemys
def collision(list_of_enemys, car):
    for i in list_of_enemys:
        if i[2][0] == car[0][0] and i[2][1] == car[0][1] :
            return True
    return False        
def remove_enemy(list_of_enemys,points):
    for i in range(len(list_of_enemys)):
        if list_of_enemys[i][2][0] == 12:
            list_of_enemys.pop(i)
            return list_of_enemys, points+1
    return list_of_enemys,points
def draw_enmeys(list_of_enemys, track, clean):
    for car in list_of_enemys:
        front,midle,back = car[0],car[1],car[2]
        if clean == False:            
            track[front[0]][front[1]] = " _   "
            track[midle[0]][midle[1]] = "| |  "
            track[back[0]][back[1]]   = " -   "
        else:
            track[front[0]][front[1]] = "_____"
            track[midle[0]][midle[1]] = "_____"
            track[back[0]][back[1]]   = "_____"
    return track
track= [['||','_____','|','_____','|','_____','||'],
        ['||','_____','|','_____','|','_____','||'],
        ['||','_____','|','_____','|','_____','||'],
        ['||','_____','|','_____','|','_____','||'],
        ['||','_____','|','_____','|','_____','||'],
        ['||','_____','|','_____','|','_____','||'],
        ['||','_____','|','_____','|','_____','||'],
        ['||','_____','|','_____','|','_____','||'],
        ['||','_____','|','_____','|','_____','||'],
        ['||','_____','|','_____','|','_____','||'],
        ['||',' _   ','|','_____','|','_____','||'], 
        ['||','| |  ','|','_____','|','_____','||'], 
        ['||',' -   ','|','_____','|','_____','||']]

car = [[10,1],[11,1],[12,1]]

Loop = True
pos_of_tracks = [1,3,5]
pos = 0
min_max_enemy = {"min":0,"max":2}
list_of_enemys = []
points = 0


while Loop:
    if msvcrt.kbhit():
           key = getKey()
           pos_old = pos_of_tracks[pos]
           pos = move(key,pos, pos_of_tracks)
           change_pos(car,pos_of_tracks[pos])
           track = move_car(track,car,pos_old)

    clear()
    draw_enmeys(list_of_enemys, track, True)
    generet_enemys(list_of_enemys,min_max_enemy,pos_of_tracks)
    list_of_enemys,points = remove_enemy(list_of_enemys,points)
    list_of_enemys = move_enemy(list_of_enemys)
    colisson = collision(list_of_enemys, car)
    if colisson == True:
        clear()
        print("loser")
        break 
    draw_enmeys(list_of_enemys, track, False)
    
    track_draw(track)
    print("Points:", points)
    time.sleep(0.2)
