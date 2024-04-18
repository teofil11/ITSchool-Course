import keyboard
import time
import os 
import random

pos=0
def generate_empty_array():
    array=[]
    for i in range(50):
        i=" "
        array.append(i)
    return(array)

matrice=[]
for i in range(30):
    matrice.append(generate_empty_array())

posX=15
posY=25
matrice[posX][posY]='x'
startTime=time.time()

def add_fruit():
    pos0X = random.randint(0,29)
    pos0Y = random.randint(0,49)
    while matrice[posX][posY] == matrice[pos0X][pos0Y]:
        pos0X = random.randint(0,29)
        pos0Y = random.randint(0,49)
    matrice[pos0X][pos0Y] = '0'

score = 0
def display():
    print(f"Score: {score} Time:{int(time.time()-startTime)}")
    for row in matrice:
        print("".join(row))
    

def moveLeft():
    global posY
    if posY >0:
        matrice[posX][posY]=' '
        matrice[posX][posY-1]='x'
        posY=posY-1

def moveRight():
    global posY
    if posY < 49:
        matrice[posX][posY]=' '
        matrice[posX][posY+1]='x'
        posY=posY+1

def moveUp():
    global posX
    if posX > 0:
        matrice[posX][posY]=' '
        matrice[posX-1][posY]='x'
        posX=posX-1
def moveDown():
    global posX
    if posX < 29:
        matrice[posX][posY]=' '
        matrice[posX+1][posY]='x'
        posX=posX+1

add_fruit()

while True:
        if keyboard.is_pressed('left'):
            os.system('cls')
            if matrice[posX][posY-1] == '0':
                score +=1
                add_fruit()
            moveLeft()
            display()
            time.sleep(0.1)
        if keyboard.is_pressed('right'):
            os.system('cls')
            if posY != 49:
                if matrice[posX][posY+1] == '0':
                    score +=1
                    add_fruit()
            moveRight()
            display()
            time.sleep(0.1)
        if keyboard.is_pressed('down'):
            os.system('cls')
            if posX != 29:
                if matrice[posX+1][posY] == '0':
                    score +=1
                    add_fruit()
            moveDown()
            display()
            time.sleep(0.1)
        if keyboard.is_pressed('up'):
            os.system('cls')
            if matrice[posX-1][posY] == '0':
                score +=1
                add_fruit()
            moveUp()
            display()
            time.sleep(0.1)
        if keyboard.is_pressed('x'):
            break

