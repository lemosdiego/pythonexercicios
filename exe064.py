#crie um programa que leia varios numeros inteiros pelo teclado.
#o programa só vai parar quando o usuário digitar o valor 999
#que é a condição de parada, no finaç mostre quantos numeros foram digitados
#e mostre a soma entre eles (desconsiderando o flog)

num = c = s = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    s += num
    c += 1
    num = int(input('Digite um número [999 para parar]: '))
print('você digitou {} números e a soma entre eles é igual a {}'. format(c, s))