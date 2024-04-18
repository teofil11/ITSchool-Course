#1 Să presupunem că avem o listă de numere întregi și dorim să găsim cel mai mare număr din această listă.
def find_max(lista):
    max_number = lista[0]
    for nr in lista:
        if nr > max_number:
            max_number = nr
    return max_number

# print(find_max([12,32,43,6,54,234,4]))

#2 Aduna numerele pare si scadele pe cele pare
def suma_numere(lista):
    suma = 0
    for nr in lista:
        if nr % 2 == 0:
            suma+= nr
        else:
            suma -= nr
    return suma

# print(suma_numere([1,2,3,4,5,6]))


#3 Să presupunem că avem o listă de numere întregi și dorim să găsim media aritmetică a acestora, cu excepția primelor două numere.

def ma(lista):
    return sum(lista[2:]) / (len(lista) - 2)

# print(ma([10,20,30,40,50]))


#4 Să presupunem că avem o listă de numere întregi și dorim să calculăm media lor,
# dar excludem valorile negative și cele mai mari decât o anumită valoare.

def calcul(lista, min_value, max_value):
    numere =[nr for nr in lista if min_value < nr < max_value]
    return sum(numere) / len(numere)

# print(calcul([-2,2,2,100], 0, 100))


#5 Să presupunem că avem o listă de numere și dorim să obținem o nouă listă care să conțină doar numerele pare din lista inițială, dar ridicate la pătrat.

def putere_pare(lista):
    x = []
    for nr in lista:
        if nr % 2 == 0:
            x.append(nr**2)
    return x

# print(putere_pare([2,3,4,5,6]))


