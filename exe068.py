#faça um programa que jogue par iou impar com o computador, o jogo só será interrompido
#quando o jogador PERDER , mostrando o total de vitorias consecultivas que conquistou
#no final do jogo

from random import randint
print('EU TE DESAFIO NO PÁR OU ÍMPAR')
v = 0
while True:
    jog = int(input('Diga um valor: '))
    comp = randint(0, 10)
    total = jog + comp
    tipo = ''
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'você escolheu {jog} e o computador {comp} no total de {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('você VENCEU!')
            v += 1
        else:
            print('você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('você VENCEU!')
            v += 1
        else:
            print('você PERDEU!')
            break
        print('vamos mais uma vez?')
print(f'Fim de jogo você venceu {v} vezes!')


