import matplotlib.pyplot as plt

# 1. Create a class called Circle that has attributes radius and color. Add methods to calculate the area and circumference of the circle.

pi = 3.14

class Circle():
    def __init__(self, raza, culoare):
        self.radius = raza
        self.color = culoare
    
    def arie(self):
        arie = pi*self.radius**2
        return arie
    
    def plot(self):
        figure, axes = plt.subplots()
        Drawing_colored_circle = plt.Circle(( 0.6 , 0.6 ), self.radius )
 
        axes.set_aspect(1)
        axes.add_artist( Drawing_colored_circle )
        plt.title( 'Colored Circle' )
        plt.show()

# cerc = Circle(0.3,'Verde')
# print(cerc.arie())
# cerc.plot()


# 2.Create a class called Rectangle that has attributes width and height. Add methods to calculate the area and perimeter of the rectangle.


class Patrulater():
    def __init__(self,latime,lungime):
        self.lungime = lungime
        self.latime = latime
        
    def area(self):
        pass

    def perimetru(self):
        pass





class Rectangle(Patrulater):
    def __init__(self, latime, lungime):
        super().__init__(latime, lungime)

    def area(self):
        area = self.lungime * self. latime
        print(area)
    
    def perimetru(self):
        perimetru = self.lungime*2 + self.latime*2
        print(perimetru)


# dreptunghi = Rectangle(5,9)
# dreptunghi.area()
# dreptunghi.perimetru()


# 3. Create a class called BankAccount that has attributes account_number and balance. Add methods to deposit and withdraw money from the account.

class BankAccount():
    def __init__(self,account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self):
        money = int(input('amount of money: '))
        self.balance += money
        print(self.balance)
    
    def withdraw(self):
        money = int(input('amount of money: '))
        if self.balance >= money:
            self.balance -= money
        else:
            print('insufficient balance')
        print(self.balance)

# cont = BankAccount(1,500)
# cont.deposit()
# cont.withdraw()


# 4. Create a class called Employee that has attributes name, position, and salary. Add a method to give a raise to the employee.

class Employee():
    def __init__(self,name,position,salary):
        self.name = name
        self.position = position
        self.salary = salary
    def salary_increase(self,amount_of_money):
        self.salary += amount_of_money
        print(self.salary)

# x = Employee('Teo','Manager',3000)
# print(x.salary)
# x.salary_increase(500)
        
# 4. Create a base class called Animal with attributes name and age. Create subclasses Dog and Cat that inherit from Animal and add specific attributes and methods.

class Animal():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def sound(self):
        raise NotImplementedError('metoda trebuie implementata')

class Dog(Animal):
    def __init__(self, name, age,species):
        super().__init__(name, age)
        self.species = species

    def sound(self):
        print('Ham,Ham')

class Cat(Animal):
    def __init__(self, name, age,species):
        super().__init__(name, age)
        self.species = species

    def sound(self):
        print('Miau')

# pisica = Cat('Petrica',2,'asdas')
# pisica.sound()


# 5.

class Angajati():
    def __init__(self,nume,prenume,salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu
        
    def calcul_salariu(self):
        pass

class Full_time(Angajati):
    def __init__(self, nume, prenume, salariu,valoare_bonuri,numar_bonuri):
        super().__init__(nume, prenume, salariu)
        self.valoare_bonuri = valoare_bonuri
        self.numar_bonuri = numar_bonuri
    
    def calcul_salariu(self):
        total = self.salariu + (self.valoare_bonuri * self.numar_bonuri)
        print(total)
    

class Part_time(Angajati):
    def __init__(self, nume, prenume, salariu):
        super().__init__(nume, prenume, salariu)
    
    def calcul_salariu(self):
        total = self.salariu
        print(total)

# x = Full_time('Popescu','Matei', 5000, 30, 10)
# y = Part_time('Grigore', 'George',2000)

# lista = [x,y]

# for angajat in lista:
#     angajat.calcul_salariu()


#6

class String():
    def __init__(self, value):
        self.value = value

    def is_lower(self):
        litere_mici = 'abcdefghijklmnopqrstuvxyz'
        e_mic = True
        for litera in self.value:
            if litera not in litere_mici:
                e_mic = False
        
        return e_mic

    def is_upper(self):
        litere_mari = 'ABCDEFGHIJKLMNOPQRSTUVXYZ'
        e_mare = True
        for litera in self.value:
            if litera not in litere_mari:
                e_mare = False
        
        return e_mare

    def split(self,char):
        cuvinte = []
        cuvant_curent = ''
        for el in self.value:
            if el != char:
                cuvant_curent += el
            else:
                cuvinte.append(cuvant_curent)
                cuvant_curent = ''
        
        return cuvinte
    

# 7

class D:
    def func(self):
        print('Din D')

class C(D):
    def func(self):
        print('Din C')

class B(D):
    def func(self):
        print('Din B')

class A(B,C):
    def func(self):
        print('Din A')


# print(A.mro())

class A:
    def func(self):
        print('Din A')

class B(A):
    def func(self):
        print('Din B')

class C(A):
    def func(self):
        print('Din C')

class D(C,B):
    def func(self):
        print('Din D')

# print(D.__mro__)