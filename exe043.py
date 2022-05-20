#desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu imc e mostre seu status
#de acordo com a tabela abaixo:
#abaixo de 18.5 - abaixo do peso
#entre 18 e 25 - peso ideal
#de 25 até 30 - sobrepeso
#de 30 até 40 - obesidade
#acima de 40 - obesidade mórbida

print('-=-'*10)
print('CALCULADORA DE IMC')
print('-=-'*10)
peso = float(input('Digite seu PESO: '))
altura = float(input('Digite sua ALTURA: '))
imc = peso / (altura * altura)
print('Calculando seu peso e sua Altura... {} Kg e {} M '.format(peso, altura,))
print('seu IMC é de {:.2f}'.format(imc))
if imc < 18.5:
    print('VOCÊ ESTÁ ABAIXO DO PESO!')
elif imc >= 18.5 and imc < 25:
    print('PARABÉNS VOCÊ ESTÁ NO PESO IDEAL!')
elif imc > 25 and imc <= 30:
    print('VOCÊ ESTÁ COM SOBREPESO!')
elif imc >30 and imc <= 40:
    print('ATENÇÃO VOCÊ ESTA OBESO!')
elif imc > 40:
    print('OBESIDADE MÓRBIDA, CUIDE DA SUA SAÚDE!')

