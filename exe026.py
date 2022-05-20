#faça um programa que leia uma frase e mostre:
#                quantas vezes aparece a letra 'A'
#                em que posição aparece pela primeira vez
#                em que posição aparece a última vez

frase = str(input('escreva uma frase: ')).lower().strip()
print('a letra A aparece {} vezes'.format(frase.count('a')))
print('a letra A aparece na posição {}'.format(frase.find('a')+1))
print('a letra A aparece por último na posição {}'.format(frase.rfind('a')+1))


