#12) Escreve um Programa que leia uma lista com no minino 5 itens, contendo itens repetidos e mostre
#os itens repetidos.

lista = [1,2,3,4,4]

repetido = set(item for item in lista if lista.count (item) > 1 and item not in repetido)

print("o numero de itens repetidos sao: ", repetido)
