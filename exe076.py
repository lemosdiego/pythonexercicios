#crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços
#na sequencia. No final mostre úma listagem de preços, organizando os dados em forma tabular.


lista = ('mouse', 105.00,
         'placa de video', 2202.00,
         'teclado', 250.00,
         'placa mãe', 1152.50,
         'fonte', 502.80 )
print('-=-' * 10)
print(' LISTA DE PREÇOS')
print('-=-' * 10)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R$ {lista[pos]:>7.2f}')
print('-=-' * 20)