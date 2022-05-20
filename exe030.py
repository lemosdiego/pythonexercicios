#crie um programa que o usuário informe um número e o programa retorne se o numero é par ou impar.

num = int(input('informe um número: '))
pi = num % 2
if pi == 0:
    print('número {} é par'.format(num))
else:
    print('número {} é impar'.format(num))
