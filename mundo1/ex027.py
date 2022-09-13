# Ex027:
# Primeiro e último nome de uma pessoa

nome = input('Qual o seu nome completo?:')
nome = nome.strip()
nome = nome.split()
fname = nome[0]
#lname = nome[nome.count(' ')-1]    ### Maneira alternativa de saber o útlimo nome, pode errar caso haja espaços adicionais
#nome.reverse() # outro método alternativo
lname = nome[len(nome)-1]

print('Seu primeiro nome é {}, e seu último nome é {}'.format(fname, lname))
