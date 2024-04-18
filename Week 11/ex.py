import math

class Vehicul():
    zboara = False
    def porneste(self):
        print("Invarte cheia")

class Masina(Vehicul):
    pass

class Avion(Vehicul):
    zboara = True
    def porneste(self):
        super().porneste
        print("Apasa pe maneta")

ford = Vehicul()
vw = Vehicul()
beoing = Avion()

# print(ford.zboara)
# print(vw.zboara)
# print(beoing.zboara)


class Dreptunghi():
    toate_laturile_egale = False

class Patrat(Dreptunghi):
    toate_laturile_egale = True



class Avioane():
    zboara = True
    def __init__(self, viteza_minima, consum):
        self.viteza_minima = viteza_minima
        self.consum = consum
    def zboara(self):
        print("Zbor")

class AvionCivil(Avioane):
    nr_pasageri = 100
    def descarca_bagaje(self):
        print("Se descarca bagajele")

class AvionMilitar(Avioane):
    munitie = 10
    def lansator_rachete(self):
        print("Se lanseaza rachetele")


F15 = Avioane(1, 50)
# F15.zboara()


# Definiți o clasă numită Person care să aibă două atribute: nume și vârstă. Apoi creați o instanță a clasei Person și afișați valorile atributelor

class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

person = Person('Jhon', 30)
# print(person.name)
# print(person.age)


class Circle():
    def __init__(self,raza):
        self.raza = raza
    
    def aria_cercului(self):
        return math.pi * self.raza ** 2

cerc = Circle(8)
# print(cerc.aria_cercului())


class Animal():
    def vorbeste(self):
        pass

    def mananca(self):
        pass

class Caine(Animal):
    def vorbeste(self):
        print('Ham Ham')
    def mananca(self):
        print('Oase')

class Pisica(Animal):
    def vorbeste(self):
        print('Miau Miau')
    def mananca(self):
        print('Peste')

tom = Pisica()
rex = Caine()

# tom.mananca()
# tom.vorbeste()
# rex.mananca()
# rex.vorbeste()



