import csv
import json


def citeste_date():
    n = int(input("De cate ori vrei sa introduci informatiile: "))
    with open('Week 9/date.csv', 'w') as file:
        file.write("Nume,Varsta,Salariu"+'\n')
        for i in range(n):
            nume = input('Introduceti nume: ')
            varsta = input("Introduceti varsata: ")
            salariu = input("Introduceti salariul: ")
            print('_'*10)
            file.write(nume+','+varsta+','+salariu+'\n')

# citeste_date()


def scrie_csv():
    dictionar = []
    n = int(input("De cate ori vrei sa introduci informatiile: "))
    for i in range(n):
        nume = input('Introduceti nume: ')
        varsta = input("Introduceti varsata: ")
        salariu = input("Introduceti salariul: ")
        dictionar.append([nume, varsta, salariu])
        print('_'*10)
    with open('Week 9/date.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(dictionar)


# scrie_csv()


def scrie_json():
    with open('Week 9/date.csv', 'r') as file:
        fisier = csv.reader(file)
        json = []
        chei = []
        for i, row in enumerate(fisier):
            if i != 0:
                json.append({chei[0]: row[0], chei[1]: row[1], chei[2]: row[2]})
            else:
                chei = row
    print(json)

# scrie_json()


def scrie_json_1():
    angajati = [
        {
            "Nume": "Dan",
            "Prenume": "Stan",
            "Salariu": 1500,
            "Firma": {
                    "Nume firma": "ewq",
                    "CUI": 1231,
                    "Numar angajati": 12
            }
        },
        {
            "Nume": "Ilie",
            "Prenume": "Ionut",
            "Salariu": 2000,
            "Firma": {
                    "Nume firma": "qwe",
                    "CUI": 132,
                    "Numar angajati": 23
            }
        },
        {
            "Nume": "Ion",
            "Prenume": "Claudiu",
            "Salariu": 2200,
            "Firma": {
                    "Nume firma": "qeew",
                    "CUI": 43532,
                    "Numar angajati": 42
            }
        }
    ]

    masini = [{
        "Mercedes": {
            "Pilot automat": "da",
            "Senzor parcare": "da",
            "Geamuri electrice": "da",
        },
        "Audi": {
             "Pilot automat": "da",
            "Senzor parcare": "da",
            "Geamuri electrice":"da",
        }

        }
    ] 
    jsonstring = json.dumps(angajati, indent=4,separators=",:")
    
    with open('Week 9/info.json', 'w') as file:
        file.write(jsonstring) 



# scrie_json_1()

def write_csv():
    with open('Week 7/curs14/tema/employees.json', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([', Employee', "Developer", '123432'])

# write_csv()

def functie():
        while True:
            with open('Week 9/fisier.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                optiune = int(input("""1.Adauga rand
2.Iesire
"""))
                if optiune == 1:
                    varsta = int(input("Introduceti varsta: "))
                    nume = input("Introduceti numele: ")
                    writer.writerow([varsta, nume])

# functie()

def afiseaza_json():
    with open('Week 9/info.json', 'r') as file:
        continut = json.load(file)
        print(continut)

# afiseaza_json()

def info_json():
    with open('Week 9/info.json', 'r') as file:
        data = json.load(file)
    nume = input("Introduceti numele: ")
    prenume = input("Introduceti prenumele: ")
    salariu = int(input("Introduceti salariul: "))
    nume_firma = input("Introduceti numele firmei: ")
    cui = int(input("Introduceti CUI: "))
    numar_angajati = int(input("Introduceti numarul de angajati: "))
    data.append({"Nume": nume, "Prenume": prenume, "Salariu": salariu, "Firma":{"Nume firma": nume_firma, "CUI": cui, "Numar angajati": numar_angajati}})
    with open('Week 9/info.json', 'w') as file:
        json.dump(data, file,indent=8,separators=",:")

# info_json()


def editeaza_json():
    with open('Week 9/info.json', 'r') as file:
        continut = json.load(file)
    continut[0][("Firma")]["Numar angajati"] = 20
    with open('Week 9/info.json', 'w') as file:
        json.dump(continut,file, indent=8,separators=",:")

editeaza_json()


def elemente_json ():
    with open('Week 9/info.json','r') as file:
        continut = json.load(file)
        print(len(continut))

# elemente_json()

def scrie_in_json():
    data = []
    nume = input("Introduceti numele: ")
    varsta = int(input("Introduceti varsta: "))
    oras = input("Introduceti orasul: ")
    data.append({"nume": nume,"varsta":varsta,"oras":oras})
    with open('Week 9/ex.json','w') as file:
        json.dump(data, file,indent=4)

# scrie_in_json()

def afiseaza_din_json():
    with open('Week 9/info.json', 'r') as file:
        continut = json.load(file)
        index = 0
        while index < len(continut):
            for key, value in continut[index].items():
                print(key + ':', value)
            index +=1

# afiseaza_din_json()

def afiseaza_nume_json():
    with open('Week 9/info.json', 'r') as file:
        continut = json.load(file)
        for angajat in continut:
            print(angajat["Nume"])

# afiseaza_nume_json()

def cauta_in_json():
    search = input("Ce doriti sa cautati: ")
    if search.isdigit():
        search = int(search)
    with open('Week 9/info.json', 'r') as file:
        continut = json.load(file)
    index = 0
    while index < len(continut):
        for key,value in continut[index].items():
            if search == value:
                print(continut[index]['Nume'], key)
        for x,y in continut[index]["Firma"].items():
            if search == y:
                print(f'{x} firma {continut[index]["Firma"]["Nume firma"]}')
        index += 1

# cauta_in_json()

def convert_csv_json():
    csv_file = input("Introduceti numele fisierului csv: ")
    csv_file += '.csv'
    json_dict = []
    with open('Week 9/'+csv_file,'r') as file:
        continut = csv.DictReader(file)
        for row in continut:
            json_dict.append(row)
    with open('Week 9/convertJSON.json','w') as file:
        json.dump(json_dict, file,indent=4)
            

# convert_csv_json()

