def doar_litere(string):
    doarLitere = True
    for caracter in string:
        if caracter.isalpha() == False:
            doarLitere = False
    return doarLitere

def anumite_caractere(string):
    toateOk = True
    for caracter in string:
        if(caracter.isalpha() == False):
            if(caracter.isdigit() == False):
                if(caracter != '*'):
                    toateOk = False
    return toateOk



def signUp():
    username = ''
    password = ''
    ok = False
    while ok == False:
        username = input("username: ")
        if doar_litere(username) == True:
            ok = True
        else:
            print("Username-ul trebuie sa contina doar litere")
    
    ok2 = False
    while ok2 == False:
        password = input("password: ")
        if anumite_caractere(password) == True:
            ok2 = True
        else:
            print("Parola trebuie sa contina doar litere, cifre si caracterul *")
    return [username, password]

def reset_password():
    ok = False
    newPassword = ''
    while ok == False:
        newPassword = input("Introdiceti parola noua: ")
        if anumite_caractere(newPassword) == True:
            ok = True
        else:
            print("Parola trebuie sa contina litere, cifre si caracterul *")
    return newPassword


def singIn(username, password):
    incercari = 3
    nume = ''
    pas = ''
    
    print("""Pentru a te autentifica trebuie sa introduci username-ul si parola,
ai doar trei incercari, dupa cele trei incercari contul se va bloca""")
    for incercare in range(incercari):
        nume = input("Username: ")
        pas = input("Parola: ")
        if nume == username and pas == password:
            print("Te-ai autentifiact cu succes")
            break
        else:
            incercari_ramase = incercari -1
            incercari -=1
            print(f"Username-ul sau parola sunt gresite mai ai {incercari_ramase} incercari")
            if incercari_ramase == 0:
                print("Cont Blocat")





def meniu():
    print("""Bine ati venit pe site-ul nostru.
Pentru a va inregistra apasati tasta 1.
Pentru a va autentifica apasati tasta 2.
Pentru a reseta parola apasati tasta 3.
Pentru a iesti apasati tasta 4""")
    optiune = 0
    while optiune != 4:
        optiune = int(input("Alegeti optiunea: "))
        if optiune == 1:
            dict = signUp()
        if optiune == 2:
            singIn(dict[0], dict[1])
        if optiune == 3:
            dict[1] = reset_password() 
            

meniu()

