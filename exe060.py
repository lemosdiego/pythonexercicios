#faça um programa que leia um numero qualquer e mostre seu fatorial:

from math import factorial
from time import sleep
print('digite um numero para saber seu fatorial')
n = int(input('Digite um número: '))
c = n
f = 1
print('Calculando! aguarde...')
sleep(4)
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c -= 1
print('{}'.format(f))
