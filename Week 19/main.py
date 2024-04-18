import random
import json

def json_ex():
    masini = []
    masina = {}
    marci_masini = ['VW','Seat','Audi','Ford','Dacia','Renault','KIA']
    with open('Week 19/input.json', 'r') as file:
        continut = json.load(file)
    masini.append(continut[0])
    for i in range(50):
        masina = {
            'marca' : random.choice(marci_masini),
            'anFabricatie' : random.randint(2007,2023),
            'nrKm' : random.randint(0,300000),
            'itpValid' : random.choice([True, False])
        }
        masini.append(masina)
        
    
    with open('Week 19/output.json', 'w') as file:
        json.dump(masini,file, indent=4)

# json_ex()


# // int -> random int
# // boolean -> random boolean
# // make -> o valoare din fisierul de tip text (array) make.txt  
# // nested -> o valoare din fisierul de tip json (array) numit nested_[make]_[model].json 
# // ..

# def create_json(nr_obiecte):
#     obiecte_generate = []
#     for i in range(nr_obiecte):
#         obiecte_generate.append({})
#     with open('Week 19/input2.json', 'r') as file:
#         continut = json.load(file)
#     continut = continut[0]
#     for key in continut:
#         spargere = continut[key].split(',')
#         if spargere[0] == 'int':
            


# create_json()