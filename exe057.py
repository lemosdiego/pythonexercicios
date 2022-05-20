#faça um programa que leia o sexo de uma pessoa, mas so aceite os valores M ou F
#caso esteja errado peça a digitação novamente até ter um valor correto

sexo = str(input('Qual o seu sexo [M/F]? ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos')).strip().upper()[0]
print('Sexo {} registrado'.format(sexo))
