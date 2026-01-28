numeros = []
par = []
impar = []
for i in range(5):
    n = int(input('Digite um número: ')) 
    numeros.append(n)
    print(f'A lista completa é: {n}')

    if n % 2 == 0:
        par.append(n)
        print(f'A lista dos pares é: {par}')

    else:
        impar.append(n)
        print(f'A lista dos ímpares é: {impar}')