import random

class Caine():
    animal = 'caine'
    culoare = 'alb'
    varsta = 10
    def latra(self):
        print('ham ham')
    def se_joaca(self):
        print('ham ham')
    def __init__(self,culoare,varsta):
        self.culoare = culoare
        self.varsta = varsta


class Om():
    def __init__(self):
        try:
            self.nume = input('Nume: ')

        except:
            print('Ceva nu a mers bine')
    def salut(self):
        print(f'Salut, eu sunt {self.nume}')

# persoana = Om('Teodorescu', 'Teofil', 22) 
# persoana.salut()
# lista = []

# for i in range(5):
#     lista.append(Om())

# for i in range(5):
#     lista[i].salut()


class dreptunghi():
    def __init__(self,lungime,latime):
        self.lungime = lungime
        self.latime = latime
    def arie(self):
        print(self.lungime * self.latime)
    def perimetru(self):
        print(2 * (self.lungime + self.latime))

# dreptunghi(10, 8).arie()


class ContBancar():
    def genereazaCont(self):
        cont = 'ROBTRLRONCRT'
        numar = random.randint(1000000000, 9999999999)
        return cont+str(numar)

    def __init__(self):
        self.cont = self.genereazaCont()
        self.balanta = int(input(f'Ce suma doriti sa depuneti in contul {self.cont}: '))
    def depune(self):
        suma_depusa = int(input(f'Suma de bani pe care vreti sa o depuneti in contul {self.cont}: '))
        self.balanta += suma_depusa
    def retragere(self):
        suma_retrasa = int(input('Suma de bani pe care vreti sa o retrageti din cont: '))
        self.balanta -= suma_retrasa
    def interogare(self):
        print(f'In contul {self.cont} mai sunt {self.balanta} ron')    

# contul_meu = ContBancar()
# contul_meu.interogare()

class Banca():
    conturi = []
    def creeaza_cont(self):
        self.conturi.append(ContBancar())
    def info_conturi(self):
        for cont in self.conturi:
            cont.interogare()
    def depunerePeBazaDeCont(self):
        numar_cont = input("Introduceti cont: ")
        for cont in self.conturi:
            if cont.cont == numar_cont:
                suma = int(input("Introduceti suma: "))
                cont.depune()
    def inchide_cont(self):
        numar_cont = input('Introduceti contul: ')
        exista = False
        for cont in self.conturi:
            if cont.cont == numar_cont:
                exista = True
                self.conturi.remove(cont)
            if not exista:
                print('Contul introdus nu exista')


# BT = Banca()
# BT.creeaza_cont()
# BT.creeaza_cont()
# BT.info_conturi()
# BT.depunerePeBazaDeCont()
# BT.inchide_cont()
# BT.info_conturi()