

def calcular_medias(notas: dict):
    #Criando lista vazia
    lista_medias = []
    #Percorrer o dicionario
    for chave, valor,in notas.items():
        #Fazendo o calculo da media das notas e utiliza o round para arrendondar o resultado com precisao em duas casas decimais
        media = round( sum(valor) / len(valor),2)
        lista_medias.append((chave, media))
    return lista_medias

notas = {'Samuel': [10,9,10,10], 'Karynne':[10,10,10,10,10], "Carol":[5,4,8], 'Wisney': [9,10,9,10,8.5]}

print(calcular_medias(notas))