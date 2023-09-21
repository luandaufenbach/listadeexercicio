"""32) Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram
obtidos os seguintes dados:
a. Código da cidade; (digitado pelo usuário)
b. Número de veículos de passeio (em 1999); (digitado pelo usuário)
c. Número de acidentes de trânsito com vítimas (em 1999). (digitado pelo usuário)
Deseja-se saber:
b. Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
c. Qual a média de veículos nas cinco cidades juntas;
d. Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
"""

# Inicializar variáveis para armazenar informações
maior_indice_acidentes = menor_indice_acidentes = float('inf')
cidade_maior_indice = cidade_menor_indice = ""
soma_veiculos = soma_acidentes = 0
cidades_menos_2000_veiculos = 0

# Loop para coletar dados de cinco cidades
for i in range(1, 6):
    print(f"Digite os dados da cidade {i}:")
    codigo_cidade = input("Código da cidade: ")
    num_veiculos = int(input("Número de veículos de passeio (em 1999): "))
    num_acidentes = int(input("Número de acidentes de trânsito com vítimas (em 1999): "))
    
    # Atualizar soma de veículos
    soma_veiculos += num_veiculos
    
    # Verificar se a cidade tem menos de 2000 veículos
    if num_veiculos < 2000:
        cidades_menos_2000_veiculos += 1
        soma_acidentes += num_acidentes
    
    # Verificar maior e menor índice de acidentes
    if num_acidentes > maior_indice_acidentes:
        maior_indice_acidentes = num_acidentes
        cidade_maior_indice = codigo_cidade
    
    if num_acidentes < menor_indice_acidentes:
        menor_indice_acidentes = num_acidentes
        cidade_menor_indice = codigo_cidade

# Calcular a média de veículos nas cinco cidades
media_veiculos = soma_veiculos / 5

# Calcular a média de acidentes nas cidades com menos de 2000 veículos
if cidades_menos_2000_veiculos > 0:
    media_acidentes_menos_2000 = soma_acidentes / cidades_menos_2000_veiculos
else:
    media_acidentes_menos_2000 = 0

# Exibir os resultados
print(f"Maior índice de acidentes: {maior_indice_acidentes} (Cidade {cidade_maior_indice})")
print(f"Menor índice de acidentes: {menor_indice_acidentes} (Cidade {cidade_menor_indice})")
print(f"Média de veículos nas cinco cidades: {media_veiculos:.2f}")
print(f"Média de acidentes nas cidades com menos de 2000 veículos: {media_acidentes_menos_2000:.2f}")
