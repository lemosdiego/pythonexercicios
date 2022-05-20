#crie um programa que leia o ano de nascimento de sete pessoas. no final mostre quantas pessoas
#ainda nao atingiram a maioridade e quantos ja são maiores.


from datetime import date
atual = date.today().year
maior = 0
menor = 0
for pess in range(1, 8):
    nasc = int(input('Digite o ano de nascimento da {} pessoa: '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('tivemos {} pessoas maior de idade'.format(maior))
print('tivemos {} pessoas menor de idade'.format(menor))

