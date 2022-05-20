#crie um programa que leia uma frase qualquer e diga se ela é
#um palindromo, desconsiderando os espaços.


frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('{} ao contrário é {}'.format(junto, inverso))
if inverso == junto:
    print('Uau! temos um palimdromo!')
else:
    print('A frase digitada não é um palimdromo!')
