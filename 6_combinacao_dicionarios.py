
dicionario_1 = {'A':2, 'B':1, 'C':4, 'D':3}
dicionario_2 = {'A':1, 'B':1, 'C':3, 'D':3, 'E':1}

def combinar_dicts(dicionario_1: dict, dicionario_2: dict):
    novo_dicionario ={}

    for chave, valor in dicionario_1.items():
            if chave in dicionario_2:
                novo_dicionario[chave] = valor + dicionario_2[chave]
            else: 
                novo_dicionario[chave] = valor

    for chave, valor in dicionario_2.items():
            if chave not in novo_dicionario:
                novo_dicionario[chave]= valor

    return novo_dicionario

print(combinar_dicts(dicionario_1, dicionario_2))

#tarefa consertar a logica