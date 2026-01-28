numeros = [[], []]

for n in range(7):
    numero = int(input(f'Digite o {n+1}° número: '))
    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)

numeros[0].sort()
numeros[1].sort()

print(f'Os números pares digitados foram {numeros[0]}')
print(f'Os números ímpares digitados foram {numeros[1]}')