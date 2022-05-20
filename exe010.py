#crie um programa que leia quanto de dinheiro uma pessoa tem na carteira,
#e mostre quantos dolares ela pode comprar, considerando que 1 dolar custa 3,27 reais

real = float(input('você possui R$: '))
dolar = (real / 3.27)
print('voce pode comprar US$: {:.2f}'.format(dolar))



