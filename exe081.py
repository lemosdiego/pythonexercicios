#crie um programa que vai ler varios numeros e colocar em uma lista
#depois disso mostre:
#quantos numeros foram digitados
#a lista de valores ordenadas de forma decrescente
#se o valor 5 foi digitado e esta ou nao na lista


valores = list()
while True:
    valores.append(int(input('digite um valor: ')))
    resp = str(input('quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print(f'voce digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('o valor 5 faz parte da lista')
else:
    print('o valor 5 nao foi encontrado')
