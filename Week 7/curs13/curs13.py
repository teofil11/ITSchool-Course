#docstrings: creati o functie si definiti parametrii ei 
import datetime
import os
def exponent(baza:int,exponent=12):
    '''Aceasta functie returneaza baza ridicata la putere
    :param int baza: 
    :param int exponent: Puterea la care vrem sa ridicam baza.
    '''
    return baza**exponent



#Creati un fisier text nou numit paul.txt
def scriereInFisier():
    '''Aceasta functie va crea un fisier text numit paul.txt'''
    listaNume=["Paul","Robert","Leontin","Natalia","Teo"]
    file=open('curs13/paul.txt','w')
    for nume in listaNume:
        file.write(f"Eu sunt {nume}\n")
    file.close()

#scrieti o problema care sa citeasca de la tastatura un text si sa il scrie intr-un fiser
def altaScriereInFisier():
    '''Aceasta functie scrie in fisier un text citit de la tastatura'''
    text=input("Introduceti ceva: ")
    file=open('curs13/robert.txt','w')
    file.write(text)
    file.close()

def scrieInFisierCititDeLaTastatura():
    '''Aceasta functie citeste de la tastatura un text si numele fisierului. Scrie textul in fisier'''
    numeFisier=input("Introduceti numele fisierului: ")
    text=input("Introduceti textul:")
    file=open('curs13/'+numeFisier,'w')
    file.write(text)
    file.close()

def scrietiInFisier(extensia):
    '''Functia citesteste de la tastatura un text si numele fisierului si scrie textul in fisier
    :param str extensia: Extensia fiserului fara punct 
    '''
    numeFisier=input("Introduceti numele fisierului: ")
    text=input("Introduceti textul:")
    file=open('curs13/'+numeFisier+"."+extensia,'w')
    file.write(text)
    file.close()

def scrieDeMaiMulteOri():
    '''Scrie in fiser atata timp cat textul introdus de utilizator nu este exit'''
    text=input("Introduceti text:")
    while(text!='exit'):
        file=open('curs13/while.txt','a')
        file.write(text+'\n')
        file.close()
        text=input("Introduceti text:")

def logareAlegeriMeniu():
    '''Scrie o functie care logheaza fiecare alegere a utilizatorului in fisierul logs.txt in formatul data: alegere facuta'''
    print("""1. Aduceti meniu de bauturi
    2. Aduceti meniu de mancare
    3. Aduceti nota 
    4. Gata
    """)
    while(True):
        optiune=int(input("Introduceti o optiune: "))
        if(optiune==1):
            print("Aduc meniul de bauturi")
            file=open("curs13/logs.txt",'a')
            file.write(str(datetime.datetime.now())
            +": Utilizatorul a ales optiunea 1\n")
            file.close()
        if(optiune==2):
            print("Aduc meniul de mancare")
            file=open("curs13/logs.txt",'a')
            file.write(str(datetime.datetime.now())+": Utilizatorul a ales optiunea 2\n")
        if(optiune==3):
            print("Aduc nota")
            file=open("curs13/logs.txt",'a')
            file.write(str(datetime.datetime.now())+": Utilizatorul a ales optiunea 3\n")
            file.close()
        if(optiune==4):   
            print("Gata")
            file=open("curs13/logs.txt",'a')
            file.write(str(datetime.datetime.now())+": Utilizatorul a plecat\n")
            file.close()
            exit()

def scrieInFisier():
    '''Scrieti in fisier folosind with'''
    with open('mihai.txt','a') as file:
        file.write('Acesta e un fisier nou!')
    print("Functia a terminat")

def citesteLoguri():
    with open('curs13/logs.txt','r') as file:
        linie=file.readline()
        while(linie):
            print(linie)
            linie=file.readline()

def citestePrimeleNCaractere():
    '''Citeste primele n caractere din fisierul logs unde n este citit de la tastatura'''      
    n=int(input("Cate caractere vrei sa citesti: "))
    with open ('curs13/logs.txt','r') as file:
        caractere=file.read(n)
        print(caractere)

def citesteCateNCaractere():
    '''Citeste si afiseaza cate n caractere din fisierul logs unde n este citit de la tastatura'''      
    n=int(input("Cate caractere vrei sa citesti: "))
    with open ('curs13/logs.txt','r') as file:
        caractere=file.read(n)
        while(caractere):
            print(caractere)
            caractere=file.read(n)

def prezenta():
    with open('curs13/curs.txt','r') as prezenta:
        prezenta.truncate()
        persoana=prezenta.readline()
        while(persoana):
            persoana=persoana.replace(',\n','')
            prezent=input(f'{persoana}: ')
            with open('curs13/prezenta.txt','a') as rezultat:
                rezultat.write(f'{persoana}: {prezent}\n')
            persoana=prezenta.readline()


#scrie intr-un fisier, pe cate o linie toate numerele pare pana la 100 
#scrie intr-un fisier, toate cuvintele citite de la tastatura pana la introducerea cuvantului gata 

#main
#scriereInFisier()
#altaScriereInFisier()
#scrieInFisierCititDeLaTastatura()
#scrietiInFisier("docx")
#scrieDeMaiMulteOri()
#logareAlegeriMeniu()
#scrieInFisier()
#citesteLoguri()
#citestePrimeleNCaractere()
#citesteCateNCaractere()
prezenta()