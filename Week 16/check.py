import time
import random
import time
import datetime

months = [31,28,31,30,31,30,31,31,30,31,30,31]

def create_json(data, sens, idPersoana, idPoarta):
    dictionar = {
        'data': data,
        'sens': sens,
        'idPersoana': idPersoana,
        'idPoarta': idPoarta
    }
    return dictionar

def pedding(value):
    if value < 10:
        value = '0' + str(value)
    return value

def megaPedding(value,lungimepedding):
    cifrenecesare = lungimepedding - len(str(value))
    for i in range(cifrenecesare):
        value = '0' + str(value)
    return value

def generate_random_date():
    year = random.randint(2022,2023)
    month = random.randint(1,12)
    day = random.randint(1,months[month - 1])
    month = pedding(month)
    day = pedding(day)
    hour = random.randint(1,24)
    hour = pedding(hour)
    minute = random.randint(0,59)
    minute = pedding(minute)
    seconds = random.randint(0,59)
    seconds = pedding(seconds)
    millis = random.randint(0,900)    
    data = f'{year}-{month}-{day}T{hour}:{minute}:{seconds}.{millis}Z'
    return data

def generate_random_sense():
    sensuri = ['in','out']
    return sensuri[random.randint(0,1)]

def generate_random_person():
    return random.randint(1,100)

def generate_random_poarta():
    return random.randint(1,2)

while True:
    random_date = generate_random_date()
    random_sens = generate_random_sense()
    random_person = generate_random_person()
    random_poarta = generate_random_poarta()
    print(create_json(random_date,random_sens,random_person,random_poarta))

    time.sleep(3)


