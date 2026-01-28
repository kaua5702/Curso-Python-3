produtos = ('Monitor', 350, 'Pc', 4000, 'Notebook', 3200, 'Videogame', 2500 )

print('=-=' * 20)
frase = 'Listagem de preços'
print(frase.center(50))
print('=-=' * 20)
for i in range(0, len(produtos), 2):
    preco = produtos[i + 1]
    nome = produtos[i]
    print(f'{nome:<15} R$ {preco:>7.2f}')
