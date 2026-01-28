def leiaInt(msg):
    while True:
        try:
            entrada = input(msg)
            
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue

        except (KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0

        else:
            return int(entrada)
    
def leiaFloat(msg):
    while True:
        try:
            entrada = float(input(msg))
        
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número real válido.\033[m')
            continue

        except (KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')

        
        else:
            return entrada

i = leiaInt('Digite um número inteiro: ')
r = leiaFloat('Digite um número real: ')

print(f'O número inteiro é {i} e o real é {r}')