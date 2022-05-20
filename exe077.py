#crie um programa que tenha uma tupla com varias palavras(não usar acentos).
#Depois disso você deve mostrar, para xada palavra, quais são suas vogais.


palavras = ('WASHINGTON', 'CORINTHIANS', 'CANADA',
            'EUROPA', 'VIAGEM', 'AEROPORTO', 'FUTURO',)
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')