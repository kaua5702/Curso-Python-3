from datetime import datetime

def voto(ano_nasc):
    ano_atual = datetime.today().year
    idade = ano_atual - ano_nasc
    
    if idade < 16:
        return 'Você não vota'

    elif 16 <= idade < 18 or idade >= 65:
        return 'Seu voto é opicional'
           

    else:
        return 'Seu voto é obrigatório' 

ano = int(input('Digite seu ano de nascimento: '))
voto(ano)