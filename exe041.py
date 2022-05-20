#a confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta
#e mostre sua categoria de acordo com a idade:
#até 9 anos: mirim
#até 14 anos: infantil
#até 19 anos: junior
#até 25 anos: sênior
#acima: master

print('-=-' * 15)
print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print('-=-' * 15)
from datetime import date
ano_atual = date.today().year
nasc = int(input('Qual a data de nascimento do Atleta? '))
idade = ano_atual - nasc
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('O atleta irá entrar na Categoria MIRIM!'.format(idade))
elif idade >= 10 and idade < 15:
    print('O atleta irá entrar na Categoria INFANTIL!'.format(idade))
elif idade >= 15 and idade < 20:
    print('O atleta irá entrar na Categoria JUNIOR'.format(idade))
elif idade >= 20 and idade < 26:
    print('O atleta irá entrar na Categoria SÊNIOR'.format(idade))
elif idade > 25:
    print('O atleta pertence a Categoria MASTER'.format(idade))

