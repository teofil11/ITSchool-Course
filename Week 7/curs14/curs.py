lista=[1,2,5,8,9]
import time
import os
import json
#la fiecare pas utilizatorului i se va cere sa introduca un caracter 
#daca este litera, il ignora 
#daca este cifra, il adauga in lista 
#functia trebuie a afiseze pe ecran un mesaj atunci cand se introduce un numar in lista 
def verificaElementeNoi():
    nrElemente=len(lista)
    while True:
        element=input("Introduceti un caracter: ")
        if element.isalpha():
            print("Se pot introduce doar cifre")
            continue
        else:
            lista.append(element)
            print(lista)
        if(len(lista)==nrElemente):
            print("Nu avem element nou")
        else:
            print("Avem un element nou")
        

##afisati toate numerele care se gasesc in sirul A dar nu si in sirul B 
A=[2,3,4,5,6,10,7]
B=[2,3,4,5,9,10,1]

def AminusB():
    for a in A:
        suntDiferite=True
        for b in B:
            if a==b:
                suntDiferite=False
        if(suntDiferite):
            print(a)
            
def AminusPaulB():
    for a in A:
        if not a in B: 
            print(a)

def eJson(filePath):
    "info.txt"
    "info.json"
    extensie=filePath.split(".")[1]
    if(extensie=="json"):
        return True
    else:
        return False

def citesteJSON(filePath):
    with open(filePath,"r") as file:
        jsonValue=file.read()
        jsonFormat=json.loads(jsonValue)
        print(jsonFormat[2]["note"][2]["optionale"]["matematiciSpeciale"])

def verificaFisiereNoi():
    fisiereVechi=[]
    while True:
        fisiere=os.listdir("Week 7/curs14/monitorizat")
        if(len(fisiereVechi)==len(fisiere)):
            print("Nu avem fisiere noi")
        else:
            for fisierNou in fisiere:
                if not fisierNou in fisiereVechi: 
                    print(fisierNou)
                    if eJson(fisierNou)==True:
                            citesteJSON("Week 7/curs14/monitorizat/"+fisierNou)
                    else:
                        with open("Week 7/curs14/monitorizat/"+fisierNou,"r") as file:
                            print(file.read())
                        
        fisiereVechi=fisiere   
        time.sleep(5)


    



verificaFisiereNoi()
# os.getcwd()

jsonArray=[{
                "contSursa":"RO12312",
                "contDestinatie":"RO12312",
                "suma":15
            },
            {
                "contSursa":"RO12312",
                "contDestinatie":"RO12312",
                "suma":15
            },
            {
                "contSursa":"RO12312",
                "contDestinatie":"RO12312",
                "suma":15
            }
        ]
jsonString=json.dumps(jsonArray)
# with open('Week 7/curs14/tranzactii.json', 'w') as file:
#     file.write(jsonString)