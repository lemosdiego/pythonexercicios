#crie um programa que leia o nomr competo de uma pessoa e mostre:
            #o nome com todas as letras maiusculas
            #o nome com todas menusculas
            #quantas letras tem ao todo sem considerar os espaços
            #quantas letras tem o primeiro nome


nome = str(input('digite seu nome completo: ')).strip()
print('analisando seu nome...')
print('seu nome em maiusculo é: {}'.format(nome.upper()))
print('seu nome em menusculo é: {}'.format(nome.lower()))
print('seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('seu primeiro nome tem {} letras'.format(nome.find(' ')))


