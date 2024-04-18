import os
import time
import json
def inmultire(deinmultit:int,inmultitor)->int:
    '''Aceasta este o functie de inmultire
    :param int deinmultit:
    :param int inmultitor: numarul la care se va inmulti deinmultit
    '''
    return deinmultit*inmultitor

# print(inmultire.__doc__)



def scrie_numere_pare():
    '''Afiseaza pe cate o linie numerele pare pana la 100'''
    with open ('Week 7/numerepare.txt', 'w') as file:
        for nr in range(100):
            if nr % 2 == 0:
                file.write(str(nr)+"\n")

# scrie_numere_pare()

def scrieInFisier():
    '''Scrie intr-un fisier pana cand se introduce cuvantul gata'''
    while(True):
        cuvant = input("Introduceti cuvant: ")
        with open('Week 7/lista cuvinte.txt', 'a') as file:
            if cuvant == "gata":
                exit()
            else:
                file.write(cuvant + "\n")
             

# scrieInFisier()



lista = [1,2,5,8,9]


def verificaElementeNoi():
    nrElemente = len(lista)
    while True:
        element = input("Introduceti un caracter: ")
        if element.isalpha():
            continue
        if element.isdigit():
            lista.append(element)
            print(lista)
        if len(lista) == nrElemente:
            print("Nu avem elemente noi")
        else:
            print("Avem un element nou")


def verificaFisiereNoi():
    nrFisiere = 0
    fisiereVechi = []
    while True:
        fisiere = os.listdir('Week 7/monitorizat')
        if len(fisiereVechi) == len(fisiere):
            print("Nu avem fisiere noi")
        else:
            for fisierNou in fisiere:
                if not fisierNou in fisiereVechi:
                    print(fisierNou)
                    with open('Week 7/monitorizat/' + fisierNou, 'r') as file:
                        print(file.read())
        fisiereVechi = fisiere    
        time.sleep(5)

    
jsonArray = [{
                "contSursa":"RO312421",
                "contDestinatie":"RO4532432",
                "suma":123
            },
             {
                "contSursa":"RO312421",
                "contDestinatie":"RO4532432",
                "suma":123
            },
            {
                "contSursa":"RO312421",
                "contDestinatie":"RO4532432",
                "suma":123
            },
        ]

jsonString = json.dumps(jsonArray)
print(jsonString)


# verificaFisiereNoi()
        

