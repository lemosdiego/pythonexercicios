#refaça o desafio 9, mostrando a tabuada de um numero que o usuario escolher
#só que agora utilizando um laço for.


tab = int(input('Tabuada de? '))
for t in range(1, 11):
    print('{} x {} = {}'.format(tab, t, tab*t))
