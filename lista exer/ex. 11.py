#11) Faça um programa que receba como entrada os dados de um funcionário: nome, numero de horas
#trabalhadas, valor da hora trabalhada. Após calcule seu salário bruto. Calcule um desconto de 2% de INSS. E
#ao final mostrar seu nome e salário final calculado

nome = input("nome: ")
horas = float(input("horas trabalhadas: "))
valor = float(input("valor por hora: "))
bruto = horas*valor
desc = bruto - (bruto*0.02)

print(f"funcionário : {nome}\n"
      f"salário bruto : {bruto}\n"
      f"sal. com desconto: {desc}")
      







#novopreco = merc - (merc*0.05)




