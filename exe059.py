#crie um programa que leia dois valores e mostre um menu na tela: #
# [1] somar
#[2] multiplicar
#[3] maior
#[4] novos numeros
#[5] sair do programa
#o programa devera realizar a operação solicitada em cada caso.


from time import sleep
valor1 = int(input('digite o 1° valor: '))
valor2 = int(input('digite o 2° valor: '))
opçao = 0
while opçao != 5:
    print('''digite a opção desejada,
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opçao = int(input('escolha uma opção: '))
    if opçao == 1:
        soma = valor1 + valor2
        print('a soma entre {} e {} é igual a {}'.format(valor1, valor2, soma))
    elif opçao == 2:
        multi = valor1 * valor2
        print('a multiplicção entre {} e {} é igual a {}'.format(valor1, valor2, multi))
    elif opçao == 3:
        if valor1 >  valor2:
            maior = valor1
        else:
            maior = valor2
            print('o maior valor entre {} e {} é {}'.format(valor1, valor2, maior))
    elif opçao == 4:
        print('informe outros valores:')
        valor1 = int(input('digite um vaalor: '))
        valor2 = int(input('digite outro valor: '))
    elif opçao == 5:
        print('finalizando...')
        sleep(4)
    else:
        print('opção inválida, tente novamente')
print('obrigado!')