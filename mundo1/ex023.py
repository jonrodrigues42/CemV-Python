# Ler um número de 0 a 9999 e mostre cada casa separadamente
#   Ex: 1834
#       1 milhar
#       8 centena
#       3 dezena
#       4 unidade
#   Fazer como string e matematicamente

# Método String

s = input('Digite um número entre 0 e 9999:')

if len(s) == 1:
    print('{} unidade'.format(s[0]))

if len(s) == 2:
    print('{} dezena'.format(s[0]))
    print('{} unidade'.format(s[1]))

if len(s) == 3:
    print('{} centena'.format(s[0]))
    print('{} dezena'.format(s[1]))
    print('{} unidade'.format(s[2]))

if len(s) == 4:
    print('{} milhar'.format(s[0]))
    print('{} centena'.format(s[1]))
    print('{} dezena'.format(s[2]))
    print('{} unidade'.format(s[3]))

if len(s) > 4:
    print('Maior que 9999')


# Médodo matemático
n = int(s)
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print("""Analisando o número {}:
    Milhar: {}
    Centena: {}
    Dezena: {}
    Unidade {}
""".format(n, m, c, d, u))
