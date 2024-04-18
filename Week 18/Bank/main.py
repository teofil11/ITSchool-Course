from BankAccount import BankAccount
from Atm import Atm

def menu(atm):
    print("""1.Creeaza cont
2.Stergere cont
3.Depunere numerar
4.Retragere numerar
          """)
    input_text = int(input('Selecteaza optiunea: '))
    
    if input_text == 1:
        sold = int(input("Introdu sold: "))
        atm.creeare_cont(sold)
        atm.afiseaza_conturi()

    if input_text == 2:
        atm.afiseaza_conturi()
        nr_cont = input("Ce cont doriti sa stergeti: ")
        atm.stergere_cont(nr_cont)
        atm.afiseaza_conturi()

    if input_text == 3:
        nr_cont = input('In ce cont doriti sa adaugati bani: ')
        suma = int(input("Introduceti banii: "))
        atm.depunere_bani(nr_cont,suma)
        atm.afiseaza_conturi()

    if input_text == 4:
        nr_cont = input('Din ce cont doriti sa retrageti bani: ')
        suma = int(input("Retrageti banii: "))
        atm.retragere_bani(nr_cont,suma)
        atm.afiseaza_conturi()


atm = Atm()
while True:
    menu(atm)



