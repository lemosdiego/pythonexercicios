#faça um programa que leia um numero qualquer e mostre na tela
#o valor do seno,cosseno e tangente desse angulo.

from math import radians, sin, cos, tan
a = float(input('digite o valor do angulo: '))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print('o angulo de {} tem o SENO de {:.2f}'.format(a, s))
print('o angulo de {} tem o COSSENO de {:.2f}'.format(a, c))
print('o angulo de {} tem a TANJENTE de {:.2f}'.format(a,t))
