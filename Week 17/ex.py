import csv

# Exercise 1:
# Write a Python program that asks the user for their name and greets them with a personalized message.

def hello():
    name = input('Nume: ')
    print(f'Salut {name}')

# Exercise 2:
# Write a Python function that takes a string as input and counts the number of vowels (a, e, i, o, u) in the string.

def vocale():
    string = str(input('Scrie textul: '))
    nr_vocale = 0
    vocale = 'aeiou'
    for litera in string:
        if litera in vocale:
            nr_vocale += 1
    print(nr_vocale)

# Exercise 3:
# Write a Python program that asks the user for a sentence and prints the sentence in reverse order.

def invers():
    string = str(input('Scrie textul: '))
    invers = string[::-1]
    print(invers)

# Exercise 4:
# Write a Python function that takes a string as input and checks if it is a palindrome (reads the same forwards and backwards).

def verifica_palindrom():
    string = str(input('Scrie textul: '))
    invers = string[::-1]
    if invers == string:
        print(f'{string} este palindrom')
    else:
        print(f'{string} nu este palindrom')


# Exercise 5:
# Write a Python program that asks the user for a sentence and prints the number of words in the sentence.

def numar_cuvinte():
    string = str(input('Scrie textul: '))
    lista_cuvinte = string.split(' ')
    print(f'Textul introdus are {len(lista_cuvinte)}')


# Exercise 6:
# Write a Python function that takes a string as input and returns a new string with all the vowels removed.

def elimina_vocale():
    string = str(input('Scrie textul: '))
    vocale = 'aeiou'
    return ''.join(litera for litera in string if litera not in vocale)


# Exercise 7:
# Write a Python program that asks the user for a sentence and prints the longest word in the sentence.
def cel_mai_lung_cuvant():
    string = str(input('Scrie textul: '))
    lista_cuvinte = string.split(' ')
    nr_litere = 0
    cel_mai_lung = ''
    for cuvant in lista_cuvinte:
        if len(cuvant) > nr_litere:
            cel_mai_lung = cuvant
    print(cel_mai_lung)



# Exercise 8:
# Write a Python function that takes a string as input and returns a new string with the first and last characters exchanged.

def inverseaza_litere():
    string = str(input('Scrie textul: '))
    new_string = string[-1] + string[1:-1] + string[0]
    print(new_string)


# Exercise 9:
# Write a Python program that asks the user for a sentence and checks if it is a pangram (contains all the letters of the alphabet).

def verifica_pangrama():
    string = str(input('Scrie textul: '))
    alfabet = 'abcdefghijklmnopqrstuvxyz'
    flag = True
    for litera in alfabet:
        if litera.lower() not in string:
            flag = False
    print(flag)


# Exercise 10:
# Write a Python function that takes a string as input and returns the number of occurrences of a specified word in the string.

def ex10():
    string = str(input('Scrie textul: '))
    x = str(input('Cuvant: '))
    aparitii = 0
    lista_cuvinte = string.split(' ')
    for cuvant in lista_cuvinte:
        if cuvant == x:
            aparitii += 1
    print(aparitii)

def ex11():
    dictionar = {
        "tabel['coloana1']": 'val1',
        "tabel['coloana2']": 'val2',
        "tabel['coloana3']": 'val3',
        "tabel['coloana4']": 'val4',
        "tabel['coloana5']": 'val5',
        "tabel['coloana6']": 'val6',
        "tabel['coloana7']": 'val7',
        "tabel['coloana8']": 'val8',
        "tabel['coloana9']": 'val9',
    }
    chei = list(dictionar.keys())
    nume_fisier = chei[0].split('[')[0]

    with open('Week 17/'+nume_fisier+'.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        header = []
        row = []
        for cheie in chei:
            coloana = cheie.split("'")[1]
            header.append(coloana)
            valoare = dictionar[cheie]
            row.append(valoare)
        writer.writerow(header)
        writer.writerow(row)




    

