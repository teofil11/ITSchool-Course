# x=[15,2,4,123]#list #https://www.w3schools.com/python/python_lists.asp
# y=(145,2,3,120)#tuple #https://www.w3schools.com/python/python_tuples.asp
# z={123,159,100}#set #https://www.w3schools.com/python/python_sets.asp

#Verificati ca parola introdusa de la tastatura incepe cu litera mare si se termina cu un caracter special 
# litereMariDeTipar='ABCDEFGHIJKLMNOPQRSTUVXYZ'
# caracterSpeciale='!@#$%^&*()_+'
# parola=input("Introduceti parola: ") #ItSchool*
# lungimeParola=len(parola)
# if parola[0] in litereMariDeTipar and parola[-1] in caracterSpeciale:
#     print("Parola corecta!")
# else:
#     print("Paroa nu respecta conditia")

#Afisati cat costa fiecare produs din meniu stiind urmatoarele valori: 
# produse=['Ciorba','Tocanita','Desert']
# preturi=[20,25,15]
# buget=int(input("Introduceti bugetul: "))
# print(buget)
# #Am cumparat o <ciorba> care a costat <x> lei si mi-au ramas <z> lei. 
# buget=buget-preturi[0]
# if(buget>0):
#     print(f"Am cumparat o {produse[0]} care a costat {preturi[0]} si mi-au ramas {buget} lei")
# else:
#     print(f"Nu am avut suficienti bani pentru {produse[0]}")
# buget=buget-preturi[1]
# if(buget>0):
#     print(f"Am cumparat o {produse[1]} care a costat {preturi[1]} si mi-au ramas {buget} lei")
# else:
#     print(f"Nu am avut suficienti bani pentru {produse[1]}")
# buget=buget-preturi[2]
# if(buget>0):
#     print(f"Am cumparat un {produse[2]} care a costat {preturi[2]} si mi-au ramas {buget} lei")
# else: 
#     print(f"Nu am avut suficienti bani pentru {produse[2]}")

#Verificati daca un numar scris de la coada la cap este la fel cu numarul scris de la cap la coada ("131,2332,1221")
#131
# x="134"
# if x==x[::-1]:
#     print("sunt egale")
# else:
#     print("nu sunt egale ")

#Verificati ca numarul scris sub forma unui sir de caractere este divizibil cu ultima lui cifra 
# x="22" 
# xint=int(x)
# ultimaCifra=int(x[-1])
# print(xint%ultimaCifra==0)

# #Verificati ca un sir de caractere contine doar litere mici 
# x=input("Introduceti un sir de caractere: ")
# print(x.islower())

# #Verificati ca un sir de caractere contine doar litere mari
# x=input("Introduceti un sir de caractere: ")
# print(x.isupper())

# #Transformati toate caracterele in litere mari
# x=input("Introduceti un sir de caractere: ")
# print(x.upper())

# #Transformati toate caracterele in litere mici
# x=input("Introduceti un sir de caractere: ")
# print(x.lower())

#Verificati ca un fisier este de tip text (are extensia txt)
# input.txt
# fisier.txt
# fisier.TXT
# numeFisier=input()
# extensie=numeFisier[-3:]
# if(extensie.lower()=="txt"):
#     print("Fisierul este de tip text")
# else: 
#     print("Fisierul nu este de tip text")

#Afisati daca un sir de caractere incepe cu o cifra
# nr=input("Introduceti un numar de la tastatura: ")
# cifre="0123456789"
# if(nr[0] in cifre):
#     print("Incepe cu o cifra")


##FOR 
#Verifica daca un caracter din sir este cifra 
# nr="1sad"
# listaCifre="0123456789"
# for caracter in nr:
#     if(caracter in listaCifre):
#         print(f"Caracterul {caracter} este cifra")
#     else:
#         print(f"Caracterul {caracter} nu este cifra")