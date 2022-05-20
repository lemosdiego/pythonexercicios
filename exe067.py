#faça um programa que mostre a tabuada de varios numeros, um de cada vez, para cada valor digitado
#pelo usuário. O programa será interrompidp quando o numero solicitado for negativo.

from time import sleep
while True:
    tab = int(input('Informe um número para saber sua tabuada: '))
    print('CALCULANDO...')
    sleep(2)
    print('-' * 14)
    if tab < 0:
        break
    for c in range(1, 11):
        print(f'{tab} x {c} = {tab*c}')
    print('-' * 14)

