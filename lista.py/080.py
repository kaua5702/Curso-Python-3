lista = []

for i in range(5):
    num = int(input(f'Digite o {i+1}º número: '))
    
    if len(lista) == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista.')
                break
            pos += 1

print(f'\nLista ordenada: {lista}')
