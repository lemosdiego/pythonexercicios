# Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno

def area(larg, com):
    a = larg * com
    print(f'a area de um terreno {larg}x{com} é de {a:.2f}m²')


print('-' * 30)
print('   CONTROLE DE TERRENO')
print('-' * 30)
l = float(input('qual a largura do terreno? '))
c = float(input('qual o comprimento do compprimento? '))
area(l, c)




#print(f'a medida desse terreno é igual a {c}m²')


