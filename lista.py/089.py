notas = []

while True:
    nomes = input('Nome: ')
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    
    notas.append([nomes, n1, n2, media])

    resposta = input('Deseja continuar? (s/n) ')
    if resposta.lower() != 's':
        print('=-=' * 10)
        print(f'{"NOME":<20}{"MÉDIA":>10}')
        print('-' * 30)
        
        for aluno in notas:
            print(f'{aluno[0]:<20}{aluno[3]:>10.2f}')
        while True:
            nome = input('Mostrar notas de qual aluno? (999 interrompe) ')
            if nome == '999':
                print('Encerrando...')
                break
        
            encontrado = False
            for aluno in notas:
                if aluno[0].lower() == nome.lower():
                    print(f'{aluno[0]:<20}{aluno[1]:>10.2f}{aluno[2]:>10.2f}')
                    encontrado = True
                    break
       
                if not encontrado:
                    print('Aluno não encontrado.')
        break