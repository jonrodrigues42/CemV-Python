# Ex032
# Dizer se um ano é bissexto ou não
# se ano % 4 == 0
# 	se ano % 100 == 0
# 		não é bissexto
# 	else
# 		é bissexto
# else
# 	se ano % 400 == 0
# 		é bissexto
# 	else
# 		não é bissexto
ano = int(input('Qual o ano? '))
bi = False

if ano % 4 == 0:
    if ano % 100 == 0:
        bi = False
    else:
        bi = True
else:
    if ano % 400 == 0:
        bi = True
    else:
        bi = False

if bi:
    print('é BI!')
else:
    print('NÃO É BI')
