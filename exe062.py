#melhore o desafio anterior perguntando para o usuario se ele deseja mostrar mais alguns termos
#o programa encerra quando ele disser que nao quer mostrar os termos

from time import sleep
print('GERADOR DE PA')
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
print('CALCULANDO!')
sleep(3)
termo = primeiro
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= 10:
        print('{} -'.format(termo), end='')
        termo += razao
        c += 1
    print('PAUSA')
    m = int(input('Você deseja mostrar mais termos? '))
print('FIM!')
