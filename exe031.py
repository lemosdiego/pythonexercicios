#desenvolva um programa que pergunte a distancia de uma viagem em km e calcule
#o preço da passagem, cobrando R$0,50 para viagens de ate 200 km e R$0,45 para viagens mais longas.

d = float(input('informe a distância da viagem: '))
print('olá, você irá percorrer {}'.format(d))
if d <= 200:
    p = d * 0.50
else:
    p = d * 0.45
print('sua passagem vai custar R${}'.format(p))
