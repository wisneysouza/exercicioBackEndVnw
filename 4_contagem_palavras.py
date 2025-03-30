def contar_frequencia(palavras):
    lista = palavras.split(' ')

    dicionario = {}

    for palavra in lista:
        if not palavra in dicionario.keys():
            dicionario[palavra] = lista.count(palavra)
    return dicionario

palavras = 'Banana Banana Maça Morango Morango Uva Uva Abacaxi Laranja Laranja'


print (contar_frequencia(palavras))