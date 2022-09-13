# Exercício Python 15:
# Escreva um programa que pergunte a quantidade de Km percorridos
# por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos km rodados? '))
dias = float(input('Por quantos uantos dias? '))

preco = (km*0.15)+(dias*60)
print('Você irá pagar R${:.2f}'.format(preco))
