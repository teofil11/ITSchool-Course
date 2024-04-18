#   2. Permiteti utilizatorului sa introduca parola de 3 ori. Dupa fiecare introducere a parolei verificati daca parola este corecta.
# Daca parola este corecta afisati acest lucru. In caz contrar, afisati: Parola gresita,
# Mai ai <3> incercari. Dupa ultima incercare, afisati "cont blocat".
# Parola trebuie sa contina o litera mare si un caracter special.




parola_corecta = "Qwerty*"
numar_incercari = 3
caractere_speciale = '!@#$%^&*()_+'
print("Parola trebuie sa contina o litera mare si un caracter special.")
print(f"Atentie! Ai doar {numar_incercari} incercari. Daca gresesti parola de {numar_incercari} ori contul se blocheaza")





# for incercari in range(numar_incercari):
#     parola_introdusa = input("Introdoceti parola: ")   
#     if parola_corecta == parola_introdusa:
#         print("Parola corecta")
#         break
#     else:
#         incercari_ramase = numar_incercari - incercari - 1
#         if incercari_ramase == 0:
#             print("Cont blocat")
#         else:
#             if any(caracter.isupper() for caracter in parola_introdusa) and any(caracter in caractere_speciale for caracter in parola_introdusa):
#                 print(f"Parola este gresita. Mai aveti {incercari_ramase} incercari")
#             else:
#                 print(f"Parola nu contine litere mari si caractere speciale. \nParola este gresita, mai aveti {incercari_ramase} incercari")











# for incercari in range(numar_incercari):
#     parola_introdusa = input("Introdoceti parola: ")
#     for caracter in parola_introdusa:
#         if caracter.isupper() and caracter in caractere_speciale:
#             break       
#     if parola_corecta == parola_introdusa and caracter.isupper and caracter in caractere_speciale:
#         print("Parola corecta")
#         break
#     else:
#         incercari_ramase = numar_incercari - incercari - 1
#         if incercari_ramase == 0:
#             print("Cont blocat")
#         else:
#             print(f"Parola este gresita sau nu respecta cerintele. Mai aveti {incercari_ramase} incercari")   
