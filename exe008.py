#escreva um programa que leia um valor em metros e o exiba convertido em centrimetros e milimetros.

m = float(input('metros: '))
cm = m * 100
mm = m * 1000
print ('{} Metros corresponde a {} Centimetros '.format(m, cm))
print('{} Metros corresponde a {} Milimetros'.format(m, mm))