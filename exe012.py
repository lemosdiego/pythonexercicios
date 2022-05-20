#faça um programa que leia o preço de um produto
#e mostre seu novo preço com 5% de desconto

valor_produto = float(input('qual o preço do seu produto R$: '))
desconto_produto = valor_produto * 5 / 100
preço_final = valor_produto - desconto_produto
print('o preço produto com 5% de desconto é R$: {:.2f}'.format(preço_final))
