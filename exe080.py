#crie um programa onde o usuario passa a digitar cinco valores numéricos e cadastre-os em uma lista
#ja na posição correta de inserção srm usar o sort, no final mostre a lista ordenada na tela



lista = []
for c in range(0, 5):
    n = int(input('digite um numero: '))
    if c == 0:
        lista.append(n)
    elif n > lista[len(lista) - 1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print(f' os valores em ordem foram {lista}')
