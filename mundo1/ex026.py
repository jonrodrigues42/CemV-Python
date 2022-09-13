# Ex026:
# Ler uma frase e dizer:
# Quantas vezes aparece a letra A
# Qual a posição da primeira letra A
# Qual a posição da última letra A

frase = input('Digite uma frase: ')
s = frase.strip()
print('A letra A aparece {} vezes'.format(s.lower().count('a')))
print('A primeira posição da letra A é {}'.format(s.lower().find('a')+1))
print('A última posição da letra A é {}'.format(s.lower().rfind('a')+1))
