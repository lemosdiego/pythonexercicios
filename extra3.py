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
        if palpites <= 3:
            print('Parabéns você acertou com {} jogadas'.format(palpites))
        elif palpites <= 7:
            print('você acertou com {} jogadas, seu desempenho foi médio...'.format(palpites))
        elif palpites >= 10:
            print('Você acertou com {} jogadas, quam sabe na próxima '.format(palpites))

