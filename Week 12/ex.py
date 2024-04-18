import csv
import json

PATH = 'Week 12/'


class A():
    def method(self):
        print('Din A')
class B(A):
    pass
class C(A):
    def method(self):
        print('Din C')
class D(B,C):
    pass

obiectD = D()
# obiectD.method()


class Vehicul():
    def __init__(self):
        self.viteza_maxima = 30
    def deplaseaza(self):
        print('Vehiculul se deplaseaza')

class Tricicleta():
    def __init__(self):
        self.coarne = True
    def deplaseaza(self):
        print('Tricicleta se deplaseaza')
    
class Bicicleta(Vehicul, Tricicleta):
    pass

bicicleta = Bicicleta()
# bicicleta.deplaseaza()


def porneste(vehicul):
    return vehicul.porneste()

class Masina():
    def __init__(self):
        self.viteza_maxima = 200
    def porneste(self):
        print("Masina porneste")

class Tir():
    def __init__(self):
        self.viteza_maxima = 110
    def porneste(self):
        print('Tirul porneste')

masina = Masina()
tir = Tir()

# masina.porneste()
# tir.porneste()



class Avion():
    def zboara(self):
        print("Avionul zboara")

class AvionPrivat(Avion):
    pass

class AvionComercial(Avion):
    pass

def metodaMea(obiect):
    obiect.zboara()


avionPrivat = AvionPrivat()
avionComercial = AvionComercial()

# metodaMea(avionComercial)
# metodaMea(avionPrivat)


# 1. Creati 3 clase Masina, Avion, Bicicleta si fiecare dintre ele sa aiba metoda misca(). (nu folositi mostenirea)



class Masina():
    def misca(self):
        print("Accelerez")

class Avion():
    def misca(self):
        print('Trag de maneta')

class Bicicleta():
    def misca(self):
        print('Pedalez')

def move(vehicul):
    vehicul.misca()

avion = Avion()
avion2 = Avion()
masina = Masina()
masina2 = Masina()
bicicleta = Bicicleta()
bicicleta2 = Bicicleta()

vehicle = [avion,avion2,masina,masina2,bicicleta,bicicleta2]

# for vehicul in vehicle:
#     vehicul.misca()


# 4. Creati o clasa fisier care sa aiba metoda citeste si sa afiseze continutul in format text si o metoda afiseaza a continutului fisierului


class Fisier():
    def __init__(self,nume_fisier,caleFisier):
        self.nume_fisier = nume_fisier
        self.caleFisier = caleFisier
    def citeste(self):
        with open(self.caleFisier + self.nume_fisier, 'r') as file:
            continut = file.read()
        return continut
    
# fisier = Fisier('text.txt', PATH)
# print(fisier.citeste())

class FisierJson(Fisier):
    def citeste(self):
        with open(self.caleFisier + self.nume_fisier, 'r') as file:
            continut = json.load(file)
        return continut

class FisierCsv(Fisier):
    def citeste(self):
        rows = []
        with open(self.caleFisier + self.nume_fisier, 'r') as file:
            continut = csv.reader(file)
            for row in continut:
                rows.append(row)
        return rows




class Persoana():
    def __init__(self,nume,varsta):
        self.nume = nume
        self.varsta = varsta
    def salut(self):
        print(f'Salut! eu sunt {self.nume} si am varsta {self.varsta}')

class Student(Persoana):
    def __init__(self,nume,varsta,an):
        super().__init__(nume, varsta)
        self.an = an
    def salut(self):
        print(f'Salut eu sunt {self.nume} si sunt in anul {self.an} de facultate')

class Angajat(Persoana):
    def __init__(self,nume,varsta,companie):
        super().__init__(nume, varsta)
        self.companie = companie
    def salut(self):
        print(f'Salut eu sunt {self.nume} si lucrez la {self.companie}')

class Intern(Angajat,Student):
    def __init__(self, nume, varsta, intership):
        self.intership = intership
    def salut(self):
        print('Salut')

student = Student('Ionica', 18,2)
angajat = Angajat('Ilie', 32,'ItSchool')
inter = Intern("nume", 21, "intership")

# student.salut()
# angajat.salut()
inter.salut()