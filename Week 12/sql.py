dictionar = [['hagi','Gica','brunet','fara'],
            ['ionut', 'popescu','saten','fara'],
            ['mihai','viteazul','necunoscut','fara'],
            ['stelica','ion','blond','fara']
]


def scrieMajuscula(nume):
    output = nume[0].upper()
    output += nume[1:len(nume)].lower()
    return output

def genereaza_insert():
    for element in dictionar:
        print(f"INSERT INTO PORSOANE VALUES(null, '{scrieMajuscula(element[0])}','{scrieMajuscula(element[1])}','{element[2]}','{element[3]}');")

# genereaza_insert()





