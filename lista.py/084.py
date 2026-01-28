pessoas = list()
total = 0

while True:
    nome = input('Digite seu nome: ')
    peso = float(input('Digite seu peso: '))
    pessoas.append([nome, peso])
    total += 1

    if len(pessoas) == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso

        if peso < menor:
            menor = peso
    
    
    resposta = input('Deseja continuar: (s/n) ')    
    if resposta.lower() != 's':
        break

print(f'{total} pessoas foram cadastradas')
print(f'As pessoas mais pesadas {maior}kg foram: ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print(f'As pessoas mais leves {menor}kg foram: ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')