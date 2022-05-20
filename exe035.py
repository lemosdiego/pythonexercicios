#desenvolva um programa que leia o comprimento de três retas e diga ao osuário
#se eles podem ou não formar um triângulo.

print('-=-'*20)
print('analisador de triângulos')
print('-=-'*20)
r1 = float(input('primeiro segmento: '))
r2 = float(input('segundo segmento: '))
r3 = float(input('terceiro segmnento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('os segmentos acima formam um triângulo')
else:
    print('os segmentos acima não formam um triãngulo')