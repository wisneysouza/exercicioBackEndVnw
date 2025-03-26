

def contar_frequencia(palavras):
    lista = palavras.split(', ')

    dicionario = {}

    for palavra in lista:
        if not palavra in dicionario.keys():
            dicionario[palavra] = lista.count(palavra)
    return dicionario        

linguagens = 'Java, Java, Java, Java, Python, Ruby, Ruby, Cobol, Java, Java, Java, Python'

print ('Quantidade de frequencia')
print ('-'*100)
print ( contar_frequencia(linguagens))