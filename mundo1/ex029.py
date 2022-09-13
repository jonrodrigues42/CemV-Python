# Ex029.
# Radar de velocidade
# Se for acima de 80km/h, dizer que foi multado e calcular a multa, sendo R$7,00 por cada km/h acima do limite
# Senão, não faça nada
vel = float(input('Qual a velocidade? '))
limit = 80.0
rs = 7
if vel > limit:
    print('Você foi multado em R${:.2f}'.format((vel-limit)*rs))
