#crie uma tupla preenchida com os 20 primeiros colocados da tabela do brasileirao
#na ordem de colocação depois mostre
#apenas os 5 primeiros colocados
#os útimos 4 colocados da tabela
#uma lista com os times em ordem alfabetica
#em que posição da tabela está o time da chapecoense


tabela = ( 'Corinthians', 'palmeiras', 'santos', 'gremio',
           'cruzeiro', 'flamengo', 'vasco', 'chapecoense',
           'atletico mg', 'botafogo', 'atletico pa', 'bahia',
           'são paulo', 'fluminense', 'sport', 'vitoria',
           'coritiba', 'avai', 'ponte preta', 'atletico go')
for t in tabela:
    print(t)
print('-=' * 45)
print(f'Os cinco primeiros colocados são: {tabela[:5]}')
print('-=' * 45)
print(f'os quatro útimos são: {tabela[16:]}')
print('-=' * 45)
print(f'os times em ordem são: {sorted(tabela)}')
print('-=' * 45)
print(f'A chapecoense está na {tabela.index("chapecoense")+1}° posição')
print('-=' * 45)

#print(f'os cinco primeiros colocados são {tabela[:6]}')
#print(f'os quatro últimos colocados são{tabela[16:]}')
#print(f'os times em ordem alfabética são {}')