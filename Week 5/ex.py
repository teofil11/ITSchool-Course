#1 Scrieti o functie care primeste ca parametri 3 numere si afiseaza maximul dintre acestea

def maxim(x, y, z):
    return max(x, y, z)
# print(maxim(3, 18, 7))


#2 Scrieti o functie care calculeaza suma tuturor elementelor dintr-o lista definita inaintea functiei( nu ca parametru)

l = [1,6,4,3]

def suma_lista(numere):
    suma = 0
    for nr in numere:
        suma += nr
    return suma

# print(suma_lista(l))



#3 Scrieti functia de mai sus si transmiteti lista ca parametru
def sum_lista(l):
    suma = 0
    for nr in l:
        suma += nr
    print(suma)
    
# sum_lista(l)



#4 Scrieti o functie care sa inversese un sir de caractere primit ca parametru si sa il returneze 

def invers(sir):
    return sir[::-1]

# print(invers('portocala'))



#5 Scrieti o functie care returneaza produsul factorial al unui numar primit ca parametru

def factorial(x):
    produs = 1
    for nr in range(1, x+1):
        produs *= nr
    print(produs)

# factorial(5)



#6 Scrieti o functie care returneaza elementele pare dintr-o lista


def pare(lista):
    for nr in lista:
        if nr % 2 == 0:
            print(nr)

pare(l)


