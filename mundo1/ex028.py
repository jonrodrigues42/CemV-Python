# Ex028.
# Gere um número random entre 0 e 5, e o user tenta adivinhar
from random import randint as rd
print('Tente adivinhar um número entre 0 e 5')
ganhou = False
while not ganhou:
    n = rd(0, 5)
    tent = int(input(':::'))
    if tent == n:
        print('Ganhou!')
        ganhou = True
    else:
        print('ERRRRROU!')
