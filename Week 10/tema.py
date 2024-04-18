import json


# 1. Scrie o functie care sa citeasca de la tastatura un numar si incearca sa scada 2 din el.
#  In cazul in care utilizatorul nu introduce numar, afiseaza eroare.

def numar():
    try:
        nr = int(input("Introduceti un numar: "))
        print(nr - 2)
    except:
        print("Trebuie sa introduceti un numar")
        numar()

# numar()


#2.Scrieti o functie care citeste de la tastatura 2 numere si caluleaza a/b.
#  Verificati ca nu crapa in cazul in care al doilea numar este 0.

def impartire():
    try:
        a = int(input('Introduceti primul numar:'))
        b = int(input('Introduceti al doi-lea numar: '))
        print(a//b)
    except ZeroDivisionError:
        print("Al doi-lea numar trebuie sa fie diferit de zero")
        impartire()

# impartire()

#3.Scrieti o functie care citeste un numar n de la tastatura si afiseaza al n-lea element din lista: [2,4,1,4,2]
#Verificati cazul in care indexul nu exista. 

def index_lista():
    lista = [2,4,1,4,2]
    try:
        n = int(input('Introduceti un numar: '))
        print(lista[n])
    except IndexError:
        print(f"Indexul listei este de la 0 la {len(lista)-1}")
        index_lista()

# index_lista()

#4.Scrieti o functie care citeste un string de la tastatura si afiseaza lungimea lui. Tratati cazul in care textul nu este string.

def lungime_string():
    try:
        x = str(input("Introduceti un text: "))
        print(len(x))
    except TypeError:
        print('Textul introdus trebuie sa fie string')

# lungime_string()


#5.Fiind dat un dictionar {"a":1,"b":2,"c":3} scrieti o functie care primeste ca parametru cheia si returneaza valoarea 

def citeste_dict():
    dict = {"a":1,"b":2,"c":3}
    try:
        key = input('Introduceti cheia: ')
        print(dict[key])
    except KeyError:
        print('Aceasta cheie nu exista in dictionar.')
        citeste_dict()

# citeste_dict()


#6.Scrieti o functie care primeste numele unui fisier ca parametru si citeste si afiseaza continutul acestuia. Tratati cazul in care fisierul nu exista.

def citeste_fisier(fisier):
    try:
        with open('Week 10/'+fisier, 'r') as file:
            continut = file.read()
            print(continut)
    except FileNotFoundError:
        print("Acest fisier nu exista")

# citeste_fisier('file.txt')


#7.Scrieti o functie care primeste ca parametru numele unui fisier json si ridica o exceptie daca fisierul nu este de tip json 

def fisier_json(nume_json):
    nume_fisier = nume_json.split('.')
    try:
        if nume_fisier[1] != 'json':
            raise Exception("Fisierul nu este json")
    except Exception as e:   
        print(e)
    
    try:
        n = int(input("Introduceti un numar: "))
    except :
        print("Trebuie sa introduceti un numar.")
    try:
        with open('Week 10/' + nume_json, 'r') as file:
            continut = json.load(file)
            print(continut[n])
    except IndexError:
        print('Ai depasit indexul')
    

# fisier_json('employees.json')

#10.Scrieti o functie care citeste fisierul text.txt. De asemenea, functia va citi un numar n de la tastatura.
# De pe fiecare linie afisati al n-lea element.
# In cazul in care o linie are mai putin elemente de n,
# afisati mesajul: pe linia curenta nu exista N elemente.


def read_file():
    try:
        n = int(input('Introduceti un numar: '))
        with open('Week 10/file.txt') as file:
            for linie in file:
                cuvinte = linie.strip().split()
                print(cuvinte[n])
    except IndexError:
        print("Pe linia curenta nu exista n elemente")

# read_file()


