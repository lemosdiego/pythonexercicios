# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

par = mai = scol = 0
matriz = [[0, 0, 0, ], [0, 0, 0, ], [0, 0, 0, ]]
for v in range(0, 3):
    for c in range(0, 3):
        matriz[v][c] = int(input(f'digite um valor para [{v}, {c}]: '))
print()
for v in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[v][c]:^5}]', end='')
        if matriz[v][c] % 2 == 0:
            par += matriz[v][c]
    print()
print('=' * 30)
print(f'a soma de todos valores digitadoe é {par}')
for v in range(0, 2):
    scol += matriz[v][2]
print(f'a soma dos valores da terceira coluna á {scol}')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'o maior valor da segunda linha é {mai}')

