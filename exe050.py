#desenvolva um programa que leia seis numeros inteiros e mostre a soma daqueles que forem pares,
#se o valor digitado for impar, desconsidere-o.

soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite um número: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('você informou {} pares e a soma é {}'.format(cont, soma))

