n = []
for i in range(0, 5):
    i = int(input('Digite um número: '))
    n.append(i)

print(n)


menor = min(n)
maior = max(n)
p_mn = n.index(menor)
p_m = n.index(maior)

print(f'O menor número da lista é {menor} e está na posição {p_mn + 1}')
print(f'O maior número da lista é {maior} e está na posição {p_m + 1}')