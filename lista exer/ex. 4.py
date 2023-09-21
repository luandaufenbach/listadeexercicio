#4) Faça um programa que leia algo pelo teclado e mostre na tela seu tipo de dado e todas as informações sobre ele.

valor = input("Digite um caractere: ")
tipo = type(valor).__name__
print("o tipo de dado é: ",tipo)