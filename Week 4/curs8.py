lista = [0,4,2,1,4,5,6]
#pozitii 0 1 2 3 4 5 6
#afisare valorilor din lista 
for element in lista: 
    print(element)

#afisare pozitii din lista 
for element in range(10): 
    print(element)

for element in range(10):
    print(element) #afisare pozitie
    print(lista[element]) #afisare element

# # Afisati numerele de la 1 la 10 folosind un for 
for x in range(10):
    print(x+1)

# #Afisati numerele de la 1 la 9 din 2 in 2 
for x in range(1,10,2):   #range(startNr, endNr,pas)
    print(x)

##Salvati primele 10 numere pare intr-o lista
lista=[]
for x in range(20):
    if(x%2==0):
        lista.append(x)
print(lista)

# #Afisati suma tuturor numerelor din lista de mai sus
sum=0
for element in lista: 
    sum=sum+element
print(sum)

#Afisati numerele mai mari ca 10 din lista de mai sus 
for element in lista: 
    if element>10:
        print(element)

#Afisati fiecare caracter dintr-un sir de caractere citit de la tastatura folosind un for 
sir=input("Introduceti un sir de caractere: ")
for element in sir: 
    print(element)


#Dictionareeee!!!

#Calculati frecventa literelor dintr-un sir de caractere 
# abbbaaacccc
# a - 4
# b - 3 
# c - 4 

frecvente={}

print(frecvente.get("a"))
sir=input("Introduceti un sir: ")
for litera in sir:
    if(frecvente.get(litera)==None):
        frecvente[litera]=1
    else:
        frecvente[litera]=frecvente[litera]+1
print(frecvente)

#Traduceti din engleza urmatoarele cuvinte pana cand utilizatorul introduce cuvantul stop: 
#mama=mother
#tata=father
#copil=child
#se=are
#plimba=walking
#prin=in the
#parc=park

dictionar={
    "mama":"mother",
    "tata":"father",
    "copil":"child",
    "se":"are",
    "plimba":"walking",
    "prin":"in the",
    "parc":"park"
}
introdusDeLaTastatura=""
while(introdusDeLaTastatura!="stop"):
    introdusDeLaTastatura=input("Introduceti cuvant: ")
    if(dictionar.get(introdusDeLaTastatura)!=None):
        print(dictionar[introdusDeLaTastatura])

#Spargeti un sir de caractere pe baza unui alt caracter 
#sirul acesta este lung
#lista=["sirul","acesta","este","lung"]
variabila="sirul acesta este lung"
lista=variabila.split(" ")
print(lista)

#Traduceti propozitia introdusa de la tastatura
dictionar={
    "mama":"mother",
    "tata":"father",
    "copil":"child",
    "se":"are",
    "plimba":"walking",
    "prin":"in the",
    "parc":"park",
    "si":"and"
}
propozitie="mama copil si tata se plimba prin parc"
cuvinte=propozitie.split(" ")
for element in cuvinte:
    if(element in dictionar):
        print(dictionar.get(element))
    else:
        print(element)

#cum evitam problema cu virgula ? 
#de exemplu mama, tata si copilul se plimba in parc 
propozitie="mama, copil si tata se plimba prin parc"
cuvinte=propozitie.split(" ")
print(cuvinte)
for element in cuvinte:
    element=element.replace(",","")
    if(element in dictionar):
        print(dictionar.get(element))
    else:
        print(element)

# #inlocuiti toate succesiunile de litere "ma" cu "ta"
sir="mama si tata merg la plimbare"
sir=sir.replace("ma","ta")
print(sir)

#verificati daca sirul de caractere "Mihai" se gaseste in alt sir de caractere 
sir="si Mihai si Valentin si Raul merg pe strada"
if(sir.find("Mihai")!=-1):
    print("Se gaseste in sir")
else:
    print("Nu se gaseste in sir")

# afisati cea mai frecventa litera din versurile: 
versuri=""" pune versurile tale aici"""

versuri=versuri.replace(" ","")
frecvente={}
for litera in versuri: 
    if(litera in frecvente):
        frecvente[litera]+=1
    else:
        frecvente[litera]=1
maxim=0
cheie=""
for valoare in frecvente:
    if(frecvente[valoare]>maxim):
        maxim=frecvente[valoare]
        cheie=valoare
print(cheie+" "+str(maxim))


# #calculati maximul din lista 
lista=[5,2,8,3]
      #0 1 2 3
maxim=0
for el in range(4):
    if(lista[el]>maxim):
        maxim=lista[el]

# WHILE

#Scrieti un program care afiseaza numerele de la 1 la 10 cu while:
numere=0
while(numere<10):
    numere+=1
    print(numere)
#Afisati primele 10 numere pare folosind un while 
numere=0
while(numere<20):
    if numere%2==0:
        print(numere)
    numere+=1

#varianta 2 
numere=0
while(numere<20):
    print(numere)
    numere+=2
# Afisati suma tuturor numerelor dintr-o lista folosind un while 
lista=[1,5,4,3,2,1,5]
      #1 2 3 4 5 6 7
numere=0
sum=0
while(numere<len(lista)):
    sum+=lista[numere]
    numere+=1
print(sum)
#Afisati numerele din lista de mai sus care sunt mai mari ca 3 folosind while 
pozitie=0
while(pozitie<len(lista)):
    if(lista[pozitie]>3):
        print(lista[pozitie])
    pozitie+=1
# Afisati fiecare caracter dintr-un string pe o linie folosind while 
sir="abcdrefadsa"
pozitie=0
while(pozitie<len(sir)):
    print(sir[pozitie])
    pozitie+=1
