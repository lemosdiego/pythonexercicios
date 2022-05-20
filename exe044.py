#elabore um programa que calcule um valor a ser pago por um produto, considerando
#seu preço normal e condição de pagamento:
#- a vista dinheiro ou cheque 10% de desconto
#- a vista no cartão 5% de desconto
#- até 2 vezes no cartão preço normal
#- 3 vezes ou mais 20% de juros

valor = float(input('Qual o valor do produto? '))
print('Seu produto custa R$ {} '.format(valor))
print('''formas de pagamento: 
[ 1 ] a vista dinheiro ou cheque 10% de desconto;
[ 2 ] a vista no cartão 5% de desconto
[ 3 ] ate 2x no cartão preço normal
[ 4 ] 3x ou mais 20% de juros''')
opção = int(input('escolha uma opção: '))
if opção == 1:
    total = valor - (valor / 100 * 10)
    print('sua compra de R${} passa a custar R${}'.format(valor, total))
elif opção == 2:
    total = valor - (valor / 100 * 5)
    print('sua compra de R${} passa a custar R${}'.format(valor, total))
elif opção == 3:
    parcela = valor / 2
    print('sua compra será parcelada em 2x de R${} no cartão'.format(parcela))
    print('sua compra nao terá desconto e continuará custando R${} no final'.format(valor))
elif opção == 4:
    total = valor + (valor / 100 * 20)
    parc = int(input('em quantas parcelas vc deseja pagar? '))
    parcela = total / parc
    print('sua compra será parcelada em {}x de {} com juros'.format(parc, parcela))
    print('sua compra de R${} , custará {} no final'.format(valor, total))
else:
    print('opção inválida')







