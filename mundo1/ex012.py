#Ex012.
# Faça um algoritmo que leia um preço de um produto e mostre seu novo preço, com 5% de desconto.

x = float(input('Qual o valor do produto? R$'))
desc = float(input('Qual o desconto? %'))
porc = desc/100
print('O novo preço, com {:.0f}% de desconto, será R${:.2f}.'.format(desc, x-(x*porc)))


