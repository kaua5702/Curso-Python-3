numeros = []
while True:
    n = int(input('Digite um número inteiro: '))
    numeros.append(n)
    
    resposta = input('Deseja continuar? (s/n) ')
    if resposta.lower() != 's':
        break
    
d = sorted(numeros, reverse=True)
print(f'Foram digitados {len(numeros)} elementos')
print(f'Em ordem decrescente {d}')
    
if 5 in numeros:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')
