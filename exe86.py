# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

matriz = [[0, 0, 0, ], [0, 0, 0, ], [0, 0, 0,]]
for v in range(0, 3):
    for c in range(0, 3):
        matriz[v][c] = int(input(f'digite um valor para [{v}, {c}]: '))
print()
for v in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[v][c]:^5}]', end='')
    print()




