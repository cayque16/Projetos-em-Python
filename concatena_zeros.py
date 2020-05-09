def conacatena_zeros(texto: str,tam_final: int,esquerda=True) -> str: 
    # Concatena zeros a uma determinada string
    #   texto -> texto que se deseja concatenar os 0s
    #   tam_final -> tamanho final que o texto deve ter
    #   esquerda -> onde se deve concatenar os 0s esquerda(True) ou direita(False)
    tam_final -= len(texto)
    if tam_final > 0:
        while tam_final > 0:
            if esquerda:
                texto = '0' + texto
            else:
                texto += '0'
            tam_final -= 1
    return texto

print(conacatena_zeros('1212',4))