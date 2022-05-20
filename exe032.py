#faça um programa que leia um ano qualquer e mostre se ele é bissexto.

a = int(input('analisar o ano: '))
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('o ano {} é bissexto'.format(a))
else:
    print('o ano {} não é bissexto'.format(a))