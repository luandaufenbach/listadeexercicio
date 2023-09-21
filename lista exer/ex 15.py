#15) Faça um programa que pergunte a temperatura atual para o usuário e mostre uma mensagem na
#tela dizendo se está “quente”, “frio” ou “agradável”.

temp = float(input("Digite a temperatura de hoje : "))
if temp > 30:
    print("hoje esta calor!")
elif temp < 15:
    print("hoje esta frio!")
else:
    print("hoje esta agradável!")

