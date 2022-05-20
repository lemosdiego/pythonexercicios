#  Faça um algoritmo que leia o salario de um funcionário
# e mostre seu novo salário com 15% de aumento.


salario_atual = float(input('digite o salario atual R$: '))
aumento = salario_atual * 15/100
novo_salario = salario_atual + aumento
print('o novo salario +15% de aumento é R$: {:.2f}'.format(novo_salario))
