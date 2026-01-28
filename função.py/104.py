def leiaInt(msg):
    entrada = input(msg)
    if entrada.isnumeric():
        return int(entrada)
    else:
        print('\033[31mERRO! Digite um número válido.\033[m')


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')