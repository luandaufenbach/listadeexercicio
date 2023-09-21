#17)Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal,
#utilizando as seguintes formulas (onde h corresponde à altura):
#• Homens: (72.7 ∗ h) − 58
#• Mulheres: (62, 1 ∗ h) − 44, 7


a = float(input("Altura: "))
b = input("Digite o seu gênero M - Masculino\n"
          "F - Feminino : ")

if b == "M":
    print(f"Peso ideal: {(72.7*a)-58}")
elif b == "F":
    print(f"Peso ideal: {(62.1*a)-44.7}")
else:
    print("nenhum genero")