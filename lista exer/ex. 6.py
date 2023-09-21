#Faça um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
#Considere: US$ 1.00 = R$ 5.41

real = float(input("Qual sua quantia de dinheiro em reais? : "))
conv = real/4.88
print(f"Com {real} você consegue {conv} dolares")