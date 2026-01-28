pilha = []
ex = input('Digite uma expressão: ')

for simbolo in ex:
    if simbolo == ex:
        pilha.append('(')

    elif simbolo == ')':
        pilha.remove(ex)
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Expressão válida!')
else:
    print('Expressão inválida!')
