# Ex031
# Calcular o valor de uma viagem de ônibus
# Até 200km, R$0,50 por km
# Acima de 200km, R$0,45 por km
km = float(input('Qual a distância a ser percorrida? '))
if km <= 200:
    print('O valor da viagem será R${:.2f}'.format(km*0.5))
else:
    print('O valor da viagem seŕa R${:.2f}'.format(km*0.45))
