import keyboard
import time
import os 
import random



def generate_empty_array():
    array = []
    for i in range(50):
        i = ' '
        array.append(i)
    return array

array = generate_empty_array()
array[25] = 'x'

def add_fruit():
    posX = array.index('x')
    pos0 = random.randint(0,49)
    while pos0 == posX:
        pos0 = random.randint(0,49)   
    array[pos0] = '0'

scor = 0
pos = 0
start_time = time.time()

def display():
    print(f'Score:{scor} Time:{int(time.time() - start_time)}')
    print(''.join(array))

add_fruit()

while True:
    
    if keyboard.is_pressed('left'):
        os.system('cls')
        pos = array.index('x')
        if pos>0:
            if array[pos-1] =='0':
                scor +=1
                add_fruit()
            array[pos-1] = 'x'
            array[pos] = ' '
        display()
        time.sleep(0.1)
    if keyboard.is_pressed('right'):
        os.system('cls')
        pos = array.index('x')
        if pos < len(array)-1:
            if array[pos+1] =='0':
                scor +=1
                add_fruit()
            array[pos+1] = 'x'
            array[pos] = ' '
        display()
        time.sleep(0.1)
    # if keyboard.is_pressed('down'):
    #     os.system('cls')
    #     print(array)
    #     time.sleep(0.1)
    # if keyboard.is_pressed('up'):
    #     os.system('cls')
    #     print(array)
    #     time.sleep(0.1)
    if keyboard.is_pressed('x'):
        break
