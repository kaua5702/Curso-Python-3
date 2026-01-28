def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: número inteiro para calcular o fatorial
    :param show: (opcional) se True, mostra o processo de multiplicação
    :return: o valor do fatorial de n
    """
    
    resultado = 1
    for i in range(n, 0, -1):
        if show:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')    
        
        resultado *= i
    return resultado


print(fatorial(5, show=True))