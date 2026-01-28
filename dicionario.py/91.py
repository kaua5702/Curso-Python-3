import random
import time


resultado = {
    'Jogador1': random.randint(1, 6),
    'Jogador2': random.randint(1, 6),
    'Jogador3': random.randint(1, 6),
    'Jogador4': random.randint(1, 6),

}


for p, d in resultado.items():
    print(f'{p} : {d}')
    time.sleep(1)

print('\n')
time.sleep(1)

print('=-=' * 30)
time.sleep(1)
print(f'{'Ranking dos jogadores':^80}')
time.sleep(1)
print('=-=' * 30)
time.sleep(1)
print('\n')
time.sleep(1)

resultados_ordenados = sorted(resultado.items(), key=lambda item: item[1], reverse=True)

for i, (p, d) in enumerate(resultados_ordenados, start=1):
    print(f'{i}° lugar: {p} com {d}')
    time.sleep(1)

print('\n')
time.sleep(1)
