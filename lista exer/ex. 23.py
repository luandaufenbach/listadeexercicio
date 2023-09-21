#Crie um programa que leia vários números inteiros pelo teclado. No final, mostre a média entre todos os
#valores lidos e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou
#não continuar a escrever valores.
l = []
num = 0
while True:
    val = float(input("valor: "))
    l.append(val)
    num+=1
    z = input("Você quer continuar adicionando valores? (N=Não)")
    if z == "N":
        break
print(f"Média: {sum(l)/num}")
print(f"Maior: {max(l)}")
print(f"Menor: {min(l)}")