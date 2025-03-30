

def ordenar_tuplas(lista_tuplas):
    lista_ordenada = sorted(lista_tuplas, key= lambda tupla: tupla[1])
    return lista_ordenada

lista = ('Samuel', 23), ('Karynne', 20), ('Caril', 22),('Suelen',21), ('Romulo',15)
print(f'As tuplas ordenadas por idade: {ordenar_tuplas(lista)}')
