def escreva(msg, cor='\033[m'):
    tamanho = len(msg) + 4
    print(cor + '~' * tamanho)
    print(cor + f'  {msg}')
    print(cor + '~' * tamanho + '\033[m')

while True:

    escreva('Sistema de ajuda PyHelp', '\033[37;42m')
    com = input('Função ou biblioteca > ').strip()
    
    if com.lower() == 'sair':
        escreva('Até logo', '\033[31;47m')
        break

    print('\n')
    escreva(f'Acessando o manual do comando {com}', '\033[34;47m')
    help(com)
