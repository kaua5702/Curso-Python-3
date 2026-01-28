matriz = [[], [], []]
cont = 0


for l in range(3):

    for c in range(3):

        valor = int(input(f'Digite um valor para [{l}, {c}]: '))
        matriz[l].append(valor)
        cont += 1
        if valor % 2 == 0:
            soma = valor + cont

for linha in matriz:
    for elemento in linha:
        print(f'[ {elemento:^5} ]', end=' ')
    print()


for l in range(3):
    soma_terceira_coluna += matriz[l][2]

    
maior_segunda_linha = max(matriz[1])

print(f'A soma dos valores pares é {soma}')
print(f'A soma dos valores da terceira coluna é {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é {maior_segunda_linha}')

