from time import sleep
nome = input('QUAL SEU NOME? ')
print('ATENÇÃO {}'.format(nome))
print('APÓS A CONTAGEM REGRESSIVA, VOCÊ VAI RECEBER UMA LINDA MENSAGEM!')
for cont in range(10, -1, -1):
    print(cont)
    sleep(1)
print('QUERO COMER SEU CU, CUZCUZ')
