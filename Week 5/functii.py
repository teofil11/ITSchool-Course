# def aduna(x,y):
#     return x+y


# for i in range(10):
#     f(i)


# suma = aduna(2,3)
# print(suma)


# lista = [2,4,6,1,3,5,7,10]

# def medie_aritmetica(tava):
#     suma = 0
#     for nr in tava:
#         suma = suma + nr
#     medie = suma/len(tava)
#     print(medie)    

# medie_aritmetica(lista)



# def suma_lista(tava):
#     suma = 0
#     for el in tava:
#         suma = suma + el 
#     return suma


# def medie_aritmetica_2(tava):
#     suma = suma_lista(tava)
#     medie = suma / len(tava)

# medie_aritmetica(lista)
# print(medie_aritmetica_2(lista))



# def x():
#     for nr in range(10):
#         print(nr)
# x()


x = [1,3,9,3,5]
y = [4,4,7,22,5,6]

#calculeaza media aritmetica a elementelor unei liste (suma tuturor elementelor din lista impartita la numarul de elemente)

def ma (lista):
    suma = 0
    for element in lista:
        suma += element
    medie_aritmetica = suma / len(lista)
    print(medie_aritmetica)


# ma(x)


#creati o functie care calculeaza suma elementelor unei liste

def suma_elemente(lista):
    suma = 0
    for element in lista:
        suma += element
    return suma


# print(suma_elemente(y))



#rescrieti functia medie_aritmetica a.i sa foloseasca functia suma_lista pentru calculul sumei

def medie_aritmetica(lista):
    suma = suma_elemente(lista)
    ma = suma / len(lista)
    print(suma)

# medie_aritmetica(x)



#scrieti o functie care sa afiseze toate numerele de la 0 la 9

def elemente():
    for element in range(10):
        print(element)

# elemente()



#scrieti o functie care calculeaza numarul de cifre impare din lista

def impare(lista):
    nr_impare = 0
    for element in lista:
        if element % 2 != 0:
            nr_impare += 1
    return nr_impare

# print(impare(y))



#scrieti o functie care afiseaza ultima litera a fiecarui sir de caractere dintr-o lista

z = ['soare', 'luna','apa']

def ult_litera(lista):
    for element in lista:
        print(element[-1])

# print(ult_litera(z))


#scrieti o functie care returneaza ultima cifra a unui numar -> ultima_cifra(123) -> 3

def ult_cifra(numar):
    return numar%10

# print(ult_cifra(3454324123))


#scrieti o functie care taie ultima cifra a unui numar -> taie_cifra(123)-> 12

def taie_cifra(numar):
    return numar//10

# print(taie_cifra(123432))

#scrieti o functie care, folosind ultima_cifra(nr) si taie_cifra(nr) scrie numarul in ordine inversa 54321 -> 12345

def invers(numar):
    nr_invers = ''
    while numar > 0:
        ultima = ult_cifra(numar)
        numar = taie_cifra(numar)
        nr_invers += str(ultima)
    return nr_invers

# print(invers(123))


#scrieti o functie care verifica daca un numar se citeste la fel citit de la cap la coada si de la coada la cap (131,1332331,1331331)

def palindrom(numar):
    nr_invers = int(invers(numar))
    if nr_invers == numar:
        print("Numarul este palindrom")
    else:
        print("Nu este palindrom")

# palindrom(12321)


#scrieti o functie care calculeaza inmultirea a doua numere

def inmultire(x,y):
    return x*y

# print(inmultire(2, 4))


#scrieti o functie care calculeaza puterea n a unui numar x folosind functia de inmultire de mai sus

def putere(baza, exponent):
    putere = baza
    for i in range(exponent-1):
        putere = inmultire(putere, baza)
    return putere

# print(putere(2, 4))


#scrieti o functie care verifica daca un numar este prim (este divizibil doar cu el insusi)

def prim(x):
    flag = True
    for i in range(2,x//2+1):
        if x%i == 0:
            flag = False
    return flag 

# print(prim(7))


#scrieti o functie care afiseaza numarul de elemente prime din lista

def numere_prime(lista):
    nr_prime = 0
    for el in lista:
        if prim(el):
            nr_prime +=1
    print(nr_prime)

# numere_prime(x)


#scrieti o functie care afiseaza suma numerelor prime din lista 

def suma_prime(lista):
    suma = 0
    for el in lista:
        if prim(el):
            suma += el
    print(suma)

# suma_prime(x)


#scrieti o functie care primeste 2 siruri de caractere ca parametru si le concateneaza

def concatenare(sir1,sir2):
    return sir1 + sir2

#scrieti o functie care fiind dat un numar n returneaza 1*2*3*...*n

def factorial(nr):
    produs = 1
    for el in range(1,nr+1):
        produs *= el
    return produs

# print(factorial(5))


# Să presupunem că avem o listă de numere întregi și dorim să găsim numerele care sunt pare și să le adunăm

def suma_pare(lista):
    suma = 0
    for nr in lista:
        if nr % 2 == 0:
            suma += nr
    return suma

# print(suma_pare(y))


# Să presupunem că avem un dicționar cu informații despre angajații unei companii,
# inclusiv numele lor, salariile și numărul de ore lucrate.
# Dorim să calculăm salariul total pentru fiecare angajat, ținând cont de numărul de ore lucrate și de tariful orar.

angajati ={
  "Alex": {"ore lucrate": 30, "$ per ora": 9},
  "George": {"ore lucrate": 25, "$ per ora": 11},
  "Mihai": {"ore lucrate": 28, "$ per ora": 13}
}

def salarii(dict):
    sal = {}
    for name, data in dict.items():
        ore_lucrate = data["ore lucrate"]
        per_ora = data["$ per ora"]
        salariu_total = ore_lucrate * per_ora
        sal[name] = salariu_total
    return sal

# print(salarii(angajati))


def filtru_cuvinte(lista, lungime, doar_litere):
    lista_filtrata = []
    for cuvant in lista:
        if len(cuvant) >= lungime and cuvant.isalpha():
            lista_filtrata.append(cuvant)
    return lista_filtrata

lis = ['apa', '123', 'mancare', 'caine', 'banana2']

# print(filtru_cuvinte(lis, 5, doar_litere = True))



# Să presupunem că avem un set de numere întregi și dorim să aflăm care este cel mai mare număr din setul respectiv

def find_max_number(numbers):
    max_number = 0
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number


# print(find_max_number(y))


# Să presupunem că avem o listă de numere și dorim să obținem suma lor, dar să ignorăm numerele negative și să adunăm doar cele pozitive

def suma_pozitive(numere):
    suma = 0
    for num in numere:
        if num >= 0:
            suma +=num
    return suma

l = [1, -6, 4, -2, 3]
# print(suma_pozitive(l))


# Să presupunem că avem o listă de numere întregi
# și dorim să calculăm suma tuturor numerelor din listă care sunt divizibile cu un anumit număr dat.

def div_sum(lista, div):
    suma = 0
    for nr in lista:
        if nr % div == 0:
            suma += nr
    return suma

# print(div_sum(y, 2))




