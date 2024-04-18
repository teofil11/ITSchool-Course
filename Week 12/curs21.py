#problema diamant 
class A(): 
    def method(self):
        print("Din A")

class B(A): 
    pass 

class C(A):
    pass

class D(B,C):
    pass


obiectD=D()
obiectD.method()

#creati o clasa bicicleta care mosteneste o clasa vehicul si o clasa tricicleta
#polimorfism folosind o functie 
def metodaMea(vehicul):
    return vehicul.deplaseaza()

class Vehicul():
    def __init__(self):
        self.viteza_maxima=30
    def deplaseaza(self):
        print("Vehiculul se deplaseaza")

class Tricicleta():
    def __init__(self):
        self.coarne=True
    def deplaseaza(self):
        print("Tricicleta se deplaseaza")

vehicul=Vehicul()
tricileta=Tricicleta()

metodaMea(vehicul)
metodaMea(tricileta)


#polimorfism folosind mostenire 
class Vehicul():
    def deplaseaza(self):
        print("Vehiculul se deplaseaza")

class MasinaDeFamilie(Vehicul):
    pass

class MasinaDeMunca(Vehicul):
    pass

ford=MasinaDeFamilie()
docker=MasinaDeMunca()
def metodaVoastra(obiect):
    obiect.deplaseaza()

metodaVoastra(ford)
metodaVoastra(docker)


lista=[ford,docker]
for masina in lista:
    masina.deplaseaza()



#rescrieti problemele de la cursul 20 folosind polimorfism 
PATH='curs20/'
import csv 
import json

class Fisier():
    def __init__(self,nume,dimensiune,tip,cale):
        self.nume=nume
        self.dimensiune=dimensiune
        self.tip=tip
        self.cale=cale
    def scrie_alt_format(self,filename):
        pass
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
        
    def scrie(self,outputPath):
        with open(outputPath,"w",newline='') as file:
            writer=csv.writer(file)
            writer.writerows(self.lines)


    def scrie_alt_format(self,outputName):
        print("csv in alt format")
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

    def scrie(self,outputFile):
        with open(self.cale+outputFile,'w') as file:
            json.dump(self.continut,file)

    def scrie_alt_format(self,outputFile):
        print("json in alt format")
        lines=[]
        for obiect in self.continut:
            lines.append([obiect['id'],obiect['name'],obiect['position'],obiect['salary']])
        with open(self.cale+outputFile,"w",newline='') as file:
            writer=csv.writer(file)
            writer.writerows(lines)
    

import os
class Folder():
    def __init__(self,caleFolder):
        self.toateFisierele=[]
        for fisier in os.listdir(caleFolder):
            type=fisier.split(".")[1]
            size=os.path.getsize(caleFolder+fisier)
            if(type=="json"):
                fisierJson=FisierJson(fisier,size,"json",caleFolder)
                self.toateFisierele.append(fisierJson)
            elif(type=="csv"):
                fisierCsv=FisierCsv(fisier,size,"csv",caleFolder)
                self.toateFisierele.append(fisierCsv)
            else:
                fisier=Fisier(fisier,size,type,caleFolder)
                self.toateFisierele.append(fisier)
    def numara_fisiere(self):
        print("Numar fisiere : "+str(len(self.toateFisierele)))

    def sterge_fisier(self,nume_fisier):
        for fisier in [self.toateFisierele]:
            if(nume_fisier==fisier.nume):
                self.toateFisierele.remove(fisier)
  
        os.remove(PATH+nume_fisier)

    def scrie_fisiere_alt_format(self,fileName):
        for fisier in self.toateFisierele:
            fisier.scrie_alt_format(fileName)

# myFolder=Folder("curs20/")
# myFolder.scrie_fisiere_alt_format("output.csv")

# 4. Creati o clasa fisier care sa aiba metoda citeste si sa afiseze continutul in format text si o metoda afiseaza a continutului fisierului

import pandas
class Fisier():
    def __init__(self,numeFisier,caleFisier):
        self.numeFisier = numeFisier
        self.caleFisier = caleFisier
    def citeste(self):
        with open(self.caleFisier+self.numeFisier,"r") as fisier:
            continut=fisier.read()
        return continut 
    
# fisier=Fisier("employees.csv","curs20/")
# print(fisier.citeste())

# 5. Creati o clasa json care mosteneste clasa fisier si suprascrie metoda citeste pentru a returna un json (dictionar)
class FisierJson(Fisier):
    def citeste(self):
        with open(self.caleFisier+self.numeFisier,"r") as fisier:
            continut=json.load(fisier)
        return continut
# 6. Creati o clasa csv care mosteneste calsa fisier si suprascrie metda citeste pentru a returna un obiect 
class FisierCsv(Fisier):
    def citeste(self):
        rows=[]
        df=pandas.read_csv(self.caleFisier+self.numeFisier)
        print(df)
        # with open(self.caleFisier+self.numeFisier,"r") as fisier:
        #     continut=csv.reader(fisier)
        #     for row in continut:
        #         rows.append(row)
        return rows
    
# jsonAngajati=FisierJson("employees.json","curs20/")
# print(jsonAngajati.citeste())

# csvAngajati=FisierCsv("employees.csv","curs20/")
# print(csvAngajati.citeste())
# 7. Creati o lista de fisiere si apelati pentru fiecare fisier din lista metoda citeste.


##mostenire multipla 
#creati o clasa numita Persoana cu atributele nume si carsta si o metoda numita saluta. Apoi creati clasele Student si Angajat care mostenesc 
#clasa persoana. apelati metoda saluta pentru fiecare clasa. Suprascrieti apoi metoda din student si rulati. Suprascrieti apoi metoda din angajat si rulati 

class Persoana():
    def __init__(self,nume, varsta):
        self.nume=nume
        self.varsta=varsta
    def salut(self):
        print(f"Salut! Eu sunt {self.nume} si am {self.varsta} ani")

class Student(Persoana):
    def __init__(self,nume,varsta,an):
        super().__init__(nume,varsta)
        self.an=an

    def salut(self):
        print(f"Salut! Eu sunt {self.nume}, student in anul {self.an}")

class Angajat(Persoana):
    def __init__(self,nume, varsta,companie):
        super().__init__(nume,varsta)
        self.companie=companie
    
    def salut(self):
        print(f"Salut! Eu sunt {self.nume} si lucrez la {self.companie}")


class Intern(Angajat,Student):
    pass 

# student=Student("Ionica",18,2)
# angajat=Angajat("Ilie",32,"ItSchool")
intern=Intern("Vasile",24,"ItSchool")
# student.salut()
# angajat.salut()
# intern.salut()