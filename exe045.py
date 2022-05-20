#crie um programa que faça o computador jogar jokenpô comm você.

from random import randint
from time import sleep
opoes = ('pedra', 'papel', 'tesoura')
maquina = randint(0, 2)
print('''Escolha uma opção:
[ 1 ] PEDRA'
[ 2 ] PAPEL
[ 3 ] TESOURA''')
jogador = int(input('Qual sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('a maquina escolheu {}'.format(maquina))
print(f'você escolheu '.format(jogador))
if maquina == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('VOCÊ VENCEU')
    elif jogador == 2:
        print('MAQUINA VENCU')
    else:
        print('JOGADA INVÁLIDA')
elif maquina == 1:
    if jogador == 0:
        print('MAQUINA VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('VOCÊ VENCEU')
    else:
        print('JOGADA INVÁLIDA')
elif maquina == 2:
    if jogador == 0:
        print('VOCÊ VENCEU')
    elif jogador == 1:
        print('MAQUINA VENCEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')




