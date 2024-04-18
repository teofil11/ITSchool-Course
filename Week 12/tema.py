class Forma():
    def aria(self):
        pass

class Dreptunghi(Forma):
    def __init__(self,lungime,latime):
        self.lungime = lungime
        self.latime = latime
    def aria(self):
        return self.lungime * self.latime

class Cerc(Forma):
    def __init__(self,raza_cercului):
        self.raza_cercului = raza_cercului
    def aria(self):
        return 3.14 * self.raza_cercului

d = Dreptunghi(10, 7)
c = Cerc(6)
forme = []
forme.append(d)
forme.append(c)

# for forma in forme:
#     print(forma.aria())



class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f'Salut numele meu este {self.name} si am {self.age} ani')

class Employee():
    def __init__(self,salary):  
        self.salary = salary
     
    def calculate_salary(self,hours):
        print(hours * self.salary)

class Manager(Person,Employee):
    def __init__(self,name,age,salary):
        Person.__init__(self, name, age)
        Employee.__init__(self, salary)

    def introduce(self):
        print(f'Salut numele meu este {self.name} si sunt manager')
    def pay_salary(self,employee,hours):
        employee.calculate_salary(hours)     
        
        

    
manager = Manager('Ion', 37, 30)
employee = Employee(16)

# employee.calculate_salary(140)
# manager.calculate_salary(140)
# manager.pay_salary(employee, 140)




    


