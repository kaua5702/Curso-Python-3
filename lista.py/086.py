matriz = [[], [], []]

for l in range(3):

    for c in range(3):

        valor = int(input(f'Digite um valor para [{l}, {c}]: '))
        matriz[l].append(valor)

for linha in matriz:
    for elemento in linha:
        print(f'[ {elemento:^5} ]', end=' ')
    print()

