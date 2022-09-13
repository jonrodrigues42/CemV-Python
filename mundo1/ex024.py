# Ex024:
# Ler o nome da cidade, e dizer se ela começa ou não com "SANTO"

s = input('Qual cidade você nasceu? ')
s = s.strip()
ss = s.split()
print('Santo' in ss[0].title())
