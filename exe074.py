#crie um programa que vai gerar 5 numeros aleatórios e colocar uma tupla
#depois disso mostre a listagem de numeros gerados e tambem indique o menor e o maior
#valor que estao na tupla


from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'os valores sorteados foram: {n}')
print(f'o maior valor sorteado foi {max(n)}')
print(f'o menor valor sorteado foi {min(n)}')