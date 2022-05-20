#faça um programa que leia um numero inteiro qualquer e mostre na tela sua tabuada.

tabuada = int(input('tabuada de: '))
valor = 1
print('*' * 18)
print('tabuada de {}'.format(tabuada, valor))
print('*' *18)
while(valor <= 10):
    print('{} x {} = {}'.format(valor, tabuada,(valor * tabuada)))
    valor = valor +  1

