import time
import datetime

flag = 0
while True:
    if datetime.datetime.now().hour == 21:
        if flag == 0:
            print('e ora 19')
            flag += 1
        else:
            flag = 0
    time.sleep(1)


