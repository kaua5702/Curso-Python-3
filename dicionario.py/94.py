dados = []
soma_idade = 0
mulheres = []
acima_m = []

while True:
    pessoa = {}
    nome = input('Nome: ')
    pessoa['Nome'] = nome.capitalize()
    idade = int(input('Idade: '))
    pessoa['idade'] = idade
    sexo = input('Sexo: (M/F)')
    pessoa['sexo'] = sexo.upper()
    
    dados.append(pessoa)

    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['Nome'])



    resposta = input('Deseja continuar? (s/n)')
    if resposta not in 'Ss':
        break

for pessoa in dados:
    soma_idade += pessoa['idade']
media = soma_idade / len(dados)


for pessoa in dados:
    if pessoa['idade'] > media:
        acima = acima_m.append(pessoa['idade'])

print('=-=' * 20)
print(f"{'DADOS':>35}")
print('=-=' * 20)

print(f'\nTotal de pessoas cadastradas: {len(dados)}')
print(f'Média de idade: {media:.1f} anos')
print(f'Mulheres cadastradas: {", ".join(mulheres) if mulheres else "Nenhuma"}')
print(f'Pessoas com idade acima da média: {", ".join(acima_m) if acima_m else "Nenhuma"}')