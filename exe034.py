#escreva um programa que pergunte o salario de um funcionario e calcule
#o valor do seu aumento, para salarios superiores a R$1.250,00 caucule um aumento de 10%
#para inferiores ou iguais o aumento é de 15%.

sa = float(input('qual o seu salario atual? '))
if sa <= 1250:
    v = sa + (sa * 15 / 100)
else:
    v = sa + (sa * 10 / 100)
print('o valor atual de R${} passa a ser de {}'.format(sa, v))


