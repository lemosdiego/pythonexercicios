# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar
# quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando
# tudo em uma lista composta.


print('=' * 30)
print('Gerador de jogos da mega sena')
print('=' * 30)
from random import randint
quant = int(input('quantos jogos vc quer fazer? '))
from random import randint
tot = 1
lista = list()
jogos = list()
while tot <= quant:
    cont = 0
    while True:
    num = randint(1, 60)
    if num not in lista:
        lista.append(num)
        cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'os numeros sorteados foram {lista}')

