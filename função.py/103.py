def ficha(nome="<<desconhecido>>", gols=0):
    print('-' * 40)
    entrada_nome = input('Nome do jogador: ')
    entrada_gols = input('Total de gols: ')
    
    if entrada_nome:
        nome = entrada_nome.capitalize()
    
    if entrada_gols:
        gols = int(entrada_gols)
    
    print('-' * 40)
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

ficha()