#refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de
#triãngulo será formmado.
#equilátero-todos os lados iguais
#isósceles-dois lados iguais
#escaleno-todos os lados diferentes

print('-=-'*20)
print('analisador de triângulos')
print('-=-'*20)
r1 = float(input('primeiro segmento: '))
r2 = float(input('segundo segmento: '))
r3 = float(input('terceiro segmnento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    equi = r1 == r2 == r3
    print('os segmentos acima formam um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('os segmentos acima não formam um TRIÂNGULO!')