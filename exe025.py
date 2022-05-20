#crie um programa que leia o nome completo de uma pessoa e diga se ela tem "silva" no nome

n = str(input('digite seu nome completo: ')).split()
print('seu nome tem silva? {}'.format('silva' in n.lower()))