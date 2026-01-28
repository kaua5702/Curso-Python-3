import time

def contador(inicio, fim, passo):
    print('-=' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    time.sleep(1.5)
    
    if passo == 0:
        passo = 1
    if passo < 0:
        passo = -passo

    if inicio < fim:
        for i in range(inicio, fim + 1, passo):
            print(i, end=' ', flush=True)
            time.sleep(0.5)
        print('FIM!')
    
    else:
        for i in range(inicio, fim - 1, -passo):
            print(i, end=' ', flush=True)
            time.sleep(0.5)
        print('FIM')

 
contador(1, 10, 1)

contador(10, 0, 2)

print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
time.sleep(1)
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
