#faça um programa que leia um número inteiro e diga se ele é ou nao um numero primo.

num = int(input('Digite um número: '))
tot = 0
for c in range(1, num +1 ):
    if num % c == 0:
        print('\033[33m', end='-')
        tot +=1
    else:
        print('\033[31m', end='-')
    print('{}'.format(c), end='-')
print('\n\033[mo número {} foi divisivel {} vezes'.format(num, tot))
if tot == 2:
    print('esse numero é PRIMO!')
else:
    print('esse numero NÃO É PRIMO!')

