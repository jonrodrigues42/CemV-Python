# Ex030
# Ler um número e dizer se ele é impar ou par
n = int(input('Digite um número inteiro: '))
d = n % 2
if d == 0:
    print('Par')
else:
    print('Impar')
