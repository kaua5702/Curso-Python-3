import random
import time

jogos = []
n = int(input('Quantos jogos serão gerados? '))

for i in range(n):
    jogo = []
    while len(jogo) < 6:
        palpite = random.randint(1, 60)
        if palpite not in jogo:
            jogo.append(palpite)
    palpite.sort()
    jogos.append(jogo)

print('-=' * 5, f'SORTEANDO {n} JOGOS', '-=' * 5)
for i, jogo in enumerate(jogos):
    print(f'Jogo {i+1}: {jogo}')
    time.sleep(1)