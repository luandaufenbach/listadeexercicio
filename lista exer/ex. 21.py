#Crie um programa que leia dois valores e mostre na tela um menu :
#a. Somar
#b. Multiplicar
#c. Maior
#d. Menor
#e. Sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso
a = float(input("Digite um 1° numero: "))
b = float(input("digite um 2° numero: "))
c = input("Digite qual equação ira querer: \n a. Somar \n b. Multiplicar \n c. Maior \n  d. Menor \n e. Sair do programa ")
if (c == "a"):
    ra = a + b
    print("calculo final deu",ra)
elif (c == "b"):
    rb = a * b
    print("calculo final deu",rb)
elif (c == "c"):
    if (a>b):
        print(a,"é o maior numero")
    else:
        print(b,"é o maior numero")
elif (c == "d"):
    if (a<b):
        print(a,"é o menor numero")
    else:
        print(b,"é o menor numero")
else:
    print("você saiu do programa")