# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
# início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep

def contador(i, f, p):
    print(f'contagem de {i} até {f} de {p} em {p}')
    if i > f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='',)
            cont -= p
        print('FIM')


contador(5, 50, 2)
contador(1, 10, 1)
print('AGORA É SUA VEZ DE PERSONALIZAR A CONTAGEM, VAMOS LÁ? ')
inicio = int(input('Inicio: '))
fim = int(input('fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)


