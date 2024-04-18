import os
import json
import csv
PATH = 'Week 11/curs20/'

class Fisier():
    def __init__(self,nume,dimensiune,tip,cale):
        self.nume=nume
        self.dimensiune=dimensiune
        self.tip=tip
        self.cale=cale

class FisierCsv(Fisier):
    def __init__(self,nume,dimensiune,tip,cale):
        super().__init__(nume,dimensiune,tip,cale)
        self.coloane=0
        self.randuri=0
        self.lines=[]
        with open(self.cale+self.nume,'r') as file:
            reader=csv.reader(file)
            for line in reader:
                self.lines.append(line)
        
    def scrie_csv(self,outputPath):
        with open(outputPath,"w",newline='') as file:
            writer=csv.writer(file)
            writer.writerows(self.lines)


    def scrie_json(self,outputName):
        jsonArray=[]
        for line in self.lines:
            jsonArray.append({
                "id":line[0],
                "name":line[1],
                "salary":line[2],
                "position":line[3]
            })
        with open(self.cale+outputName,'w') as file:
            json.dump(jsonArray,file)

class FisierJson(Fisier):
    def __init__(self,nume,dimensiune,tip,cale):
        super().__init__(nume,dimensiune,tip,cale)
        with open(self.cale+self.nume,'r') as file:
            self.continut=json.load(file)

    def scrie_json(self,outputFile):
        with open(self.cale+outputFile,'w') as file:
            json.dump(self.continut,file)

    def scrie_csv(self,outputFile):
        lines=[]
        for obiect in self.continut:
            lines.append([obiect['id'],obiect['name'],obiect['position'],obiect['salary']])
        with open(self.cale+outputFile,"w",newline='') as file:
            writer=csv.writer(file)
            writer.writerows(lines)


class Folder():
    def __init__(self,caleFolder):
        self.jsoane = []
        self.csvuri = []
        self.fisiere = []
        for fisier in os.listdir(caleFolder):
            type = fisier.split('.')[1]
            size = os.path.getsize(caleFolder)
            if type == 'json':
                fisierJson = FisierJson(fisier, size, 'json', caleFolder)
                self.jsoane.append(fisierJson)
            elif type == 'csv':
                fisierCsv = FisierCsv(fisier, size, "csv", caleFolder)
                self.csvuri.append(fisierCsv)
            else:
                fisier = Fisier(fisier, size, type, caleFolder)
                self.fisiere.append(fisier)
    def numara_fisiere(self):
        print(f'Numar Json: {len(self.jsoane)}')
        print(f'Numar Csv: {len(self.csvuri)}')
        print(f'Numar alte fisiere: {len(self.fisiere)}')
    
    def afiseaza_fisiere(self,caleFolder):
        fisiere = os.listdir(caleFolder)
        for fisier in fisiere:
            print(fisier)

    def sterge_fisier(self,nume_fisier,caleFolder):
        try:
            os.remove(os.path.join(caleFolder,nume_fisier))
        except FileNotFoundError:
            print("Fisierul nu exista")
    
folder = Folder(PATH)
# folder.afiseaza_fisiere(PATH)
folder.sterge_fisier("nume_fisier", PATH)



# 2. Definiți o clasă părinte Animal cu o metodă move() și o clasă copil Cat care moștenește această metodă și își adaugă propria funcționalitate.
#  Apoi creați un obiect Cat și apelați metoda move().

class Animal():
    def __init__(self,rasa,culoare,varsta):
        self.rasa = rasa
        self.culoare = culoare
        self.varsta = varsta
    def move(self):
        print('Pas')

class Cat(Animal):
    def __init__(self, rasa, culoare, varsta):
        super().__init__(rasa, culoare, varsta)
    def toarce(self):
        print("Brrrrr")
    def miauna(self):
        print('Miau')


tom = Cat("persana", "gri", 2)
# tom.move()
# tom.toarce()



# 3. Creați o clasă părinte Vehicle cu o metodă drive() și o clasă copil Car care moștenește această metodă și își adaugă propria funcționalitate.
#  Apoi creați un obiect Car și apelați metoda drive().

class Vehicle():
    def __init__(self,culoare,an,):
        self.culoare = culoare
        self.an = an
    def drive(self):
        print('Drive the vehicle')

class Car(Vehicle):
    def __init__(self,marca,culoare,an,putere):
        super().__init__(culoare, an)
        self.marca = marca
        self.putere = putere
        self.an = an
    def drive(self):
        print('Drive the car')
    def accelereaza(self):
        print('Vrooooom')

myCar = Car('Bmw', "Negru", 2007, 163)
# myCar.drive()
# myCar.accelereaza()



# 4. Definiți o clasă părinte Shape cu o metodă area() și o clasă copil Rectangle care moștenește această metodă și își adaugă propria funcționalitate.
#  Apoi creați un obiect Rectangle și apelați metoda area()

class Shape():
    def __init__(self,nr_laturi):
        self.nr_laturi = nr_laturi
    def area(self):
        self.lungime_laturi = []
        for latura in range(self.nr_laturi):
            lungime = int(input("Introduceti lungimea laturii: "))
            self.lungime_laturi.append(lungime)
        print('Se calculeaza aria')
        

class Rectangle(Shape):
    def __init__(self,lungime,latime,nr_laturi):
        super().__init__(nr_laturi)
        self.lungime = lungime
        self.latime = latime
    def area(self):
        print(f'Aria dreptunghiului esre {self.lungime * self.latime}')

    def perimeter(self):
        print(f'Perimetrul dreptunghiului este {2*self.lungime + 2*self.latime}')
        

    
    


x = Rectangle(10, 5, 4)
# x.area()
