dictionar=[["haGi","gica","brunet"],
           ["ionut","popescu","saten"],
           ["miHai","vancica","blond"],
           ["mihai","viteazul","necunoscut"],
           ["stElica","ion","blond"]
]

#INSERT INTO PERSOANE VALUES(null,'Hagi','Gica','brunet');


#haGi=> Hagi
def scrieMajuscula(nume):
    output=nume[0].upper()
    output+=nume[1:len(nume)].lower()
    return output

def generaza_insert():
    for element in dictionar:
        print(f"INSERT INTO PERSOANE VALUES(null,'{scrieMajuscula(element[0])}','{scrieMajuscula(element[1])}','{scrieMajuscula(element[2])}','fara');")

import random
culori_par=['brunet','blond','saten','roscat']
#insert into persoane values(null,'nume1','prenume1','brunet',"nume+brunet")
for element in range(100):
    culoare_par=culori_par[random.randint(0,3)]
    print(f"INSERT INTO PERSOANE VALUES(null,'nume{element}','prenume{element}','{culoare_par}','nume{str(element)+culoare_par}');")
