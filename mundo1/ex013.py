#Ex013.
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

sal = float(input('Qual o salario? R$'))
aum = float(input('Qual o aumento? '))
porc = aum/100
print('O novo salário, com {:.0f}% de aumento seŕa: R${:.2f}'.format(aum, sal+(sal*porc)))