def notas(*n, situacao=False):
    """
    -> Calcula estatísticas sobre notas de alunos.
    :param n: uma ou mais notas (aceita múltiplos valores)
    :param situacao: valor opcional, mostra a situação do aluno se True
    :return: dicionário com total, maior, menor, média e situação (se solicitado)
    """


    dados = {}
    dados['total'] = len(n)
    dados['maior'] = max(n)
    dados['menor'] = min(n)
    dados['media'] = sum(n) / len(n)
    
    if situacao:
        if dados['media'] < 6:
            dados['situação'] = 'Ruim'
        elif dados['media'] > 7:
            dados['situação'] = 'Razoável'
        else:
            dados['situação'] = 'Boa'

    
    return dados

resp = notas(5.0, 9,0, 10, 6, 8.5, situacao=True)
print(resp)