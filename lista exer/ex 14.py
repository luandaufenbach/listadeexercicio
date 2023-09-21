#14) Escreva um Programa que verifique se um elemento está na lista e verifique a posição exata dele da lista.
lista = [10, 20, 30, 40, 50]

procura = int(input("digite o numero que voce procura: "))

if procura in lista:
    posicao = lista.index(procura)
    print(f"o numero {procura} esta na posicao {posicao} da lista")
else:
    print("o numero nao foi encontrado na lista")