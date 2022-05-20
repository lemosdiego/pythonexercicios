#refaça o desafio 51 lendo o primeiro termo e a razão de uma PA
#mostrando os 10 primeiros termos da progressao usando a estrutura while
from time import sleep
print('GERADOR DE PA')
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
print('CALCULANDO!')
sleep(3)
termo = primeiro
c = 1
while c <= 10:
    print('{} - '.format(termo), end='')
    termo = termo + razao
    c += 1
print('FIM!')
