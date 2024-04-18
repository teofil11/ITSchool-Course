# class Vehicul():
#     zboara=False
#     def set_zboara(self,value):
#         self.zboara=value
#     def accelereaza(self):
#         print("pazea ca vin")

# class Masina(Vehicul):
#     def set_zb(self,zboara):
#         super().set_zboara(zboara)
#     def accelereaza(self):
#         super().accelereaza()
#         print("vine masina titit")

# class Avion(Vehicul):
#     zboara=True
#     def accelereaza(self):
#         super().accelereaza()
#         print("niuuuuuu")

# vehicul=Vehicul()
# masina=Masina()
# avion=Avion()

# print(masina.zboara)
# masina.set_zb(True)
# print(masina.zboara)

# vehicul.accelereaza()
# masina.accelereaza()
# avion.accelereaza()




#mostenire: parinte si copil 
#suprascriere 

class Vehicul():
    zboara=False
    def porneste(self):
        print("Invarte cheia!")
class Masina(Vehicul):
    pass 

class Avion(Vehicul):
    zboara=True
    def porneste(self):
        super().porneste()
        print("Apasa pe maneta")

ford=Vehicul()
vw=Masina()
beoing=Avion()

# print(ford.zboara)
# print(vw.zboara)
# print(beoing.zboara)

# beoing.porneste()
# ford.porneste()
# vw.porneste()


#Creati o clasa dreptunghi si o clasa patrat. Clasa patrat sa mosteneasca clasa dreptunghi. Patrat va avea in plus o valoare booleana patrat=True 

class Dreptunghi:
    def __init__(self, lungime, latime):
        self.lungime = lungime
        self.latime = latime

class Patrat(Dreptunghi):
    def __init__(self, latura):
        super().init(latura, latura)
        self.patrat = True

dreptunghi=Dreptunghi(2,3)

#Creati o clasa Avion. Din clasa Avion, creati 2 clase: AvionMilitar, AvionCivil. Atat avionul militar cat si cel civil au urmatoarele proprrietati: 
#Ambele zboara
#Ambele au viteza minima zbor 
#Ambele au un consum de combustibil 

#Avionul civil are un numar de pasageri 
#Avionul descarca bagaje 

#Avionul militar poate lansa rachete in timp ce zboara (suprascriere)
#Avionul militar are cantitate munitie (int tone) 

class Avion:
    def __init__(self, viteza_minima, consum_combustibil):
        self.viteza_minima = viteza_minima
        self.consum_combustibil = consum_combustibil

    def zboara(self):
        print("Avionul zboara")

class AvionMilitar(Avion):
    def __init__(self, viteza_minima, consum_combustibil, cantitate_munitie):
        super().__init__(viteza_minima, consum_combustibil)
        self.cantitate_munitie = cantitate_munitie

    def lanseaza_racheta(self):
        print("Avionul militar lanseaza rachete")

# F16 = AvionMilitar(1, 50, 10)
# F16.lanseaza_racheta()

#Creati clasa Fisier cu urmatorii parametri: 
#nume 
#dimensiune 
#tip 
#cale 

#creati clasa FisierCsv care sa contina pe langa parametrii Fisier si urmatoarele:
#Numar coloane 
#Numar randuri 
#CitireFisier csv
#ScriereFisier csv 

#creati clasa FisierJson: fisierele citite vor contine array-uri. 
#Vrem sa cream o lista de obiecte din acele array-uri.
#CitireFisier json
#ScriereFisier json
PATH='Week 11/curs20/'
import csv
import json

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
    



# employees=FisierCsv('employees.csv',10,'csv',PATH)
# employees.scrie_json("test.json")

# employees.citire_fisier()
# employees.scrie_csv("curs20/test.csv")

# employees=FisierJson("employees.json",10,'json',PATH)
# employees.scrie_json("test2.json")
# employees.scrie_csv("test2.csv")


#Creati o clasa folder care sa citeasca automat intr-un obiect toate fisierele dintr-un folder. 
#Fisierele vor fi salvate ca obiecte in interiorul clasei Folder 
import os
class Folder():
    def __init__(self,caleFolder):
        self.jsoane=[]
        self.csvuri=[]
        self.fisiere=[]
        for fisier in os.listdir(caleFolder):
            type=fisier.split(".")[1]
            size=os.path.getsize(caleFolder+fisier)
            if(type=="json"):
                fisierJson=FisierJson(fisier,size,"json",caleFolder)
                self.jsoane.append(fisierJson)
            elif(type=="csv"):
                fisierCsv=FisierCsv(fisier,size,"csv",caleFolder)
                self.csvuri.append(fisierCsv)
            else:
                fisier=Fisier(fisier,size,type,caleFolder)
                self.fisiere.append(fisier)
    def numara_fisiere(self):
        print("Numar json: "+str(len(self.jsoane)))
        print("Numar csv : "+str(len(self.csvuri)))
        print("Numar alte fisiere : "+str(len(self.fisiere)))
        print("TOTAL: "+str( len(self.jsoane)+len(self.csvuri)+len(self.fisiere)))

# folder=Folder(PATH)
# folder.numara_fisiere()
