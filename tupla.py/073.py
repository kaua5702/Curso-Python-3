brasileirao_2025 = (
    'Flamengo', 'Palmeiras', 'Cruzeiro', 'Mirassol', 'Bahia',
    'Botafogo', 'São Paulo', 'RB Bragantino', 'Corinthians', 'Fluminense',
    'Internacional', 'Ceará', 'Grêmio', 'Atlético-MG', 'Vasco',
    'Santos', 'Vitória', 'Juventude', 'Fortaleza', 'Sport'
)

print('Os primeiros 5 colocados são:')
for posicao, time in enumerate(brasileirao_2025[0 : 6], start=1):
    print(f'{posicao}° - {time}')
    
print(f'\nOs últimos 4 colocados são:')
for posicao, time in enumerate(brasileirao_2025[-4:], start=17):
    print(f'{posicao}° - {time}')
    
print(f'\nEm ordem alfabética:')
times_ordenados = tuple(sorted(brasileirao_2025))
for time in times_ordenados:
   print(time)
    
if 'Chapecoense' in brasileirao_2025:
    print(f'\nChapecoense está na posição {brasileirao_2025.index('Chapecoense')}')
else:
    print(f'\nA chapecoense não está na serie A')