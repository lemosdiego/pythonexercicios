#faça um programa que leia o comprimento do cateto oposto
#e do cateto adjacente de um triangulo retangulo,
#calcule e mostre o comprimento da ipotenusa.
from math import hypot
co = float(input('digite o valor do cateto oposto: '))
ca = float(input('digite o valor do cateto adjacente: '))
h1 = hypot(co, ca)
print('o valor da hipotenusa é: {:.2f}'.format(h1))
