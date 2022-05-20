# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.


lista1 = list()
lista2 = list()
naior = menor = 0
while True:
    lista1.append(str(input('Nome: ')))
    lista1.append(str(input('Peso: ')))
    if len(lista2) == 0:
        maior = menor = lista1[1]
    else:
        if lista1[1] > maior:
            maior = lista1[1]
        if lista1[1] < menor:
            menor = lista1[1]
    lista2.append(lista1[:])
    lista1.clear()
    resp = str(input('Deseja prosseguir? [S/N] '))
    if resp in 'Nn':
        break
print(f'você cadastrou {len(lista2)} pessoas')
print(f'os menores pesos cadastrados foram {maior} kg ', end='')
for p in lista2:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print()
print(f'o maiores peso encontrado foram {menor}kg ', end='')
for p in lista2:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
print('obrigado!')



