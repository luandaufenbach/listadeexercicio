"""33) Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os
códigos utilizados são:
 1 , 2, 3, 4 - Votos para os respectivos candidatos
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
a. O total de votos para cada candidato;
b. O total de votos nulos;
c. O total de votos em branco;
d. A percentagem de votos nulos sobre o total de votos;
e. A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o
valor zero."""

# Inicializar contadores para cada candidato e votos nulos e em branco
votos_candidato1 = votos_candidato2 = votos_candidato3 = votos_candidato4 = 0
votos_nulos = votos_em_branco = total_votos = 0

while True:
    voto = int(input("Digite o código do candidato (1 a 4), 5 para voto nulo, 6 para voto em branco ou 0 para encerrar: "))

    if voto == 0:
        break
    elif voto == 1:
        votos_candidato1 += 1
    elif voto == 2:
        votos_candidato2 += 1
    elif voto == 3:
        votos_candidato3 += 1
    elif voto == 4:
        votos_candidato4 += 1
    elif voto == 5:
        votos_nulos += 1
    elif voto == 6:
        votos_em_branco += 1
    else:
        print("Voto inválido. Por favor, digite um código válido.")

    total_votos += 1

# Calcular as percentagens
percentagem_votos_nulos = (votos_nulos / total_votos) * 100
percentagem_votos_em_branco = (votos_em_branco / total_votos) * 100

# Exibir os resultados
print(f"Total de votos para o Candidato 1: {votos_candidato1}")
print(f"Total de votos para o Candidato 2: {votos_candidato2}")
print(f"Total de votos para o Candidato 3: {votos_candidato3}")
print(f"Total de votos para o Candidato 4: {votos_candidato4}")
print(f"Total de votos nulos: {votos_nulos}")
print(f"Total de votos em branco: {votos_em_branco}")
print(f"Percentagem de votos nulos sobre o total de votos: {percentagem_votos_nulos:.2f}%")
print(f"Percentagem de votos em branco sobre o total de votos: {percentagem_votos_em_branco:.2f}%")
