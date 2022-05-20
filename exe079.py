#crie um programa osde o usuario possa digitar varios valores numericos e cadastreos em uma lists
#caso o numero ja exista la dentro ele nao sera adcionado. No final, serão exibidos todos os valores
#unicos digitados, em ordem crescente.



num = list()
while True:
    n = int(input('digite um numero: '))
    if n not in num:
        num.append(n)
        print('valor adcionado...')
    else:
        print('valor duplicado, tente novamente...')
    r = str(input('deseja continuar? [S/N]'))
    if r in 'Nn':
        break
print('=' * 40)
num.sort()
print(f'você digitou os valores {num}')
