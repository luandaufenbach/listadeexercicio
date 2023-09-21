#8) Faça um programa que leia a largura e a altura de uma parede em metros, e calcule a sua área e a
#quantidade da tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m².

larg = float(input("largura parede: "))
alt = float(input("Altura da parede: "))

area = larg * alt
litros = area / 2

print(f"a área da parede é {area}")
print(f"Serão necessários {litros} de tinta para pintar parede")