# Ex034
# Cálculo de salários
# Para salários acima de 1250, aumento de 10%
# Para salários menores ou iguais a 1250, aumento de 15%
sal = float(input('Qual o seu salário? R$'))
if sal > 1250:
    novo = sal+(sal*0.1)
else:
    novo = sal+(sal*0.15)
print('Seu novo salaŕio será de: R${:.2f}'.format(novo))
