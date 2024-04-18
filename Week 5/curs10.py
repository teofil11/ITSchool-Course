#1 Scrieti o functie care primeste ca parametri 3 numere si afiseaza maximul dintre acestea (puteti face fara for si fara while)
#2 Scrieti o functie care calculeaza suma tuturor elementelor dintr-o lista definita inaintea functiei( nu ca parametru)
#3 Scrieti functia de mai sus si transmiteti lista ca parametru 
#4 Scrieti o functie care sa inversese un sir de caractere primit ca parametru si sa il returneze 
#5 Scrieti o functie care returneaza produsul factorial al unui numar primit ca parametru( 10 factorial = 1*2*3*...*10)

#6 Scrieti o functie care returneaza elementele pare dintr-o lista 

def numarPar(lista):
    for element in lista:
        if(element%2==0):
            print(element)
#7 Scrieti o functie care returneaza elementele impare dintr-o lista
def numarImpar(lista):
    for element in lista:
        if(element%2!=0):
            print(element)
#8 Scrieti o functie care returneaza True atunci cand un numar primit ca parametru se afla in intervalul 3-10 si False in caz contrar
def returneaza(nr):
    if(nr in range(3,11)):
        return True
    else: 
        return False
    

def test(nr):
    for i in range(100):
        print(i)
        if(i==nr):
            return "gata"
#9 Scrieti o functie care primeste un sir de caractere ca parametru si afiseaza numarul de caractere mari si nr de caractere mici.
def litere(s):
    mare=0
    mic=0
    for c in s:
        if(c.isupper()):
            mare+=1
        elif(c.islower()):
            mic+=1
    print("Nr de litere mari este:"+str(mare))
    print("Nr de litere mici este:"+str(mic))
#HINT: Pentru a verifica daca un caracter este litera mare, folosim litera.isupper()  iar pentru a verifica daca e lietra mica litera.islower()
#10 Scrieti o functie care  primeste ca  parametru un sir de caractere si retunreaza doua siruri de caractere. Unul cu literele mari si unul cu literele mici
def generareLista(s):
    sirMare=""
    sirMic=""
    for c in s:
        if(c.isupper()):
            sirMare=sirMare+c
        elif(c.islower()):
            sirMic=sirMic+c
    return [sirMare,sirMic]
#11 Scrieti o functie care sa afiseze toate numerele prime dintr-o lista
def estePrim(nr):
    prim=True
    for i in range(2,nr):
        if nr%i==0:
            prim=False
    return prim

def afiseazaPrime(lista):
    for i in lista:
        if(estePrim(i)==True):
            print(i)

lista=[1,5,2,3,4]
# numarPar(lista)
# numarImpar(lista)
#print(returneaza(2))
# test(20)
#litere("acestaEsteUnTest")
# print(generareLista("acestaESTEunTest"))
afiseazaPrime