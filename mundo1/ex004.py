s = input('Digite algo: ')
print('Tipo primitivo {}'.format(type(s)))
print('Só espaços? {}'.format(s.isspace()))
print('É um nmr? {}'.format(s.isnumeric()))
print('É alpha? {}'.format(s.isalpha()))
print('Alphanum? {}'.format(s.isalnum()))
print('Mai? {}'.format(s.isupper()))
print('Min? {}'.format(s.islower()))
print('Capt? {}'.format(s.istitle()))