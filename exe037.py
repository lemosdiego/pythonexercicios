#escreva um programa que leia um numero inteiro qualquer e peça pro usuario escolher qual será a base de conversão
#1-binário, 2-octal, 3-hexadecimal


num = int(input('digite um numero inteiro: '))
print(''' escolha uma das bases de conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opçao = int(input('sua opção: '))
if opçao == 1:
    print('convertido para BINÁRIO é igual a {}'.format(num, bin(num)))
elif opçao == 2:
    print('convertido para OCTAL é igual a {}'.format(num, oct(num)))
elif opçao == 3:
    print('convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)))
else:
    print('opçao inválida tente novamente!!')
