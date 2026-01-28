from time import sleep


def maior(* num):
    print('-=' * 30)
    print('Analisando os valores passados...')
    sleep(1)

    if not num:
        print('Nenhum valor informado.')
        sleep(0.5)
        return

    print('Valores informados:', end=' ')
    for n in num:
        print(n, end=' ', flush=True)
        sleep(0.5)
    print(f'\nForam informados {len(num)} valores ao todo.')
    sleep(0.5)
    
    
    maior_valor = num[0]
    for n in num:
        if n > maior_valor:
            maior_valor = n
    print(f'O maior valor informado foi {maior_valor}')
    sleep(0.8)


maior(10, 47, 35, 9)
maior(90, 100, 250, 87, 15)
maior(9, 32, 27)
maior()