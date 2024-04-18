##creati un quiz 
raspunsuri=[]
intrebari=[{
                    "intrebare":"Cum se declara un dictionar?",
                    "raspunsuri":"a.{} b.[] c.()",
                    "corect":"a"
                    },
                    {
                    "intrebare":"Cum se defineste o functie?",
                    "raspunsuri":"a.def functie:  b.def functie(): c. functie()",
                    "corect":"b"
                    },
                    {
                    "intrebare":"Ce returneaza urmatoarea operatie: 2+3*2",
                    "raspunsuri":"a.3  b.8  c.5 ",
                    "corect":"b"
                    },
                    {
                    "intrebare":"Fiind data lista x=[4,2,1,3] ce va afisa x[4]",
                    "raspunsuri":"a.3  b.1  c.eroare ",
                    "corect":"c"
                    },
                    {
                    "intrebare":"Ce reprezinta instructiunea elif",
                    "raspunsuri":"a.evitam un else si un if  b.e degeaba  c.nu exista ",
                    "corect":"a"
                    }
                ]



def afiseaza_intrebare(nr_intrebare):
    print(intrebari[nr_intrebare].get("intrebare"))
    print(intrebari[nr_intrebare].get("raspunsuri"))
    raspuns=input("Introduceti varianta: ")
    raspunsuri.append(raspuns)

def afiseaza_intrebari():
    for intrebare in intrebari:
        print(intrebare["intrebare"])
        print(intrebare["raspunsuri"])
        raspuns=input("Introduceti varianta: ")
        raspunsuri.append(raspuns)
        print("\n")

def calculeaza_scor_si_reset():
    scor=0
    for i in range(len(intrebari)):
        if(raspunsuri[i]==intrebari[i]["corect"]):
            scor=scor+2
    raspunsuri.clear()
    return scor    

def urmatoarea_intrebare():
    intrebare_curenta=len(raspunsuri)
    if len(intrebari)-1<=intrebare_curenta:
        print("Nu mai sunt intrebari")
    else:
        afiseaza_intrebare(intrebare_curenta)

def quizz():
    print("""1.Start quizz 
2.Next question
3.Show score and reset
4.Exit
    """)

    while(True):
        optiune=input("Alege optiune: ")
        if optiune.isdigit():
            optiune=int(optiune)
            if(optiune not in range(1,5)):
                print("Optiunea trebuie sa fie in intervalul 1-4")
                continue
        else: 
            print("Trebuie sa introduceti o cifra!")
            continue
        if optiune==1 or optiune==2:
            urmatoarea_intrebare()
        if optiune==3:
            calculeaza_scor_si_reset()
        if optiune==4:
            exit()



quizz()
print(raspunsuri)