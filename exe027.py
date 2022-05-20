#faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente

nome = str(input('escreva seu nome completo: ')).strip()
n = nome.split()
print('seu primeiro nome é {}'.format(n[0]))
print('seu ultimo nome é {}'.format(n[len(n)-1]))

