import requests
import mysql.connector
import random
import datetime
import time
import csv
import os
import colorlog
import logging


def test1(id_manager,URL,cale,nume_tabel):
    users = [['Mihai','Badea','Itschool', id_manager.upper(), 'gmail'],
             ['Paul','Muntean','Itschool', id_manager.upper(), 'gmail'],
             ['Leo','Olteanu','Itschool', id_manager.upper(), 'gmail'],
             ['Natalia','Angiu','Google', id_manager.upper(), 'gmail']]

    for user in users:
        jsonData = {
            'prenume':user[0],
            'nume':user[1],              
            'companie':user[2],
            'idManager':user[3],
            'email':user[4],
        }

        r = requests.post(URL+cale,json = jsonData)
    
    
    connect = mysql.connector.connect(host = 'localhost', user = 'root', password = 'root', database = 'project')
    cursor =  connect.cursor()  

    cursor.execute(f"SELECT * FROM {nume_tabel}")
    results=cursor.fetchall()

    for row in users:
        found=False
        contor=0
        while not found and contor<len(results):
            flag=True
            for i in range(len(row)):
                if row[i]!=results[contor][i+1]:
                    flag=False
            if flag==True:
                found=True
            else:
                contor+=1
        return found

# print(test1('ceo','http://127.0.0.1:5000/','signup','employees'))


def test2(cale,tip):
    persoane=[]
    linii=[{
        'idPersoana': 'idPersoana',
        'data': 'data',
        'sens': 'sens'
    }]

    for i in range(50):

        alegere=random.randint(0,1)
        output={
                "data":datetime.datetime.now(datetime.timezone.utc).isoformat().replace("+00:00", "Z"),
                "idPoarta":random.randint(1,3)

            }
        aIntrat=False
        if(alegere==1):
            #intrare
            idPersoana=random.randint(1,30)
            while(idPersoana in persoane):
                idPersoana=random.randint(1,30)
            output["sens"]="in"
            output["idPersoana"]=idPersoana
            persoane.append(output['idPersoana'])
            aIntrat=True
        else:
            #iesire 
            if(len(persoane)>0):
                idPersoana=persoane[random.randint(0,len(persoane)-1)]
                output["sens"]="out"
                output["idPersoana"]=idPersoana
                persoane.remove(idPersoana)
                aIntrat=True
        if(aIntrat):
            linii.append(output)

    if tip == 'csv':
        with open(cale,"w",newline='') as file:
            writer=csv.writer(file)
            for linie in linii:
                array=[str(linie['idPersoana']),linie['data'],linie['sens']]
                writer.writerow(array) 
              
    else:
        with open(cale,"w") as file:
            for linie in linii:
                file.write(f"{linie['idPersoana']},{linie['data']},{linie['sens']};\n")
    
    with open(cale,'r') as file:
        if tip =='csv':
            continut = csv.reader(file)
            for i in range(len(linii)):
                for row in continut:
                    if row[0] == linii[i]['idPersoana'] and row[1] == linii[i]['data'] and row[2] == linii[i]['sens']:
                        return True

        else:
            id_persoana = False
            data = False
            sens = False
            continut = file.readlines()
            for i in range(len(continut)):
                if str(linii[i]['idPersoana']) == str(continut[i].strip(';\n').split(',')[0]):
                    id_persoana = True
                else:
                    return False
                    
                if linii[i]['data'] == continut[i].strip(';\n').split(',')[1]:
                    data = True
                else:
                    return False
                
                if linii[i]['sens'] == continut[i].strip(';\n').split(',')[2]:
                    sens = True
                else:
                    return False
                    
            
            if id_persoana and data and sens:
                return True     


# print(test2('Project/inputs/Poarta1.txt','txt'))


def test3(fisier_input):
    fisiere = os.listdir('Project/inputs')
    fisiere_backup = os.listdir('Project/backup_inputs')
    ext = fisier_input.split('.')[1]
    file_name = fisier_input.split('.')[0]
    for fisier in fisiere:
        if fisier == fisier_input:
            return False
    for element in fisiere_backup:
        if element == file_name+'('+str(datetime.datetime.now().date())+').'+ext:
            return True
    return False

# print(test3('Poarta1.txt'))


def test4(path):
    flag = True
    for fisier in os.listdir(path):
        created_time = os.path.getctime(path+fisier)
        curent_time = time.time()
        if created_time <= curent_time-5:
            flag = False
            return flag
        else:
            return True
    return flag

# print(test4('Project/inputs/'))

log_format = (
    '%(log_color)s%(levelname)s%(reset)s '
    '%(log_color)s%(asctime)s%(reset)s '
    '%(log_color)s%(message)s%(reset)s'
)

logger = colorlog.getLogger()
logger.setLevel(logging.DEBUG)  # Set the desired log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(colorlog.ColoredFormatter(log_format))
logger.addHandler(stream_handler)

def check():
    punctaj = 0
    if test1('ceo','http://127.0.0.1:5000/','signup','employees'):
        punctaj += 2.5
        logging.info('Test 1 passed')
    if test2('Project/inputs/Poarta2.csv','csv'):
        punctaj += 2.5
        logging.info('Test 2 passed')
    time.sleep(3)
    if test3('Poarta2.csv'):
        punctaj += 2.5
        logging.info('Test 3 passed')
    if test4('Project/inputs/'):
        punctaj += 2.5
        logging.info('Test 4 passed')
    if punctaj <= 5:
        logging.error(f'Punctajul este {punctaj}')
    if punctaj > 5 and punctaj <= 7.5:
        logging.warning(f'Punctajul este {punctaj}')
    if punctaj > 7.5:
        logging.info(f'Punctajul este {punctaj}')

check()
