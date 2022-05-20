#faça um programa que leia a largura de uma parede em metros, calcule a sua área e a
#quantidade de tinta necessaria para pinta-la,sabendo que a cada litro de tinta
#pinta uma area de 2m quadrados.

largura =float(input('qual a largura da parede: '))
altura = float(input('qual a altura da parede: '))
area = altura * largura
print('sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(largura, altura, area))
tinta = area / 2
print('para pintar uma area de {} voce precisa de {}L de tinta' .format(area, tinta))





