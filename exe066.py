#crie um programa que leiavarios numeros inteiros no teclado. O programa só vai parar quando o usuário
#digitar 999, que é a condição de parada. No final mostre quantos numeros foram digitados, e qual foi
#a soma entre eles (desconsiderando o flog)


soma = cont = 0
while True:
    num = int(input('digite um numero [999 para parar]: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'a soma dos {cont} valores é igual a {soma}')

