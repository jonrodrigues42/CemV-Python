# Ex035
# Ler 3 retas e dizer se elas podem ou não formar um triangulo
# (princípio matemático)
a = int(input('Lado A: '))
b = int(input('Lado B: '))
c = int(input('Lado C: '))

if a+b > c and a+c > b and b+a > c and b+c > a:
    print('É um triangulo')
else:
    print('Não é um triangulo')
