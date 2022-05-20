#crie um programa que leia varios numeros inteiros pelo teclado.no final da execução
#mostre a média de todos os valores, qual foi o menor e qual foi o maior valores lidos
#o programa deve perguntar ao usuario se ele quer ou nao continuar a digitar valores.

r = 'Ss'
soma = quant = media = 0
while r in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print('você digitou {} números e a média foi {}'.format(quant, media))
print('o maior valor foi {} e o menor foi {}'.format(maior, menor))

