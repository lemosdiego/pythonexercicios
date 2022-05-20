#Desenvolva um programa que leia o nome, idade e sexo de quatro pessoas.
#No final do programa, mostre:
#A média de idade do grupo
#Qual o nome do homem mais velho
#Quantas mulheres tem menos de 20 anos

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomemaisvelho = ''
totmulherr20 = 0
for p in range(1,5):
   print('---- {}° PESSOA ----'.format(p))
   nome = str(input('Nome: ')).strip()
   idade = int(input('Idade: '))
   sexo = str(input('Sexo [M/F]: ')).strip()
   somaidade += idade
   if p == 1 and sexo in 'M/m':
       maioridadehomem = idade
       nomemaisvelho = nome
   if sexo in 'M/m' and idade > maioridadehomem:
           maioridadehomem = nome
           nomemaisvelho = nome
   if sexo in 'F/f' and idade < 20:
           totmulherr20 += 20
mediaidade = somaidade / 4
print('A MÉDIA DE IDADE DO GRUPO É DE {} ANOS'.format(médiaidade))
print('O homem mais velho se chama {} e tem {} anos!'.format(nomemaisvelho, maioridadehomem))