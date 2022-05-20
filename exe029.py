#escreva um programa que leia a velocidade de um carro, se ele ultrapassar
#80 km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7
#por cada km acima do limite.

from time import sleep
print('-=-' *20)
print('olá, boa viagem e dirija com segurança!!!')
print('-=-' * 20)
v = float(input('qual a velocidade em km/h? '))
if v > 80:
    print('você foi multado')
    multa = (v-80) * 7
    print('sua multa é de R$ {:.2f}!'.format(multa))
else:
    print('velocidade permitida, siga com segurança!')
