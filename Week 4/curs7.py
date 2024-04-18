#Afisati sirul [1,3,2,6,7,2,3] sub urmatoarea forma: elementul de pe pozitia 0 este 1 
                                        #        elementul de pe pozitia 1 este 3 
sir=[2,3,2,6,7,2,2]
for i in range(len(sir)):
    print(f"sir[{i}]={sir[i]}")


# rotiti toate elementele cu o pozitie spre stanga [1,3,2,6,7] -> [3,2,6,7,1]
#                                                  0 1 2 3 4
sir=[1,3,2,6,7]
aux=sir[0]
for nr in range(4):
    sir[nr]=sir[nr+1]
sir[-1]=aux
print(sir)


#rotiti toate elementele cu o pozitie spre dreapta  [1,3,2,6,7] => [7,1,3,2,6]
sir=[2,6,1,3] #> [3,2,6,1]15
aux=sir[-1]
for nr in range(3,0,-1):
    sir[nr]=sir[nr-1]
sir[0]=aux
print(sir)



#verificati ca un numar citit de la tastatura este prim (de exemplu 17, 13,11)
#adica nu exista niciun numar astfel incat numar%divizor==0
# 8, 2,3,4,5,6,7 
nr=int(input("Introduceti un numar: "))
flag=False
for divizor in range(2,nr,1):
    if(nr%divizor==0):
        flag=True
if(flag==True):
    print("Numarul nu e prim") 
else :
    print("Numarul este prim") 


#rescrieti range(start,stop,pas) cu while 

start=int(input("start="))
stop=int(input("stop="))
pas=int(input("pas="))

nr=start
while(nr<stop):
    print(nr)
    nr=nr+pas
    
for nr in reversed(range(1,7)):
    print(nr)


#citim un numar de la tastatura si afisam astfel: pentru 4 
#4 3 2 1 
#3 2 1 
#2 1 
#1

nr=int(input("nr="))
for el in range(nr,0,-1):
    myString=""
    for i in range(el,0,-1):
        myString=myString+str(i)+" "
    print(myString)
