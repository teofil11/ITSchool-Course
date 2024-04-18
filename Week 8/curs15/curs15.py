import csv 

#probleme curs 
# 1. Citeste fisierul csv persoane.csv ca csv si afiseaza primele 2 persoane 
# 2. Scrie un fisier csv cu date despre persoane si varsta acestora 
# 3. Scrie o functie care afiseaza cnp-urile tuturor persoanelor din fisierul persoane
# 4. Scrie o functie care sa identifice pe baza cnp-ului daca o persoana este femeie sau barbat (daca cnp-ul incepe cu 1 e barbat, daca incepe cu 2 e femeie) 
# 5. Scrie o functie care identifica anul nasterii unei persoane pe baza CNP-ului (cifra a doua si a 3-a din CNP) 
# 6. Scrie o functie care identifica luna nasterii unei persoane pe baza CNP-ului (cifra a 4-a si a 5-a din CNP ) 
# 7. Scrie o functie care identifica ziua nasterii unei persoane pe baza CNP-ului (cifra a 6- si a 7-a din CNP) 
# 8. Afisati persoanele care au ziua de nastere in ziua rularii programului. (luati data curenta din modulul datetime) 

#CITIRE FISIER
def citeste_curs():
    with open("Week 8/curs15/curs.csv","r") as file:
        fisier=csv.reader(file)
        for row in fisier:
            print(row[0])

citeste_curs()
# SCRIERE FISIER
continut=[
    ['Nume','Varsta','Oras'],
    ['Andrei',22,'Bucuresti'],
    ['Matei',21,'Timisoara']
]
def scrie_fisier():
    with open('curs15/my_file.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(continut)

#scrieti o functie care citeste un fisier json si il saveaza ca csv 
import json
def convert_json_2_csv():
    #cu json.loads() - incarc json object din string 
    # with open("curs15/employees.json","r") as file:
    #     jsonText=file.read()
    #     jsonObject=json.loads(jsonText)
    # print(jsonObject[1])

    #cu json.load() - incarc json object din file 
    with open("curs15/employees.json","r") as file:
        jsonObject=json.load(file)
    continut=[]
    continut.append(["Id","Name","Position","Salary"])
    for angajat in jsonObject:
        continut.append([angajat["id"],angajat["name"],angajat["position"],angajat['salary']])
    with open('curs15/employees.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(continut)
# convert_json_2_csv()