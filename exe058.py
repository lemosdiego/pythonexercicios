#melhore o jogo do desafio 28 onde o computador pensa em um numero entre 0 e 10
#só que agora ele vai advinhar até acertar, mostrando no final quantos palpites foram necessarios para vencer

from random import randint
computador = randint(0, 10)
print('Olá, pensei em um número entre 0 e 10, tente dvinhar... ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Escolha um número entre 0 e 10: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente de novo!')
        elif jogador > computador:
            print('Menos... Tente de novo!')
print('Você acertou com {} tenativas, parabens!'.format(palpites))


