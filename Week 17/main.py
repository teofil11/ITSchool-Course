def muta_elementele_cu_o_pozitie_la_dreapta():
    lista= [1,4,3,7,5,6,11,8,9]
    aux = lista[-1]
    for i in range(len(lista)-1,0,-1):
        lista[i] = lista[i-1]
    lista[0] = aux
    print(lista)

muta_elementele_cu_o_pozitie_la_dreapta()