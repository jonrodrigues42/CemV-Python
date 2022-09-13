### Ex022:
# Ler o nome completo e mostrar:
#   A) O nome com todas as letras maiusculas
#   B) // // minúnuculas
#   C) Quantas letras tem ao todo, sem considerar espaços
#   D) Quantas letras tem o primeiro nome ###

frase = input('Qual o seu nome:')

# A)
print(frase.upper())

# B)
print(frase.lower())

# C)
space = frase.count(' ')
print('Seu nome tem {} letras'.format(len(frase)-space))

# D)
nome = frase.split()
print('O primeiro nome é {}, ele tem {} letras.'.format(nome[0], len(nome[0])))
