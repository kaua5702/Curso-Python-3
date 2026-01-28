v1 = int(input('Digite um número inteiro: '))
v2 = int(input('Digite um número inteiro: '))
v3 = int(input('Digite um número inteiro: '))
v4 = int(input('Digite um número inteiro: '))

numeros = (v1, v2, v3, v4)
print(f'\nTupla criada: {numeros}')

if 9 in numeros:
    nove = tuple.count(9)
    print(f'O número 9 aparece {nove} vez/es')

if 3 in numeros:
    tres = numeros.index(3)
    print(f'O número 3 aparece pela primeira vez na posição {tres}')

print('Numeros pares digitados: ')
for i in tuple:
    if i % 2 == 0:
        print(i)