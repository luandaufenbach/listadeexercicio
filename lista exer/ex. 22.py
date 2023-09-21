#Crie um programa que leia vários números inteiros pelo teclado. O programa só pode para quando for
#digitado o numero 1000. No final, mostre quantos números foram digitados e qual foi a soma deles.
#Desconsiderando o valor 1000 da parada.
x = num = soma = 0
while x != 1000:
    x = int(input("Digite um número: "))
    if x != 1000:
        num+=1
        soma+=x
print(f"Quantidade de números inseridos: {num}")
print(f"Soma de todos os números inseridos: {soma}")