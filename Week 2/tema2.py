# 1.   Cititi de la tastatura si afisati numele si varsta utilizatorului: <Nume> are <20> de ani.

# nume = input("Care este numele tau? ")
# varsta = input("Cati ani ai? ")
# print(f"{nume} are {varsta} de ani")






# # 2.   Cititi de la tastatura un nume. Daca este numele vostru afisati "Da, eu sunt" daca nu, afisati "Nu sunt eu".

# nume = input("Care este numele tau ?")
# if nume == "Teo":
#     print("Da, eu sunt")
# else:
#     print("Nu sunt eu")





# # 3.   Hardcodati(declarati intr-o variabila) o parola si apoi cereti ca utilizatorul sa o introduca de la tastatura.
# #  Verificati daca parola este corecta. 

# parola = "123qwerty"
# p = input("Care este parola? ")

# if parola == p:
#     print("Parola este corecta")
# else:
#     print("Parola este gresita")






# 4.   Permiteti utilizatorului sa introduca parola de 3 ori. Dupa fiecare introducere a parolei verificati daca parola este corecta. Daca parola
# este corecta afisati acest lucru. In caz contrar, afisati: Parola gresita, Mai ai <3> incercari. Dupa ultima incercare, afisati "cont blocat".

# parola = "qwerty"
# p = input("Care este parola? ")

# if parola == p:
#     print("Parola este corecta")
# else:
#     p = input("Parola este gresita, mai ai <3> incercari ")
#     if parola == p:
#         print("Parola este corecta")
#     else:
#         p = input("Parola este gresita, mai ai <2> incercari ")
#         if parola == p:
#             print("Parola este corecta")
#         else:
#             p = input("Parola este gresita, mai ai doar o incercare ")
#             if parola == p:
#                 print("Parola este corecta")
#             else:
#                 print("Cont blocat")



# 5.   Cititi un numar de la tastatura si verificati daca acesta e par

# nr = int(input("Introduceti un numar: "))
# if nr%2 == 0:
#     print(f"numarul {nr} este par")
# else:
#     print(f"numarul {nr} nu este par")



# 6.   Cititi un numar de la tastatura si verificati daca acesta e impar

# nr = int(input("Introduceti un numar: "))
# if nr%2 != 0:
#     print(f"numarul {nr} este impar")
# else:
#     print(f"numarul {nr} este par")



# 7.   Cititi un numar de la tastatura si verificati daca acesta e divizibil cu 5 (restul impartirii cu 5 este 0) 

# nr = int(input("Introduceti un numar: "))
# if nr%5 == 0:
#     print(f"Numarul {nr} este divizibl cu 5")
# else:
#     print(f"Numarul {nr} nu este divizibil cu 5")



# 8.   Cititi un numar de la tastatura si verificati daca acesta are ultima cifra 4

# nr = int(input("Introduceti un numar: "))
# if nr%10 == 4:
#     print(f"Ultima cifra a numarului {nr} este 4")
# else:
#     print(f"Ultima cifra a numarului {nr} nu este 4") 




# 9.   Cititi un numar de la tastatura si verificati daca acesta e divizibil cu ultima cifra a sa. Exemplu: 15423 e divizibil cu 3.

# nr = int(input("Introduceti un numar: "))
# nr2 = nr%10
# if nr%nr2 == 0:
#     print(f"Numarul {nr} este divizibil cu numarul {nr2}")
# else:
#     print(f"Numarul {nr} nu este divizibil cu numarul {nr2}")



# 10.  Cititi un numar de la tastatura si verificati daca acesta se afla in intervalul 10 100

# nr = int(input("Introduceti un numar: "))
# if 10<= nr <=100:
#     print(f"Numarul {nr} se afla in intervalul 10 - 100")
# else:
#     print(f"Numarul {nr} nu se afla in intervalul 10 - 100")




# 11.  Cititi un numar de la tastatura si verificati daca acesta e mai mic decat 70

# nr = int(input("Introduceti un numar: "))
# if nr < 70:
#     print(f"Numarul {nr} este mai mic decat 70")
# else:
#     print(f"Numarul {nr} este mai mare sau egal cu 70")



# 12.  Cititi doua numere de la tastatura a si b. Implementati in python codul pentru urmatorul pseudocod: 
#     daca b>a
#         b=b-a 
#     altfel 
#         a=a-b

# a = int(input("Introduceti un numar: "))
# b = int(input("Introduceti alt numar: "))
# if b>a:
#     b = b-a
# else:
#     a = a-b
# print(a, b)



# 13.

# buget = int(input("Care este bugetul? "))
# schimbareBara = 1500
# schimbareUlei = 1000
# revizie = 700
# rovigneta = 100
# rca = 800

# if buget >= schimbareBara:
#     buget = buget - schimbareBara
#     print(f"Am schimbat bara si ne-au ramas {buget} lei.")
# else:
#     print("Bugetul nu poate acoperi schimbarea barii")

# if buget >= schimbareUlei:
#     buget = buget - schimbareUlei
#     print(f"Am schimbat uleiul si ne-au ramas {buget} lei")
# else:
#     print("Bugetul nu poate acoperi schimbarea uleiului ")

# if buget >= revizie:
#     buget = buget - revizie
#     print(f"Am facut revizia si ne-au ramas {buget} lei")
# else:
#     print("Bugetul nu poate acoperi revizia")

# if buget >= rovigneta:
#     buget = buget - rovigneta
#     print(f"Am facut rovignieta si ne-au ramas {buget} lei")
# else:
#     print("Bugetul nu poate acoperi rovignieta")

# if buget >= rca:
#     buget = buget - rca
#     print(f"Am facur rca-ul si ne-au ramas {buget} lei")
# else:
#     print("Bugetul nu poate acoperi rca-ul")

