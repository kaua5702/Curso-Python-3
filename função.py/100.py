import random
import time


numeros = []

def sorteia(numeros):
    print('🎲 Sorteando 5 valores da lista:', end=' ')
    for i in range(5):
        num = random.randint(1, 100)
        numeros.append(num)    
        print(num, end=' ', flush=True)
        time.sleep(0.3)
    print('✅ PRONTO!')


def somaPar(numeros):
    soma = 0
    print('🧮 Somando os valores pares de:', end=' ')
    time.sleep(0.5)
    for i in numeros:
        print(i, end=' ', flush=True)
        time.sleep(0.3)
        if i % 2 == 0:
            soma += i
    print(f'\nTemos: {soma}')
    time.sleep(0.5)
        

sorteia(numeros)
somaPar(numeros)
