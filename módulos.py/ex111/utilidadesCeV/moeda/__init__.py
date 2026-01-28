def metade(n=0, formato=False):
    res = n / 2
    return moeda(res) if formato else res


def dobro(n=0, formato=False):
    res = n * 2
    return moeda(res) if formato else res


def aumentar(n=0, quant=0, formato=False):
    res =  n + (n * quant / 100)
    return moeda(res) if formato else res


def diminuir(n=0, quant=0, formato=False):
    res = n - (n * quant / 100)
    return moeda(res) if formato else res 

def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')


def resumo(p=0, aumenta=0, diminui=0):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)

    print(f"{'Preço analisado:':<20} {moeda(p)}")
    print(f"{'Dobro do preço:':<20} {moeda(dobro(p))}")
    print(f"{'Metade do preço:':20} {moeda(metade(p))}")
    print(f"{f'{aumenta} % de aumento:':<20} {moeda(aumentar(p, aumenta))}")
    print(f"{f'{diminui} % de redução:':<20} {moeda(diminuir(p, diminui))}")
    print('-' * 30)
