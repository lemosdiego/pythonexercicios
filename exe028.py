#escreva um programa que faça o computador pensar em um numero inteiro
#entre 0 e 5 e faça o usuário tentar descobrir o número escolhido pelo
#computador.O programa devera escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 15)
print('pensando em um número entre 0 e 5. tente acertar...')
print('-=-' * 15)
jogador = int(input('chute um número: '))
print('PROCESSANDO...')
sleep(4)
if jogador == randint(0, 5):
    print('parabens você venceu!')
else:
    print('que pena você perdeu! o numero é {}'.format(computador))


