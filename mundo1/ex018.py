# Estudo de módulos
# sen, cos e tang
from math import sin, cos, tan, radians

an = float(input('Qual o ângulo? '))
x = radians(an)
print('O seno de {} é: {:.2f}'.format(an, sin(x)))
print('O cossneno de {} é {:.2f}'.format(an, cos(x)))
print('A tangente de {} é {:.2f}'.format(an, tan(x)))
