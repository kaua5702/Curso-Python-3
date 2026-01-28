def terreno(larg, compr):
    area = compr * larg
    print(f'A área do terreno é de {area:.2f} m²')


print('\nControle de terrenos')
print('-' * 30)

larg = float(input('LARGURA (m): '))
compr = float(input('COMPRIMENTO (m): '))

terreno(larg, compr)