#faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade se
#se ele ainda vai se alistar no serviço militar
#se é a hora de se alistar
#se já passou o tempo do alistamento
#seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

print('SERVIÇO DE ALISTAMENTO MILITAR!')
ano = 2022
nasc = int(input('Digite seu ano de nascimento: '))
atual = ano - nasc
print('sua idade é de {} anos'.format(atual))
if atual < 18:
    saldo = 18 - atual
    print('\033[33mVocê deve se alistar em {} ano(s)'.format(saldo))
    ano1 = ano + saldo
    print('Seu alistamento será em {}'.format(ano1))
elif atual == 18:
    print('\033[32mVocê tem {} anos, É hora de se ALISTAR!'.format(atual))
elif atual > 18:
    saldo = atual - 18
    print('\033[31mJá passou o prazo, comparecer imediatamente a junta militar!'.format(saldo))
    ano2 = ano - saldo
    print('Seu alistamento foi em {}'.format(ano2))

