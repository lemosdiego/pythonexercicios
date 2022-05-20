#desenvolva um programa que leia quatro valores pelo teclado
#e guarde-os em uma tupla, no final mostre:
#quantas vezes apareceu o valor 9
#em que posição foi digitado o valor 3
#quais foram os numeros pares


v = (int(input('digite um valor: ')),
     int(input('digite um valor: ')),
     int(input('digite um valor: ')),
     int(input('digite um valor: ')))
print(f'você digitou os valores: {v}')
print(f'o valor 9 foi digitado {v.count(9)} vezes')
if 3 in v:
    print(f'o valor 3 apareceu na {v.index(3)+1}° posição')
else:
    print('você nao digitou o valor 3')
print('os valores pares digitados foram: ', end='')
for n in v:
    if n % 2 == 0:
        print(n, end=' ')




