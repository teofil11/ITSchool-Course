##################################################concepte importante##################################
#                                                                                                     #
#clasa vs obiect                                                                                      #
#atribute/variabile specifice clasei vs atribute/variabile specifice instantei(obiect)                #
#constructorul (functia __init__ ) care este prima functie care se apeleaza cand construim un obiect  #
#__str__ ne permite sa afisam ce vrem noi  cand dam print(obiect)                                     #
#######################################################################################################
#creati o clasa numita caine care sa fie goala 
#adaugati proprietatea animal=caine care sa fie specifica tuturor instantelor
#adaugati proprietatea rasa care sa fie specifica fiecarei instante a clasei 
#adaugati functia latra care sa printeze "ham ham"
#adaugati un constructor 
#adaugati un o functie care sa printeze clasa sub forma urmatoare: eu sunt un {animal}, din rasa {rasa} si latru asa: {latra}
class Caine():
    animal="caine"
    def latra(self):
        print("ham ham")
    def __init__(self,culoare,varsta):
        self.culoare=culoare
        self.varsta=varsta
    def __str__(self):
        return f"Cainele acesta are culoarea {self.culoare} si varsta {self.varsta}"
suier=Caine("alb",10)
fluier=Caine("negru",5)

# suier.latra()
# fluier.latra()
print(suier)



#creati o clasa numita om care sa aiba urmatoarele instance variables: nume, prenume, varsta 
#creati o metoda pentru a initializa clasa respectiva 
#creati o metoda numita salut care sa afiseze urmatorul text" "Salut! Eu sunt {nume}"
#cititi de la tastatura informatiile necesare pentru a instantia n oameni si adaugati-i intr-o lista
class Om():
    def __init__(self):
        try:
            self.nume=input("nume=")
        except:
            print("ceva nu a mers bine!")
    def saluta(self):
        print(f"Salut, eu sunt {self.nume}!")
    def __str__(self):
        return self.nume

lista=[]

# #adaug in lsita
# for i in range(5):
#     lista.append(Om())

# #saluta toata lumea
# for i in range(5):
#     lista[i].saluta()
    
#creati o clasa numita dreptunghi care sa aiba urmatoarele proprietati: lungime, latime 
#creati o functie numita arie care sa afiseze aria dreptunghiului (lungime* latime)
#creati o functie numita perimetru care afiseaza perimetrul dreptunghiului 2*(lungime+latime)

class Dreptunghi():
    def __init__(self,lungime,latime):
        self.lungime=lungime
        self.latime=latime
    def arie(self):
        return self.lungime*self.latime  
    def perimetru(self):
        return 2*(self.lungime+self.latime)

# patrat=Dreptunghi(2,2)
# print(f"Arie={patrat.arie()}, Perimetru={patrat.perimetru()}")

#creati o clasa numita ContBancar cu atributele balanta, numar_cont. 
#creati o metoda depune care adauga bani in cont 
#creati o metoda retrage care retrage bani din cont 
#creati o metoda interogare_sold
import random
class ContBancar():
    def genereaza_cont(self):
        cont="ROBTRLRONCRT"
        numar=random.randint(1000000000000,9999999999999)
        return cont+str(numar)

    def __init__(self):
        self.cont=self.genereaza_cont()
        self.balanta=int(input(f"Ce suma doriti sa introduceti in contul {self.cont}: "))
        
    def depunere(self,suma):
        self.balanta+=suma
    def retragere(self,suma):
        if(suma<=self.balanta):
            self.balanta-=suma
    def interogare(self):
        print(f"In contul {self.cont} mai sunt {self.balanta} RON")
# contulMeu=ContBancar()
# contulMeu.interogare()

#modificati clasa anterioara astfel incat sa nu ii mai dam soldul ca parametru 
#din __init__ vreau sa afiseze "Cati bani doriti sa depuneti in contul <ROBTRLRONCRT....>: 100" 
# rezolvata mai sus 


#creati o clasa numita banca care sa contina o lista conturi bancare 
#creati o metoda creeaza cont 
#creati o metoda sterge cont

class Banca():
    conturi=[]
    def adaugaCont(self):
        self.conturi.append(ContBancar())
    def interogareConturi(self):
        for cont in self.conturi:
            cont.interogare()
    def depunerePeBazaDeCont(self):
        numarCont=input("Introduceti cont:")
        exista=False
        for cont in self.conturi:
            if(cont.cont==numarCont):
                exista=True
                suma=int(input("Introduceti suma: "))
                cont.depunere(suma)
        if not exista:
            print('Contul introdus este invalid!')
    
    def inchideCont(self):
        numarCont=input("Introduceti cont:")
        exista=False
        for cont in self.conturi:
            print(cont)
            if(cont.cont==numarCont):
                exista=True
                self.conturi.remove(cont)
        if not exista:
            print("Contul introdus nu exista")


# BT=Banca()
# BT.adaugaCont()
# BT.adaugaCont()
# BT.interogareConturi()
# # BT.depunerePeBazaDeCont()
# BT.inchideCont()
# BT.interogareConturi()


#creati un meniu care sa permita apelarea functiilor din obiectul banca
##creati o functie care genereaza conturi in lei (ROBTRLRONCRT<nr de 13 cifre>)
##primul cont va fi ROBTRLEURCRT0000000000001 respectiv ROBTRLRONCRT0000000000001 (calculam lungimea numarului la care am ajuns si adaugam 0 pana ajungem la 13 caractere)
##programul continua de la ultimul cont ramas (salveaza in fisier pentru a retine conturile emise chiar si atunci cand programul se inchide )
##pentru numarul 1 trebuie sa facem padding la stanga cu 0 pentru a ajunge la 13 cifre 
