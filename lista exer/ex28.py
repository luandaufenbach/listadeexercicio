"""28) Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para
cada eleitor votar e ao final mostrar o número de votos de cada candidato"""

num_eleitores = int(input("Informe o número total de eleitores: "))

votos_candidato1 = 0
votos_candidato2 = 0
votos_candidato3 = 0

for eleitor in range(1, num_eleitores + 1):
    print(f"Eleitor {eleitor}:")
    voto = int(input("Informe o número do candidato (1, 2 ou 3): "))

    if voto == 1:
        votos_candidato1 += 1
    elif voto == 2:
        votos_candidato2 += 1
    elif voto == 3:
        votos_candidato3 += 1
    else:
        print("Voto inválido. Este voto não será contado.")
        
print("\nResultado da eleição:")
print(f"Candidato 1: {votos_candidato1} votos")
print(f"Candidato 2: {votos_candidato2} votos")
print(f"Candidato 3: {votos_candidato3} votos")
