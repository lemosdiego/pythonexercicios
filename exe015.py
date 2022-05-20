# Escreva um programa que pergunte a quantidade de KM pecorridos por um carro alugado
#  e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar sabendo
#  que o carro custa R$ 60 por dia e R$0.15 por KM rodado.

km_percorrido = float(input('digite a quantidade de KM percorridos: '))
dias_alugados = int(input('digita a quantidade de dias alugados: '))
dia = dias_alugados * 60.00
km = km_percorrido * 0.15
valor = dia + km
print('valor total a pagar: R${}'.format(valor))

