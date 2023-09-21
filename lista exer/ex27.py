"""27) Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120"""

numero = int(input("Informe um número inteiro positivo: "))

fatorial = 1

if numero < 0:
    print("O fatorial não está definido para números negativos.")
elif numero == 0:
    print("O fatorial de 0 é 1.")
else:
    for i in range(1, numero + 1):
        fatorial *= i

    print(f"{numero}! = {fatorial}")
