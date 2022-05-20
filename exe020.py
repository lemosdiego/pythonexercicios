#o mesmo professor do desafio anterior quer sortear a ordem de
#apresentação de trabalho dos alinos. faça um programa que
#leia o nomr dos quatro alunos e mostre a ordem sorteada.
import random
a1 = input('primeiro aluno: ')
a2 = input('segundo aluno: ')
a3 = input('terceiro aluno: ')
a4 = input('quarto aluno: ')
lista = [a1, a2, a3, a4]
sorteio = random.shuffle(lista)
print('a sequencia deve ser: {}'.format(lista))
