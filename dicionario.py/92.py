import datetime
ano_atual = datetime.datetime.now().year

dados = {}

nome = input('Nome: ')
dados['Nome'] = nome

nascimento = int(input('Ano de nascimento: '))
idade = ano_atual - nascimento
dados['Idade'] = idade

ctps = int(input('Carteira de trabalho: (0 não tem) '))
dados['Ctps'] = ctps
if ctps != 0:
    ano_c = int(input('Ano de contratação: '))
    dados['Ano de contratação'] = ano_c
    salario = float(input('Salário: '))
    dados['Salário'] = salario
    aposentadoria = (ano_c + 30) - ano_atual
    dados['Aposentadoria'] = aposentadoria

print(f'Nome tem valor {nome}')
print(f'Idade tem o valor {idade}')
print(f'CTPS tem o valor {ctps}')
print(f'Contratação tem valor {ano_c}')
print(f'Salário tem valor {salario}')
print(f'Aposentadoria tem valor {aposentadoria}')
