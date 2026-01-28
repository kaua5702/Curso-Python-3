dados = {}

nome = input('Nome: ')
dados['Nome'] = nome

partidas = int(input('Partidas: '))
gols = []

for i in range(partidas):
    g_m = int(input(f'Quantos gols na {i + 1}ª partida: '))
    gols.append(g_m)

dados['gols'] = gols
dados['total'] = sum(gols)

print('=-=' * 20)
print(f"{'DESEMPENHO':>35}")
print('=-=' * 20)
print('\n')

print(f'O jogador {dados['Nome']} jogou {partidas} partidas')

for i in range(partidas):
    print(f'  => Na {i + 1}ª partida, fez {gols[i]} gols')
print(f'Foi um total de {dados['total']}')