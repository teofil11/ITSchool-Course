# - cititi de la tastatura 4 numere si adaugati-le intr-o lista
# numere = []
# for nr in range(4):
#     numar = int(input("Introduceti un numar: "))
#     numere.append(numar)



# - verificati daca cel putin unul dintre numere este par


# exista_par = False

# for numar in numere:
#     if numar%2 == 0:
#         exista_par =True
#         break

# if exista_par == True:
#     print("Exista cel putin un numar par")
# else:
#     print("Nu exista nici un numar par")



 # - verificati daca toate numerele sunt impare 


# toateSuntImpare = True

# for numar in numere:
#     if numar%2 ==0:
#         toateSuntImpare = False

# if toateSuntImpare == True:
#     print("Toate numerele sunt impare")
# else:
#     print("Nu toate numerele sunt impare")



# - afisati maximul numerelor citite de la tastatura

# maxim = numere[0]
# index = 1
# while index < len(numere):
#     if numere[index]>maxim:
#         maxim = numere[index]
#     index = index +1
# print(maxim)


# - afisati minimul numerelor citite de la tastatura 

# minim=numere[0]
# index=1
# while(index<len(numere)):
#    if(numere[index]<minim):
#       minim=numere[index]
#    index=index+1
# print(minim)




# Problema 2: 
# - cititi numere de la tastatura pana cand se introduce numar 6 si adaugati-le intr-un array 
# - rescrieti toate subpunctele de la problema 1 cu while 

# numere = []
# numar = int(input("Introduceti un numar: "))
# numere.append(numar)

# while numar != 6:
#     numar = int(input("Introduceti un numar: "))
#     numere.append(numar)
# print(numere)



# - verificati daca cel putin unul dintre numere este par


# exista_par = False
# for x in numere:
#     if x%2 == 0:
#         exista_par = True
#         break
# if exista_par == True:
#     print("In aceasta lista este cel putin un numar par")
# else:
#     print("In aceasta lista nu sunt numere pare")


# - verificati daca toate numerele sunt impare


# toateSuntImpare = True
# for x in numere:
#     if x%2 == 0:
#         toateSuntImpare = False
#         break
# if toateSuntImpare == True:
#     print("Toate numerele din lista sunt impare")
# else:
#     print("Nu toate numerele din lista sunt impare")




# - afisati maximul numerelor citite de la tastatura 
# 
#   
# maxim = numere[0]
# index = 1
# while index < len(numere):
#     if numere[index]>maxim:
#         maxim = numere[index]
#     index = index + 1
# print(maxim)



# - afisati minimul numerelor citite de la tastatura


# minim = numere[0]
# index = 1 
# while index < len(numere):
#     if numere[index]<minim:
#         minim = numere[index]
#     index = index + 1
# print(minim)








# 3. Cititi un numar de la tastatura si afisati tabla inmultirii pentru acel numar.


# x = int(input("Introduceti un numar"))

# for numar in range(1, 10):
#     print(f"{x} x {numar} = {x*numar}")
    



# Problema 4:
# Cititi un sir de caractere de la tastatura si afisati cate vocale sunt in acel sir


# x = input("Introduceti un text: ")
# vocale = 'aeiou'
# numar_vocale = 0

# for vocala in x:
#     if vocala.lower() in vocale:
#         numar_vocale = numar_vocale + 1
# print(f"In textul introdus sunt {numar_vocale} vocale")
