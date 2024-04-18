# Să presupunem că avem o listă de numere întregi și dorim să găsim suma tuturor numerelor pare din listă. 
# Folosind instrucțiunea for în Python, scrie un program care afișează suma numerelor pare din listă.


# lista = []
# for nr in range(6):
#     numar = int(input("Introduceti numerele: "))
#     lista.append(numar)
# suma = 0
# for numar in lista:
#     if numar % 2 == 0:
#         suma = suma + numar
# print(suma)




# Calcularea sumei elementelor unei liste.

# suma = 0
# lista = [1,432,54,3,64,234,64,4,543]
# for numar in lista:
#     suma += numar
# print(suma)


# Să se determine cel mai mare număr dintr-o listă de numere întregi


# lista = [1,3,45,654,234,65,4353,65,234,65,34,65,345,65,23]

# index = 1
# maxim = 0

# while index < len(lista):
#     if lista[index]>maxim:
#         maxim = lista[index]
#     index +=1
# print(maxim)



#  Să se determine suma primelor n numere naturale pare, unde n este introdus de utilizator
# n = int(input("Introduceti un numar: "))
# suma = 0
# x = 0

# for i in range(2, 2*n+1, 2):
#     suma += i
# print(suma)



# i = 2
# while x < n:
#     suma += i
#     i += 2
#     x += 1
# print(suma)



# Să se scrie un program care să calculeze suma cifrelor unui număr întreg dat.


# nr = int(input(("Introduceti un numar: ")))
# suma = 0
# while nr != 0:
#     cifra = nr % 10
#     suma += cifra
#     nr = nr // 10
# print(suma)


# un program care calculează suma numerelor întregi de la 1 la n (inclusiv).


# n = int(input("Introduceti un numar: "))
# suma = 0
# i = 1

# while i <= n:
#     suma +=i
#     i +=1
# print(suma)



# scrie un program care afișează toate numerele prime mai mici sau egale cu un număr dat de utilizator


# nr = int(input("Introduceti un numar: "))

# for x in range(2,nr+1):
#     este_prim = True
#     for y in range(2,int(x**0.5)+1):
#         if x % y == 0:
#             este_prim = False
#             break
#     if este_prim:
#         print(x)





# folder = []
# folder.append('poze')
# folder.append('documente')
# folder.append('arhiva')
# folder.append('jocuri')

# folder.sort()
# print(x)



# Suma numerelor până la un număr dat

# n = int(input("Introduceti un numar: "))
# i = 0
# suma = 0
# while i < n:
#     suma += i
#     i += 1
# print(suma)


# Afisarea cifrelor unui numar

# n = int(input("Introduceti un numar: "))

# while n != 0:
#     print(n%10)
#     n = n//10


# Scrie un program care citește un număr natural de la tastatură și afișează numărul inversat.

# n = int(input("Introduceti un numar natural: "))
# invers = 0
# while n != 0:
#     cifra = n % 10
#     invers = invers * 10 + cifra
#     n //= 10
# print("Numarul inversat este", invers)



# Scrie un program Python care citește un număr natural de la tastatură și verifică dacă este palindrom 
# (dacă se citește la fel de la stânga la dreapta și de la dreapta la stânga).


# n = int(input("Introduceti un numar: "))

# invers = 0
# copie = n
# while copie != 0:
#     cifra = copie % 10  
#     invers = invers * 10 + cifra
#     copie //= 10

# if n == invers:
#     print(n, "este palidrom")
# else:
#     print(n, "nu este palidrom")



# Să se calculeze suma primelor n numere naturale.

# n = int(input("Introduceti un numar: "))

# suma = 0
# i = 0
# while i <= n:
#     suma += i
#     i +=1
# print(suma) 



# Problema: Să se determine suma cifrelor unui număr.

# n = int(input("Introduceti un numar: "))
# suma = 0
# while n > 0:
#     cifra = n % 10
#     suma += cifra
#     n //= 10
# print(suma)


# Problema: Să se determine numărul de cifre ale unui număr.


# n = int(input("Introduceti un numar: "))
# numar_cifre = 0
# while n > 0:
#     numar_cifre += 1
#     n //= 10
# print(numar_cifre)



# Problema: Să se verifice dacă un număr dat este prim sau nu.

# n = int(input("Introduceti un numar: "))


# if n < 2:
#     print("Numarul nu este prim")
# else:
#     i = 2
#     while i * i < n:
#         if n % i == 0:
#             print("Numarul nu este prim")
#             break
#         i += 1
#     else:
#         print("Numarul este prim")

# Problema: Să se afișeze toate numerele pare de la 1 la n.

# n = int(input("Introduceti un numar: "))

# for numar in range(2,n+1,2):
#     print(numar)


# Să se afișeze tabla înmulțirii pentru numerele de la 1 la n.

# n = int(input("Introduceti un numar: "))

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         print(i*j, end="\t")
#     print()


# Să se afișeze toate numerele prime de la 1 la n

# n = int(input("Introduceti un numar: "))

# for nr in range(2, n+1):
#     for divizor in range(2, nr):
#         if nr%divizor == 0:
#             break
#     else:
#         print(nr, end=" ")