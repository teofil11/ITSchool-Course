# 1. Verificati daca 3173 de lei inseamna mai putin de 600 de euro (la cursul bnr de azi).
print(3173/4.9157 < 600)

# 2. Fie 3 variabile a, b, c cu valori diferite.
a = 31
b = 95
c = 47 
# 2.a Verificati daca a este mai mic ca b si b este mai mic ca c
print(a<b and b<c)
# 2.b Verificati daca a este mai mic ca c.
print(a<c)
# 2.c Ce observati aici?


# 3. Verificati daca 2+2:2 este egal cu 2:2+2
print(2+2/2 == 2/2+2)

# 4. Inversati rezultatul de la problema 3 (daca este True sa fie False sau daca este False sa fie True)
print((2+2)/2 == 2/2+2)

# 5. Verificati daca numarul 144 se imparte exact la 12
print(144 % 12 == 0)

# 6. Verificati daca numarul 50 se imparte exact la 2,5, 10 ( intr-o singura instructiune)
print(50 % 2 == 0 and 50 % 5 == 0 and 50 % 10 == 0)

# 7. Verificati daca numarul 1024 se imparte exact la 4,8,16 sau la 100
print(1024 % 4 == 0 and 1024 % 8 == 0 and 1024 % 16 == 0 or 1024 % 100 == 0)