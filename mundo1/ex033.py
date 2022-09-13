# Ex033
# Ler 3 números, e dizer qual é o maior e qual é o menor
a = int(input('Qual o primeiro número? '))
b = int(input('Qual o segundo número? '))
c = int(input('Qual o terceiro número? '))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
maior = a
if b>a and b>a:
    maior = b
if c>a and c>b:
    maior = c

print('O menor núemro é {}. e o maior é {}.'.format(menor, maior))


# Usando a função sort (cheetado)
#sort = [n1, n2, n3]
#sort.sort()
#print('O menor númeor é {} e o maior número é: {}'.format(sort[0], sort[2]))
