jogadores = []

while True:
    print('-' * 30)
    dados = {}
    
    nome = input('Nome: ')
    dados['Nome'] = nome

    partidas = int(input('Partidas: '))
    gols = []

    for i in range(partidas):
        g_m = int(input(f'Quantos gols na {i + 1}ª partida: '))
        gols.append(g_m)
    print('-' * 30)

    dados['gols'] = gols
    dados['total'] = sum(gols)

    jogadores.append(dados)

    resposta = input('Deseja continuar: (s/n) ')
    if resposta.lower() != 's':
        break


print('=-=' * 20)
print(f"{'N°':<3} {'NOME':>15} {'GOLS':<25} {'TOTAL':<6}")
print('-' * 55)


for i, jogador in enumerate(jogadores):
    gols_formatados = ', '.join(str(g) for g in jogador['gols']) 
    print(f"{i+1:<3} {jogador['Nome']:<15} {gols_formatados:<25} {jogador['total']:<6}")


buscar = input('\nDigite o nome do jogador que deseja buscar: ').capitalize()
encontrado = False

print('=-=' * 20)
print(f"{'DESEMPENHO':>35}")
print('=-=' * 20)

for jogador in jogadores:
    if jogador['Nome'].lower() == buscar.lower():
        print(f"\nDados de {buscar}:")
        print(f"Gols por partida: {jogador['gols']}")
        for i, g in enumerate(jogador['gols']):
            print(f'  => Partida {i + 1}: {g} gols')
        print(f"Total de gols: {jogador['total']}")
        encontrado = True
        break

if not encontrado:
    print(f"\nJogador '{buscar}' não encontrado.")

