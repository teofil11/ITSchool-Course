def string(string):
    vowel = 'aeiou'
    vocale = 0
    consoane = 0
    for i in string:
        if i in vowel:
            vocale += 1
        elif i not in vowel and i.isalpha():
            consoane += 1
    
    return f'Vocale : {vocale}, Consoane: {consoane}'

