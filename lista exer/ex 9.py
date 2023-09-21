#9) Construir um programa que leia nome e valor em dinheiro (reais) de uma pessoa. Calcule e retorne uma
#mensagem com o valor convertido para Dólar e calcule e retorne uma mensagem com o valor convertido para Euros.

valor = float(input("Digite o valor : "))
dolar = valor/4.88
euro = valor/5.27

print("Os valores convertidos são :\n"
      f"Dolar(es) : {dolar}\n"
      f"Euro(s) {euro}")