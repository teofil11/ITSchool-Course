def patrat():
    try:
        n = int(input("n= "))
        n = n**2
        print(n)
    except ValueError:
        print("Trebuie sa introduceti un numar inreg")
# patrat()


def citeste_numar():
    try:
        n = int(input('Introduceti numar: '))
        n = n-2
        print(n)
    except:
        print("Trebuie introdus un numar")
        citeste_numar()

# citeste_numar()


def numere():
    try:
        a = int(input("Introduceti primul numar: "))
        b = int(input("Introduceti al doilea numar: "))
        print(a/b)
    except ZeroDivisionError:
        print("b trebuie sa fie diferit de 0")
        numere()

# numere()

def gaseste_in_lista():
    lista = [2,4,1,4,2]
    try:
        n = int(input("Introduceti indexul: "))
        print(lista[n])
    except IndexError:
        print(f"Indexul listei este de la 0 la {len(lista)-1}")
        gaseste_in_lista()

# gaseste_in_lista()

def lungime(n):
    try:
        print(len(n))
    except TypeError:
        print("Parametrul nu poate fi masurat")

# lungime(2)


def citire_dict(key):
    a = {"a":1,"b":2,"c":3}
    try:
        print(a[key])
    except KeyError:
        print("Aceasta cheie nu exista in dictionar")

# citire_dict("g")


def citeste_fisier(fisier):
    try:
        with open('Week 10/'+ fisier, 'r') as file:
            continut = file.read()
            print(continut)
    except FileNotFoundError:
        print("Acest fisier nu exista")

# citeste_fisier('file.txt')


def fisier_json(nume_json):
    numefisier = nume_json.split('.')
    try:
        if numefisier[1] != "json":
            raise Exception("Fisierul nu este json")
    except Exception as e:
        print(e)       


# fisier_json("nume.json")

