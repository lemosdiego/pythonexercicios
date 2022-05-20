#escreva um programa para aprovar o emprestimo bancario para a compra de uma casa
#o programa vai perguntar o valor da casa, o salario do comprador e em quantos anos vai pagar.
#calcule o valor da prestação mensal, sabendo que ela nao pode exceder 30% do salario ou então o emprestimo sera negado.


print('mCALCULO DE EMPRESTIMO BANCARIO')
casa = float(input('QUAL O VALOR DA CASA? '))
salario = float(input('QUAL SEU SALÁRIO MENSAL? '))
anos = int(input('EM QUANTOS ANOS VOCE DESEJA PAGAR? '))
meses = anos * 12
parcelas = casa / meses
minimo = salario / 100 * 30
if parcelas <= minimo:
    print('\033[32mPARABÉNS SEU EMPRESTIMO FOI APROVADO! O VALOR'
          'DAS PARCELAS SERÁ DE R${:.2f} EM {} MESES'.format(parcelas, meses))
else:
    print('\033[31mINFELIZMENTE SEU EMPRESTIMO FOI NEGADO!,'
          'POIS O VALOR DAS PARCELAS É MAIOR QUE 30% DO SEU '
          'SALÁRIO MENSAL!')
