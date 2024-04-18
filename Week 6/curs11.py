#1.scrieti o functie care afiseaza suma a doua numere 
def suma(a,b):
    return a+b
#2.scrieti o functie care afiseaza produsul a doua numere 
def produs(a,b):
    return a*b
#3.scrieti o functie care afiseaza in ordine crescatoare toate valorile cuprinse intre cele 2 numere
def interval(a,b):
    if(a<=b):
        for i in range(a,b):
            print(i)
    else:
        for i in range(b,a):
            print(i)
#MENIU: cititi 2 numere de la tastatura si intrebati apoi utilizatorul ce functie doreste sa apeleze astfel: 
#pentru a afisa suma a doua numere, introduceti cifra 1 
#pentru a afisa produsul a doua numere, introduceti cifra 2 
#pentru a afisa intervalul, introduceti cifra 3
#pentru a iesi, apasati tasta 4 

def meniu():
    a=int(input("a="))
    b=int(input("b="))
    
    optiune=0
    while(optiune!=4):
        print("""pentru a afisa suma a doua numere, introduceti cifra 1 
pentru a afisa produsul a doua numere, introduceti cifra 2
pentru a afisa intervalul, introduceti cifra 3""")
        optiune=int(input("optiune="))
        if(optiune==1): 
            print(suma(a,b))
        elif(optiune==2): 
            print(produs(a,b))
        elif(optiune==3):
            print(interval(a,b))

#meniu()

#scrieti un program care afiseaza 1 la infinit 
optiune=10
# while(True):
#     print(1)

#4.scrieti o functie care citeste 5 elemente de la tastatura elemente si le incarca intr-o lista 
def creeaza_lista():
    lista=[]
    for nr in range(5):
        lista.append(input())
    return lista

# lista=creeaza_lista()

#5.scrieti o functie care afiseaza fiecare element si pozitia lui. Exemplu sir[0]=valoare
def afiseaza_elemente(lista):
    for i in range(len(lista)):
        print(f"sir[{i}]={lista[i]}")
# afiseaza_elemente(lista)
#6.scrieti o functie care citeste valori de la tastatura pana se introduce cuvantul gata 
def ia_gata():
    variabila=""
    while(variabila.lower()!="gata"):
        variabila=input("Introduceti cuvant: ")
# ia_gata()

#7.scrieti o functie care afiseaza toate valorile dintr-un sir pana la intalnirea unui numar impar 
#cu for 
def pana_la_impar(lista):
    for i in lista:
        if(i%2==1):
            break
        else:
            print(i)


#cu while
def pana_la_impar_cu_while(lista):
    i=0
    while(lista[i]%2==0):
        print(lista[i])
        i=i+1
# pana_la_impar_cu_while(sir)

#8.scrieti o functie care face suma tuturor numerelor dintr-un sir pana la intalnirea unui numar par 
#cu for 
def suma_pana_la_par(lista):
    suma=0
    for i in lista:
        if(i%2==0):
            break
        else:
            suma+=i
    return suma

#cu while
def suma_suma_pana_la_par_cu_while(lista):
    suma=0
    i=0
    while(lista[i]%2==1):
        suma+=lista[i]
        i=i+1
    return suma

#9.scrieti o functie care calculeaza suma cifrelor unui numar  432
def suma_cifre(nr):
    suma=0
    while(nr>0):
        cifra=nr%10
        suma=suma+cifra
        nr=nr//10
    return suma

#10. scrieti o functie care verifica daca un string contine doar litere
def contine_doar_litere(string):
    suntToateLitere=True
    for litera in string:
        if(litera.isalpha()==False):
            suntToateLitere=False
    return suntToateLitere

#11. scrieti o functie care verifica daca un string contine doar litere,cifre si caracterul *  4a*_ewq
def contine_anumite_litere(string):
    suntToateOk=True
    for litera in string:
        if(litera.isalpha()==False):
            if(litera.isdigit()==False):
                if(litera!="*"):
                    suntToateOk=False
    return suntToateOk

#12. scrieti o functie de inregistrare a utilizatorilor 
def signUp():
    username=""
    password=""
    ok=False
    while(ok==False):
        username=input("username: ")
        if(contine_doar_litere(username)==True):
            ok=True
        else:
            print("Username-ul trebuie sa contina doar litere! Va rugam reintroduceti!")
    ok2=False
    while(ok2==False):
        password=input("password=")
        if(contine_anumite_litere(password)==True):
            ok2=True
        else:
            print("Parola poate sa contina doar litere, cifre si caracterul *")
    return {"username":username,"password":password}
#13. scrieti o functie de resetare a parolei 
def reset_password():
    ok=False
    newPassword=""
    while(ok==False):
        newPassword=input("Introduceti noua parola: ")
        if(contine_anumite_litere(newPassword)==True):
            ok=True
        else:
            print("Parola poate sa contina doar litere, cifre si caracterul *")
    return newPassword
#14. scrieti o functie de autentificare. Sa se intampla de maxim 3 ori apoi sa afiseze cont blocat 
#15. creati un meniu care permite sa alegeti intre urmatoarele variante:
#resetare parola 
#autentificare 
#inregistrare 
#iesire

sir=[1,2,4,6,1,8,10]
# pana_la_impar(sir)
# print(suma_suma_pana_la_par_cu_while(sir))
# print(suma_cifre(432))
# print(contine_doar_litere("aaadads"))
dict=signUp()
dict['password']=reset_password()
print(dict)
signUp()