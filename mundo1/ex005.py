#Ex005.
#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Digite um número: '))
print('Você digitou {}.\nSeu sucessor é {}, e seu antecessor é {}.'.format(n, n+1, n-1))
