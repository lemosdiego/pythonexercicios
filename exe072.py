#crie um programa que tenha uma tupla totalmente preenchida com uma contagem
#por extenso de 0 a 20. seu programa deverá ler um número pelo teclado entre 0 e 20
#e mostrálo por extenso.

cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco',
        'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
        'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
        'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
        num = int(input('Digite um numero entre 0 e 20: '))
        if 0 <= num <= 20:
                break
        print('tente novamente...', end='')
print(f'você digitou o número {cont[num]}')