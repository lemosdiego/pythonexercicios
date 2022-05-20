#crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem
#no final de acordo com a média atingida.
#media abaixo de 5.0:
#reprovado
#media entre 5.0 e 6.9:
#recuperação
#media 7.0 ou superior:
#aprovado

print('MÉDIA DO ALUNO')
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('digite sua segunda nota: '))
media = (nota1 + nota2) / 2
print('A soma das notas é igual a: {}, e sua média é {}: '.format(nota1 + nota2, media))
if media < 5.0:
    print('\033[31mSua média é {} ,infelizmente Você foi REPROVADO!'.format(media))
elif media >= 5.0 and media < 7:
    print('\033[33mSua média é {} ,Você está em RECUPERAÇÃO!'.format(media))
elif media >= 7.0:
    print('\033[32mSua média é {} ,Parabéns você foi APROVADO!'.format(media))
