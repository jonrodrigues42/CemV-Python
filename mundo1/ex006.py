#Ex006.
#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

n = int(input('Digite um número: '))
d = n*2
t = n*3
r = n**(1/2)
print('Você digitou {}.'.format(n))
print('Seu dobro é {}, seu triplo é {}, e sua raiz quadrade é {}.'.format(d, t, r))
