from BankAccount import BankAccount
import json


path = 'Week 18/Bank/'

class Atm():
    def genereaza_nrCont(self):
        with open(f'{path}nrCont.txt', 'r') as file:
            nr = file.read()
        while len(nr) < 13:
            nr = '0' + nr
        cont = 'ROBTRLRONCRT' + nr
        with open(f'{path}nrCont.txt', 'w') as file:
            nr = int(nr) + 1
            file.write(str(nr))
        return cont
    

    def creeare_cont(self,balanta):
        nr_cont = self.genereaza_nrCont()
        cont = BankAccount(nr_cont,balanta)
        with open(f'{path}accounts.json', 'r') as file:
            data = json.load(file)
        data.append({'Cont': nr_cont, 'Balanta': balanta})
        with open(f'{path}accounts.json', 'w') as file:
            json.dump(data, file, indent=4)
    

    def depunere_bani(self,nrCont,suma):
        with open(f'{path}accounts.json', 'r') as file:
            data = json.load(file)
        for cont in data:
            if cont['Cont'] == nrCont:
                cont['Balanta'] += suma
        with open(f'{path}accounts.json', 'w') as file:
            json.dump(data, file, indent=4)


    def retragere_bani(self,nrCont,suma):
        with open(f'{path}accounts.json', 'r') as file:
            data = json.load(file)
        for cont in data:
            if cont['Cont'] == nrCont:
                if cont['Balanta'] >= suma:
                    cont['Balanta'] -= suma
                else:
                    print('Fonduri insuficiente')
        with open(f'{path}accounts.json', 'w') as file:
            json.dump(data, file, indent=4)


    def stergere_cont(self,nrCont):
        with open(f'{path}accounts.json', 'r') as file:
            data = json.load(file)
        data = [cont for cont in data if cont['Cont'] != nrCont]
        with open(f'{path}accounts.json', 'w') as file:
            json.dump(data, file, indent=4)


    def afiseaza_conturi(self):
        with open(f'{path}accounts.json', 'r') as file:
            data = json.load(file)
        for cont in data:
            for key, value in cont.items():
                print(f'{key}: {value}')
            print('-' * 30)