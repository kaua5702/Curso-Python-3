palavras = ('amor', 'perto', 'perdoa', 'saudade')

for i in palavras:
    vogais = ('a', 'e', 'i', 'o', 'u')
    print(f'\nas vogais presentes em {i} são:')
    for l in vogais:
        if l in i:
            print(f'{l} /', end = ' ')

print
