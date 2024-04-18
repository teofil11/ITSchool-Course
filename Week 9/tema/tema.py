import csv
import json

def scrie_csv():
    '''Aceasta functie citeste de la tastatura
    informatii si le scrie intr-un fisier csv'''
    informatii = []
    nume = input("Introduceti numele: ")
    varsta = input("Introduceti varsta: ")
    oras = input("Introduceti orasul in care locuiti: ")
    informatii.append([nume,varsta,oras])
    with open('Week 9/tema/informatii.csv', 'w',newline='') as file:
        file.write("Nume,Varsta,Oras"+'\n')
        writer = csv.writer(file)
        writer.writerows(informatii)

# scrie_csv()


def scrie_in_csv():
    with open('Week 9/tema/informatii.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        nume = input("Introduceti numele: ")
        varsta = input("Introduceti varsta: ")
        oras = input("Introduceti orasul in care locuiti: ")
        writer.writerow([nume, varsta,oras])

# scrie_in_csv()

