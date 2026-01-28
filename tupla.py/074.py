import random

numeros = tuple(random.randint(0, 20) for _ in range(5))
print('Números aleatórios gerados:', numeros)
print(f'O menor número é {min(numeros)}')
print(f'O maior número é {max(numeros)}')