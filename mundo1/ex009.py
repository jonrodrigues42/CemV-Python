#Ex009.
#Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada

n = int(input('Digite um número: '))
x = 0
max = int(input('Qual o máximo? '))

while(x<(max+1)):
    print('{} x {} = {}'.format(n, x, n * x))
    x = x+1

