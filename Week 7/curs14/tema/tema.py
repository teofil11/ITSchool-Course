import json

# 1.

def dict_json():
    '''Aceasta functie citeste un fisier json
    si returneaza continutul lui intr-un dictionar'''
    with open('Week 7/curs14/tema/employees.json', 'r') as file:
        continut = json.load(file)
    return continut
    
# print(dict_json())

# 2. 


def plataSalarii():
    '''Aceasta funcie citeste un fisier json
    si calculeaza suma necesara pentru plata salariilor'''
    salarii = 0
    with open('Week 7/curs14/tema/employees.json', 'r') as file:
        continut = json.load(file)
        angajati = (continut.get("employees"))
        for angajat in angajati:
            salarii += angajat.get('salary')
        print(salarii)

# plataSalarii()

# 3.

def info_company():
    '''Aceasta functie citeste un fisier json
    si afiseaza informatii despre compamie'''
    with open('Week 7/curs14/tema/employees.json', 'r') as file:
        continut = json.load(file)
        info = continut.get("company_info")
        print(info.get('address'))

# info_company()

# 4.

def info_employees(departament):
    '''Aceasta funcitie citeste un fisier JSON si 
    afiseaza salariul angajatilor dintr-un departament
    :param str departament: departamentul din care se va afisa salariul angajatilor,
    parametrul se introduce intre ghilimele
    '''
    with open('Week 7/curs14/tema/employees.json', 'r') as file:
        continut = json.load(file)
        angajati = continut.get("employees")
        for angajat in angajati:
            if departament == angajat.get('department'):
                print(f'Angajatul {angajat.get("name")} are salariul {angajat.get("salary")}')
            


        

# info_employees('Sales')