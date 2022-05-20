#faça um programa que calcule a soma de todos os numeros impares que sao multiplos de 3
#que se encontram no intervalo entre 1 e 500.

soma = 0
cont = 0
for inter in range(1, 501, 2):
    if inter % 3 == 0:
        soma = soma + inter
        cont = cont + 1
print('A SOMA DOS {} VALORES É IGUAL A: {}'.format(cont, soma))




