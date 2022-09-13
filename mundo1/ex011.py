#Ex011.
# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule sua área e quantidade de tinta necessária para pintá-la.
# Cada litro de tinta pinta uma área de 2m².

l = int(input('Digite a largura em m: '))
a = int(input('Digite a altura em m: '))
area = l*a

print('A área da parede é {}. Você precisa de {:.1f}l de tinta para pintá-la.'.format(area, area/2))
