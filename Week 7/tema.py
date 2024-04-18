import datetime
import time
import os

# 1.
def numere():
    ''' Aceasta functie creaza un fisier text
    si scrie in el numerele de la 1 la 1000
    pe cate o linie
    '''
    with open('Week 7/numere.txt', 'a') as file:
        for nr in range(1, 101):
            file.write(f'{nr} \n') 

# numere()




# 2.
def numere_pare():
    '''Aceasta funcie citeste un fisier cu numere si scrie intr-un alt fisier numerele pare'''
    with open(f'Week 7/numere.txt', 'r') as file:
        file.readline()
        for linie in file: 
            if int(linie) % 2 == 0:
                with open('Week 7/problema2.txt', 'a') as file2:
                    file2.write(f'{linie}')
            
                
# numere_pare()        



# 3.

def numaratoare():
    '''Aceasta fincie este o numaratoare
    ea incepe sa numere de la 1 pana cand 
    programul este oprit. La urmatoarea rulare a programului
    incepe numaratoarea de unde a ramas
    '''
    while True:
        
        with open('Week 7/numaratoare.txt', 'r') as file2:
            numar_curent = int(file2.readline())
        numar_curent += 1
        with open("Week 7/numaratoare.txt", 'w') as file:
            file.write(str(numar_curent))
        print(numar_curent)

        time.sleep(2)

# numaratoare()




# 4. 

def data():
    '''Aceasta functie scrie intr-un fisier la fiecare
    10 secunde data curenta
    '''
    while True:
        with open('Week 7/datacurenta.txt', 'a') as file:
            file.write(f'{datetime.datetime.now()} \n')
        time.sleep(10)

# data()



# 5.

def verifica_cuvinte():
    '''Aceasta functie verifica cate 
    cuvinte sunt intr-un fisier
    '''
    with open('Week 7/lista cuvinte.txt', 'r') as file:
        continut = file.read()
        numar_cuvinte = len(continut.split())
    return numar_cuvinte

# print(verifica_cuvinte())


# 6.

def frecventa():
    '''Aceasta functie calculeaza freecventa
    cuvintelor dintr-un fisier
    '''
    frecvente = {}
    with open('Week 7/lista cuvinte.txt', 'r') as file:
        continut = file.read()
        for cuvant in continut.split():
            if cuvant in frecvente:
                frecvente[cuvant] += 1
            else:
                frecvente[cuvant] = 1
        return frecvente

# print(frecventa())


# 7.

def toate_fisierele():
    '''Aceasta funcie afiseaza si scrie intr-un 
    fisier toate fisierele dintr-o cale'''
    lista_fisiere = os.listdir("C:/Users/Teofil/Desktop/IT School/Curs/Week 7")
    with open('Week 7\listafisiere.txt', 'w') as file:
            for fisier in lista_fisiere:
                print(fisier)
                file.write(fisier + '\n')

toate_fisierele()
