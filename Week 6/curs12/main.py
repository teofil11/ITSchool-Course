
import om.contra as contra
import om.pro as pro
import om.extra as extra
from contabilitate import salarii

import datetime
import time
import os

def main():
    contra.functie("Internetul")
    pro.functie("internet")
    extra.functie("AI-ul ")


#avem 5 angajati cu salariul brut de 5000 RON 
#care sunt taxele pe care trebuie firma sa le plateasca 
def calculeazaTaxe(salariuBrut):
    taxe=0
    taxe+=salarii.cas(salariuBrut)
    taxe+=salarii.cass(salariuBrut)
    print(f"Trebuie sa plateasca {taxe} lei")
    print(f"Salariu net al unui angajat este {salarii.salariuNet(salariuBrut)}")

calculeazaTaxe(10000)

listaFisiere=[]
while(True):
    print(datetime.datetime.now())
    listaNouaFisiere=os.listdir("E:/IT School/test")
    for fisier in listaNouaFisiere:
        if(fisier not in listaFisiere):
            print("Fisier nou: "+fisier)
    listaFisiere=listaNouaFisiere
    time.sleep(10)
