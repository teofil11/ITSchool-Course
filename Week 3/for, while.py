# nr = input("Introduceti un numar: ")
# cifre = '0123456789'
# for caracter in nr:
#     if(caracter in cifre):
#         print(f"{caracter} Se afla in lista")
#     else:
#         print(f"{caracter} Nu se afla in lista")


# numere=[]
# limit = 6
# while limit>0:
#     array=[]
#     for numar in range(limit):
#         array.append((numar))
#     limit = limit -1
#     print(array[::-1])



# for i in range(10):
#     print("*")
# for i in range(10):
#     row = row + "*"
# print(row)


# array = [1, 2, 6, 2, 3, 7, 9, 10]

#afisare cu for
# for nr in array:
#     print(nr)


#afiseare cu while
# index = 0
# while(index<len(array)):
#     print(array[index])
#     index = index + 1


#problema curs 1 (afisare numere descrescator)
#5 4 3 2 1 
#4 3 2 1
#3 2 1
#2 1
#1
numere=[]
limit=6

while limit>0:
    array=[]
    for numar in range(limit):
        array.append(numar)
    limit=limit-1
    print(array[::-1])

# # afisare numere din array
array=[1,2,6,2,3,7,9,10]
for nr in array:
    print(nr)

# afisare numere din array cu while
array=[1,2,6,2,3,7,9,10]
#      0 1 2 3 4 5 6 7
print(len(array))
index=7
while(index>=0):
    print(array[index])
    index=index-1

#introduceti parola cat timp parola e gresita 
parola="bogdan"
parolaUtilizator=input("Introduceti parola: ")
while (parola!=parolaUtilizator):
    print('Parola este gresita')
    parolaUtilizator=input("Introduceti parola: ")
print("parola este corecta")

# afisati ultima cifra a unui numar
n=16421
ultimaCifra=n%10
print(ultimaCifra)

# calculati suma cifrelor unui numar
n=12345131
sum=0
while(n>0):
    ultimaCifra=n%10
    sum=sum+ultimaCifra
    n=n//10
print(sum)


# stergeti dintr-un numar suma cifrelor lui atata timp cat el este pozitiv
nrOriginal=int(input("Introduceti un numar:"))
while(nrOriginal>0):
    n=nrOriginal
    sum=0
    while(n>0):
        ultimaCifra=n%10
        sum=sum+ultimaCifra
        n=n//10
    nrOriginal=nrOriginal-sum
    print(f"Nr original este acum {nrOriginal} iar suma a fost {sum}")


# #cum aflu valoarea maxima dintr-o lista 
lista=[1,2,6,2,1,10,1]
#      0 1 2 3 4 5  6
maxim=lista[0]
index=1
while(index<len(lista)):
   if(lista[index]>maxim):
      maxim=lista[index]
   index=index+1
print(maxim)

#cum aflu valoarea minima dintr-o lista 
lista=[1,2,6,2,1,10,1]
#      0 1 2 3 4 5  6 
min=lista[0]
index=1
while(index<len(lista)):
   if(lista[index]<min):
      min=lista[index]
   index=index+1
print(min)


#verificati daca intr-o lista toate elementele sunt pare 
x=[2,4,6,8,10]
x=[2,4,5,8,10]
toateSuntPare=True
for nr in x:
    if(nr%2!=0):
        toateSuntPare=False
if(toateSuntPare==True):
    print("Toate sunt pare")
else:
    print("Exista si impare")


# #verificati daca intr-o lista exista cel putin un element impar
ok=False
for nr in x:
    print(nr)
    if(nr%2!=0):
        ok=True
        break
if(ok==True):
    print("Am gasit un numar impar")
else:
    print("Nu am gasit impare")

#instructiunea continue
for nr in range(10):
   print(nr)
   if(nr%2==0):
      print("lucrez ceva foarte complicat aici daca nr este par ")
      ###ceva care dureaza mult####
      for i in range(10000):
         print(i)
   else:
      continue
   

# for intr-un interval din 2 in 2 
for i in range(1,10,2):
    print(i)