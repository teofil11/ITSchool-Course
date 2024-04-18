from convertor import operatii as op
from convertor import convertortemperatura as conv
import convertor.schimbvalutar as sv




def main():
    nr1 = int(input("Introduceti primul numar: "))
    nr2 = int(input("Introduceti al doi-lea numar: "))
    operatie = input("Introduceti operatia dorita(+,-,*,/): ")
    if operatie == "+":
        rezultat = op.adunare(nr1, nr2)
        print(f"Rezultatul operatiei este {rezultat}")
    elif operatie == "-":
        rezultat = op.scadere(nr1, nr2)
        print(f"Rezultatul operatiei este {rezultat}")
    elif operatie == "*":
        rezultat = op.inmultire(nr1, nr2)
        print(f"Rezultatul operatiei este {rezultat}")
    elif operatie == "/":
        rezultat = op.impartire(nr1, nr2)
        print(f"Rezultatul operatiei este {rezultat}")
    else:
        print("Operatia introdusa nu este valida")
    


def temp():
    temperatura = float(input("Introduceti temperatura in grade celsius: "))
    temperatura_f = conv.celsius_to_fahrenheit(temperatura)
    temperatura_k = conv.celsius_to_kelvin(temperatura)
    print(f"{temperatura} grade celsius inseamna {temperatura_f} grade fahrenheit")
    print(f"{temperatura} grade celsius inseamna {temperatura_k} grade kelvin")



def curs_valutar():
    lei = float(input("Introduceti suma in lei: "))
    euro = sv.schimb_euro(lei)
    dolar = sv.schimb_dolar(lei)
    print(f"{lei} lei este egal cu {euro} euro")
    print(f"{lei} lei este egal cu {dolar} dolari")

curs_valutar()