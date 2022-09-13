#Ex008.
#Escreva um programa que leia um valor em metros e o exiba em cm e mm
m = int(input('Digite um valor em m: '))
cm = m*100
mm = m*1000
print('{}m equivale a {}cm e {}mm.'.format(m , cm, mm))
