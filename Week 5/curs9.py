#calculeaza media aritmetica a elementelor unei liste (suma tuturor elementelor din lista impartita la numarul de elemente)
def medie_aritmetica(tava):
    suma=0
    for el in tava:
        suma=suma+el
    medie=suma/len(tava)
    print(medie)

#creati o functie care calculeaza suma elementelor unei liste 
def suma_lista(tava):
    suma=0
    for el in tava:
        suma=suma+el
    return suma

#rescrieti functia medie_aritmetica a.i sa foloseasca functia suma_lista pentru calculul sumei 
def medie_aritmetica_2(tava):
    suma=suma_lista(tava)
    medie=suma/len(tava)
    return medie

#scrieti o functie care sa afiseze toate numerele de la 0 la 9 
def afisare_numere():
    for x in range(10):
        print(x)

#scrieti o functie care calculeaza numarul de cifre impare din lista 
def numara(tava):
    nr_cifre_impare=0
    for element in tava:
        if(element%2==1):
            nr_cifre_impare=nr_cifre_impare+1
    return nr_cifre_impare

#scrieti o functie care afiseaza ultima litera a fiecarui sir de caractere dintr-o lista
def ultima_litera(tava):
    for cuvant in tava:
        print(cuvant[-1])

#scrieti o functie care returneaza ultima cifra a unui numar -> ultima_cifra(123) -> 3 
def ultima_cifra(tava):
    return tava%10

#scrieti o functie care taie ultima cifra a unui numar -> taie_cifra(123)-> 12
def taie_cifra(nr):
    return nr//10

#scrieti o functie care, folosind ultima_cifra(nr) si taie_cifra(nr) scrie numarul in ordine inversa 54321 -> 12345 
def inverseaza(nr):
    invers=""
    while(nr>0):
        ult_cifra=ultima_cifra(nr)
        nr=taie_cifra(nr)
        invers+=str(ult_cifra)
    return invers

#scrieti o functie care verifica daca un numar se citeste la fel citit de la cap la coada si de la coada la cap (131,1332331,1331331)
def verifica_palindrom(nr):
    invers=int(inverseaza(nr))
    if(invers==nr):
        print("E palindrom")
    else:
        print("Nu e palindrom")


#scrieti o functie care calculeaza inmultirea a doua numere 
def inmultire(x,y):
    return x*y

#scrieti o functie care calculeaza puterea n a unui numar x folosind functia de inmultire de mai sus 
#3**4=3*3*3*3
def putere(baza,exponent):
    putere=baza
    for i in range(exponent-1):
        putere=inmultire(putere,baza)
    return putere

# #scrieti o functie prin care mariti valoarea unui numar cu n
# nr=100
# def mareste_numar(n):
#     global nr
#     nr=nr+n
# mareste_numar(10)
# mareste_numar(10)
# mareste_numar(20)
# print(nr)

#rescrieti functia de mai sus pentru a nu mai folosi variabila globala 
def mareste_numar(n,nr):
    nr=nr+n
    return nr

#scrieti o functie care verifica daca un numar este prim (este divizibil doar cu el insusi) 
def ePrim(nr):
    flag=0
    for i in range(2,nr//2+1):
        if(nr%i==0):
            flag=1
    if(flag==1):
        return True
    else:
        return False

#scrieti o functie care afiseaza numarul de elemente prime din lista 
def numara_prime(tava):
    nrPrime=0
    for el in tava:
        if(ePrim(el)):
            nrPrime=nrPrime+1
    print(nrPrime)
lista=[2,4,6,1,3,5,7,10]
charList=['cand','rasare','soarele','ies','pe','s']

#scrieti o functie care afiseaza suma numerelor prime din lista 
def suma_prime(tava):
    sum=0
    for el in tava:
        if(ePrim(el)):
            sum=sum+el
    print(sum)

#scrieti o functie care primeste 2 siruri de caractere ca parametru si le concateneaza 
def concateneaza(sir,sir2):
    return sir+sir2

#scrieti o functie care elimina elementele duplicate dintr-o lista
 
def elimina_duplicate(sir):
    frecvente={}
    for element in sir:
        if(frecvente.get(element)!=None):
            frecvente[element]=frecvente[element]+1
        else: 
            frecvente[element]=1
    lista=[]
    for cheie in frecvente:
        if(frecvente[cheie]==1):
            lista.append(cheie)
    return lista

#scrieti o functie care fiind dat un numar n returneaza 1*2*3*...*n
def factorial(n):
    produs=1
    for i in range(1,n+1):
        produs=produs*i
    return produs

# medie_aritmetica(lista)
# print(medie_aritmetica_2(lista))
#afisare_numere()
# print(numara(lista))
#ultima_litera(charList)
# print(ultima_cifra(1002))
# print(taie_cifra(10024))
# inverseaza(12345)
# inverseaza(12222)
# verifica_palindrom(12322)
# print(putere(2,1))
#ePrim(11)
#numara_prime(lista)
#suma_prime(lista)
# print(concateneaza("nume ","prenume"))
# lista=["ana","andreea","ana","dan"]
# lista=elimina_duplicate(lista)
# print(factorial(4))