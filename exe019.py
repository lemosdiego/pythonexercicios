#um professor quer sortear um de seus quatro alunos para apagar o quadro,
#faça um programa que ajude ele lendo o nome deles e
#escrevendo o nome dos escolhidos.

from random import choice
a1 = input('primeiro aluno: ')
a2 = input('segundo aluno: ')
a3 = input('terceiro aluno: ')
a4 = input('quarto aluno: ')
lista = [a1, a2, a3, a4]
esc = choice(lista)
print('o escolhido foi {} '.format(esc))
