
def somar_pares(lista_de_numeros):
    resultado=0
    for numero in lista_de_numeros:
        if numero % 2 ==0:
            resultado+= numero
    return resultado

lista = [1,4,10,6,3,7,9]

print(f' A soma dos pares na lista é: {somar_pares(lista)}')