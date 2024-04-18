
# // int -> random int
# // boolean -> random boolean
# // make -> o valoare din fisierul de tip text (array) make.txt  
# // nested -> o valoare din fisierul de tip json (array) numit nested_[make]_[model].json 
# // ... 
import json 
import random


def readInput(nrObiecteGenerate):
    obiecteGenerate=[]
    for i in range(nrObiecteGenerate):
        obiecteGenerate.append({})
    with open("input.json","r") as file:
        continut=json.load(file)
    continut=continut[0]
    for cheie in continut:
        spargere=continut[cheie].split(',')
        if(spargere[0]=='int'):
            for i in range(nrObiecteGenerate):
                obiecteGenerate[i][cheie]=random.randint(int(spargere[1]),int(spargere[2]))
        elif(spargere[0]=='boolean'):
            for i in range(nrObiecteGenerate):
                obiecteGenerate[i][cheie]=random.choice([True,False])
        elif(spargere[0]=='nested'):
            with open(spargere[2]+".json","r") as file:
                continutNested=json.load(file)
            for i in range(nrObiecteGenerate):
                flag=False
                for obiect in continutNested:
                    if(obiect[spargere[1]]==obiecteGenerate[i][spargere[1]]):
                        obiecteGenerate[i][spargere[2]]=random.choice(obiect["detail"])
                        flag=True
                        break
                if not flag:
                    obiecteGenerate[i][spargere[2]]='undefined'
                #print(obiecteGenerate[i])
        elif(spargere[0]=='array'):
            #metoda 1
            elemente=spargere[1:]
            #metoda 2
            # elemente=[]
            # for index in range(1,len(spargere),1):
            #     elemente.append(spargere[index])
            for i in range(nrObiecteGenerate):
                obiecteGenerate[i][cheie]=random.choice(elemente)

            # print(spargere)
        else:
            valoare=spargere[0]
            with open(valoare+".txt","r") as file:
                valori=file.read().split(',')
            for i in range(nrObiecteGenerate):
                obiecteGenerate[i][cheie]=random.choice(valori).strip("'")  
        print(obiecteGenerate)  
readInput(40)