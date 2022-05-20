#crie um programa que vai ler varios numeros e colocalos em uma lista.
#depois disso crie duas listas extras que vão conter apenas valores pares e os valores impares
#digitados respectivamente, ao final mostre o conteudo das 3 listas geradas


lista = []
pares = []
impares = []
while True:
    lista.append(int(input('digite um valor: ')))
    resp = str(input('quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'os numeros digitados foram {lista} ')
print(f'os valores pares foram {pares}')
print(f'os valores impares foram {impares}')