#Ex010.
#Crie um programa que leia quanto dinheiro uma pessoa tem, e quantos dólares ela pode comprar
#Considerar US$1,00 = R$3,27, e R$5,33

rs = float(input('Quantos R$ vc tem? '))
us3 = rs/3.57
us5 = rs/5.33

print('Considerando 3,27, você teria: US${:.2f}.'.format(us3))
print('Considerando 5,33, você teria: US${:.2f}.'.format(us5))