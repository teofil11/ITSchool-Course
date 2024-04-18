import csv
import datetime

# 1. Citeste fisierul csv persoane.csv ca csv si afiseaza primele 2 persoane 
def citeste_csv():
    with open('Week 8/persoane.csv', 'r') as file:
        fisier = csv.reader(file)
        for i,persoana in enumerate(fisier):        
            if i > 2:
                break
            print(persoana)
            
            
            

# citeste_csv()


# 2. Scrie un fisier csv cu date despre persoane si varsta acestora 

continut = [
    ['Nume','Varsta', 'Oras'],
    ['Catalin', 25, 'Bucuresti'],
    ['Gabriel', 27, 'Oradea']
]

def scrie_csv():
    with open('Week 8\datepersoane.csv', 'w', newline='') as file:
        scrie = csv.writer(file)
        scrie.writerows(continut)
        
# scrie_csv()


# 3. Scrie o functie care afiseaza cnp-urile tuturor persoanelor din fisierul persoane
def afiseaza_CNP():
    with open('Week 8/persoane.csv', 'r') as file:
        fisier = csv.reader(file)
        for row in fisier:
            print(row[2])

# afiseaza_CNP()

# 4. Scrie o functie care sa identifice pe baza cnp-ului daca o persoana este femeie sau barbat (daca cnp-ul incepe cu 1 e barbat, daca incepe cu 2 e femeie)


def gen_persoane():
    with open('Week 8/persoane.csv', 'r') as file:
        fisier = csv.reader(file)
        for i in fisier:
            gen = i[2]
            if gen[0] == '1':
                print(f'{i[0]} {i[1]} este de sex masculin')
            elif gen[0] == '2':
                print(f'{i[0]} {i[1]} este de sex feminin')
            else:
                continue

# gen_persoane()

# 5. Scrie o functie care identifica anul nasterii unei persoane pe baza CNP-ului (cifra a doua si a 3-a din CNP)

def an_nastere():
    with open('Week 8/persoane.csv') as file:
        fisier = csv.reader(file)
        an = '19'
        for i in fisier:
            an2 = i[2]
            if  an2.isalpha():
                continue
            print(f'{i[0]} {i[1]} este nacut in anul {an}{(an2[1:3])}')

# an_nastere()

# 6. Luna nastere

lunile_anului = {
    "ianuarie":'01',
    "februarie":'02',
    "martie":'03',
    "aprile":'04',
    "mai":'05',
    "iunie":'06',
    "iulie":'07',
    "august":'08',
    "septembrie":'09',
    "octombrie":'10',
    "noiembrie":'11',
    "decembrie":'12' 
}


def luna_nastere():
    with open('Week 8/persoane.csv', 'r') as file:
        fisier = csv.reader(file)
        for i in fisier:
            luna = i[2]
            l = luna[3:5]
            for x in lunile_anului:
                if l == lunile_anului[x]:
                    l = list(lunile_anului.keys())[list(lunile_anului.keys()).index(x)]
                    print(f'{i[0]} {i[1]} este nascut in luna {l}')

# luna_nastere()

# 7. Ziua nastere

def ziua_nastere():
    with open('Week 8/persoane.csv', 'r') as file:
        fisier = csv.reader(file)
        for i in fisier:
            ziua = i[2]
            if ziua.isalpha():
                continue
            print(f'{i[0]} {i[1]} este nascut in ziua {ziua[5:7]}')

# ziua_nastere()

# 8. Afisati persoanele care au ziua de nastere in ziua rularii programului. (luati data curenta din modulul datetime)

def astazi():
    with open('Week 8/persoane.csv', 'r') as file:
        fisier = csv.reader(file)
        for i,row in enumerate(fisier):
            if i!=0:
                cnp = row[2]
                luna = cnp[3:5]
                ziua = cnp[5:7]
                luna_curenta = datetime.datetime.now().month
                ziua_curenta = datetime.datetime.now().day
                if luna_curenta < 10:
                    luna_curenta = "0" + str(luna_curenta)
                if ziua_curenta < 10:
                    ziua_curenta = "0" + str(ziua_curenta)
                if luna_curenta == luna and str(ziua_curenta) == ziua:
                    print(row[0]+' '+ row[1])

                      
# astazi()


