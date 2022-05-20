# Crie um programa que leia um numero real qualquer pelo teclado e mostre na ela sua porção inteira
from math import trunc
n1 = float(input('digite um numero qualquer: '))
print('a parte inteira de {} é: {}'.format(n1, trunc(n1)))


