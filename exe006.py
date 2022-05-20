#crie um algoritmo que leia o numero e mostre o seu dobro,triplo e raiz quadrada.

num = int(input('digite um número: '))
dobro = num * 2
triplo = num * 3
raiz = num ** 0.5
print('o dobro de {} é {}'.format(num, dobro))
print('o triplo de {} é {}'.format(num, triplo))
print('a raiz de {} é {:.2f}'.format(num, raiz))
