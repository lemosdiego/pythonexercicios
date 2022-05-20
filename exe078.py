#faça um programa que leia 5 valores numéricos e guarde-os em uma lista
#no final mostre qual foi o maior e o menor valor digitados e suas respectivas posições na lista


num = []
maior = 0
menor = 0
for c in range(0, 5):
    num.append(int(input(f'digite um valalor para a posição {c}: ')))
    if c == 0:
        maior = menor = num[c]
    else:
        if num[c] > maior:
            maior = num[c]
        if num[c] < menor:
            menor = num[c]
print('-=-' * 30)
print(f'você digitou os valores {num} ')
print(f'o maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(num):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'o menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(num):
    if v == menor:
        print(f'{i}...', end='')
print()