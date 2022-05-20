#escreva um programa que leia dois numeros inteiros e compare-os mostrando, na tela uma mensagem
#o primeiro valor é maior, o segundo valor é maior, não existe valor maior os dois sao iguais

n1 = int(input('Digite um valor inteiro: '))
n2 = int(input('Digite outro valor inteiro: '))
if n1 > n2:
    print('\033[32mO PRIMEIRO valor é maior!')
elif n2 > n1:
    print('\033[34mO SEGUNDO valor é maior!')
else:
    print('\033[33mOs dois são IGUAIS!')