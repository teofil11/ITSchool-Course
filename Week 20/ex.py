
def palindrom(string):
    inverrs = string[::-1]
    if inverrs == string:
        return True
    return False

# print(palindrom('aaa'))


def multiplu():
    for i in range(1,101):
        if i%3 == 0:
            print('multiplu')
        else:
            print(i)

# print(multiplu())

def paranteze(string):
    dict_paranteze = {')':'(', ']':'[', '}':'{'}
    counter = []

    for caracter in string:
        if caracter in '([{)]}':
            counter.append(caracter)
    
    var = (''.join(counter))
    print(var)
    var = var.replace('()', '')
    print(var)
    var = var.replace('[]','')
    print(var)
    var = var.replace('{}','')
    print(var)

    if var == '':
        print('Paranteze valide')
    else:
        print('Paranteze incorente')
    


# paranteze('{[(1+2)]+[(3*2)+2]}*4')
