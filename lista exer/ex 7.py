#7) Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto e com 15% de aumento.
merc = float(input("valor da sua mercadoria: "))
novopreco = merc - (merc*0.05)
novoprecoaumento = merc * 0.15

print(f"Sua mercadoria teve um novo preço de : {novopreco}, novo preço com aumento : {novoprecoaumento}")
