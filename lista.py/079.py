n = []
while True:
    numero = int(input('Digite um número: '))
    if numero not in n:
        n.append(numero)
        print('Valor adicionado com sucesso!')
    else:  
        print('Esse número ja foi adicionado. Tente novamente')
        continue
    
    resposta = input('Deseja continuar? (s/n) ')
    if resposta.lower() != 's':
        n.sort()
        print(f'Você digitou os valores: {n}')
        break
