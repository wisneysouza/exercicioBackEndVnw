

def contar_tpo3_mais_frequentes(numeros: list):
    frequencia = {}
    for numero in numeros:
        if numero in frequencia.keys():
            frequencia[numero] += 1
        else:
                frequencia[numero] = 1

        numeros_ordenados = sorted(frequencia.keys(), key=lambda chave: (frequencia[chave], chave), reverse=True)

    return numeros_ordenados[:3]


lista_numeros = [1,1,1,1,2,4,5,5,2,2,2,2,2,7,7,7,7,7,7,7,7,7]

print(contar_tpo3_mais_frequentes(lista_numeros))