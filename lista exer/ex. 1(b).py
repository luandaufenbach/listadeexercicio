#2)Faça um script que leia algo
#pelo teclado e mostra na tela o seu tipo de dado.

valor = input("Digite um caractere: ")
tipo = type(valor).__name__
print("o tipo de dado é: ",tipo)