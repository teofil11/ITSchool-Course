import json

class ContBancar():
    def genereaza_cont(self):
        with open('Week 11/tema/nrCont.txt', 'r') as file:
            nr = file.read()
        while len(nr) < 13:
            nr = '0' + nr
        cont = 'ROBTRLRONCRT' + nr
        with open('Week 11/tema/nrCont.txt', 'w') as file:
            nr = int(nr) + 1
            file.write(str(nr))
        try:
            suma = int(input('Ce suma de bani doriti sa depuneti in cont: '))
            if suma < 0:
                suma = 0


            with open('Week 11/tema/conturi.json','r') as file:
                data = json.load(file)
                
                data.append({'Cont': cont,'Balanta': suma})
        
            with open('Week 11/tema/conturi.json','w') as file:
                json.dump(data, file, separators=",:",indent=4)
        except ValueError:
            print('Suma trebuie sa contin doar numere')
    def inchide_cont(self):
        self.nCont = input("Introduceti numarul contului pe care vreti sa il inchideti: ") 
        with open('Week 11/tema/conturi.json','r') as file:
            continut = json.load(file)
        index = 0
        while index < len(continut):
            for key,value in continut[index].items():
                if value == self.nCont:
                    del continut[index]
                    print('Contul a fost sters')
            index += 1
        with open('Week 11/tema/conturi.json','w') as file:
            json.dump(continut, file, separators=',:',indent=4)

class Banca():
    def depunere(self):
        index = 0
        with open('Week 11/tema/conturi.json','r') as file:
            continut = json.load(file)
        
        self.cont = input('Introduceti numarul contului in care vreti sa depuneti bani: ')
        self.suma = int(input('Suma de bani pe care vreti sa o depuneti in cont: '))
        if self.suma < 0:
            print('Trebuie sa introduceti o suma pozitiva')
        else:
            while index < len(continut):
                for key,value in continut[index].items():
                    if value == self.cont:
                        balance = continut[index]['Balanta']
                        new_balance =self.suma + balance
                        continut[index]['Balanta'] = new_balance
                        with open('Week 11/tema/conturi.json','w') as file:
                            data = json.dump(continut, file,separators=',:', indent=4)
                index += 1
    def retragere(self):
        index = 0
        with open('Week 11/tema/conturi.json','r') as file:
            continut = json.load(file)
        
        self.cont = input('Introduceti numarul contului din care vreti sa retrageti bani: ')
        self.suma = int(input('Suma de bani pe care vreti sa o retrageti din cont: '))
        if self.suma < 0:
            print('Trebuie sa introduceti o suma pozitiva')
        else:
            while index < len(continut):
                for key,value in continut[index].items():
                    if value == self.cont:
                        balance = continut[index]['Balanta']
                        new_balance = balance - self.suma
                        continut[index]['Balanta'] = new_balance
                        if new_balance < 0:
                            print('Sold insuficient')
                        else: 
                            with open('Week 11/tema/conturi.json','w') as file:
                                data = json.dump(continut, file,separators=',:', indent=4)
                index += 1
    def interogare_sold(self):
        index = 0
        with open('Week 11/tema/conturi.json','r') as file:
            continut = json.load(file)
        self.cont = input('Introduceti numarul contului din care vreti sa aflati soldul: ')
        while index < len(continut):
            for key, value in continut[index].items():
                balance = continut[index]['Balanta']
                if value == self.cont:
                    print(f'Soldul contului {value} este de {balance} lei')
            index += 1
                    
        

def meniu():
    print('Bine ati venit la Banca Transilvania.')
    print('-'*10)
    print("""Pentru a creea un cont apasati tasta 1.
Pentru a depune bani apasati tasta 2.
Pentru a retrage bani apasati tasta 3.
Pentru a afla soldul contului apasati tasta 4.
Pentru a inchide contul apasati tasta 5.
Pentru a iesi apasati tasata 0""")
    while True:
        try:
            optiune = int(input('Introduceti optiunea: '))
            if optiune == 1:
                ContBancar().genereaza_cont()
            if optiune == 2:
                Banca().depunere()
            if optiune == 3:
                Banca().retragere()
            if optiune == 4:
                Banca().interogare_sold()
            if optiune == 5:
                ContBancar().inchide_cont()
            if optiune == 0:
                print('La revedere')
                exit()
        except ValueError:
            print("Trebuie sa introduceti un numar")


meniu()


            


