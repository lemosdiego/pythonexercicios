#crie um programa onde o usuario digite uma expressao qualquer que use parenteses
#seu aplicativo devera analizar se a expressao passada esta com os parenteses
#abertos e fechados na ordem correta



expr = str(input('digite a expressão: '))
p = []
for simb in expr:
    if simb == '(':
        p.append('(')
    elif simb == ')':
        if len(p) > 0:
            p.pop()
        else:
            p.append(')')
            break
if len(p) == 0:
    print('sua expressão é válida!')
else:
    print('sua expressão é inválida!')