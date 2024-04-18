# 0. Creati o functie care citeste de la tastatura o lista si o returneaza

def list():
    lista = []
    for i in range(5):
        i = int(input("Introduceti un numar: "))
        lista.append(i)
    return lista

# print(list())


# 1. verificati daca toate numerele dintr-o lista sunt pare 

def pare():
    lista = [12,4,6]
    for nr in lista:
        if nr%2 != 0:
            return False
    return True

# print(pare())


# 2. verificati daca cel putin un numar dintr-o lista este divizibil cu 5

def divizibil(nr):
    lista = [2,15,26,11,17,9,7]
    for numar in lista:
        if numar % nr == 0:
            return True
    return False

# print(divizibil(5))

# 3. Verificati ca exista fix 3 numere pare intr-o lista

def nr_pare():
    lista = [2,15,26,11,17,9,7,4]
    nr_numar_pare = 0
    for nr in lista:
        if nr % 2 == 0:
            nr_numar_pare += 1
    if nr_numar_pare == 3:
        return True
    else: 
        return False

# print(nr_pare())

# 4. creati o functie care sa verifice daca toate elementele unui sir sunt unice 

def unic():
    sir = 'sadfdgfdpogikasdasd'
    dict = {}
    for value in sir:
        if value in dict:
            dict[value] += 1
        else:
            dict[value] = 1
    for value in dict.values():
        if value > 1:
            return False
    return True

# print(unic())

# 5. creati o functie care verifica daca toate liniile unui fisier au aceeasi lungime 

def files():
    lungimi = []
    with open('Week 19/text.txt', 'r') as file:
        continut = file.readlines()
    for line in continut:
        lungime_linie = len(line.replace('\n', ''))
        lungimi.append(lungime_linie)
    for lungime in lungimi:
        if lungime != lungimi[1]:
            return False
    return True
        
# print(files())


# 6. creati o functie care verifica daca o parola respecta toate conditiile de securitate (contine un caracter special, are o litera mare, si o cifra)

def password(parola):
    caracter_special = False
    litera_mare = False
    cifra = False

    if (not caracter.isalnum() for caracter in parola):
        caracter_special = True
    if (caracter.isupper() for caracter in parola):
        litera_mare = True
    if (caracter.isdigit() for caracter in parola):
        cifra = True
    
    if caracter_special and litera_mare and cifra:
        return True
    return False

print(password('Parola1*'))