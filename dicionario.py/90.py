arq = {}


nome = input('Nome: ')

media = float(input('Média: '))

if media >= 7.0:
    situacao = 'Aprovado'
else:
    situacao = 'Reprovado'


arq['nome'] = nome
arq['media'] = media
arq['situacao'] = situacao 

print(arq)