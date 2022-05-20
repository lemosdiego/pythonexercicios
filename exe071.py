# crie um programa que simule um funcionamento de um caixa eletronico
#no inicio pergunte ao o usuario qual valor será sacado (numero inteiro)
#e o programa vai informar qquantas cedulas de cada valor serao entregues
#considere que o caixa possui R$50 R$20 R$10 R$01


total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('nome do produto: '))
    preço = float(input(' preço do produto R$ '))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    resp = ''
    while resp not in 'SN':
        resp = str(input(' Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'o total da compra foi R$ {total:.2f}')
print(f'temos {totmil} produtos custando mais de R$ 1000')
print(f'o produto mais barato foi {barato} que custa R${menor:.2f}')

