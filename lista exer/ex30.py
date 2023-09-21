"""30) O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de
conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá
receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser
informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e
perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta
operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser
conforme o exemplo abaixo:
a. Lojas Tabajara
b. Produto 1: R$ 2.20
c. Produto 2: R$ 5.80
d. Produto 3: R$ 0
e. Total: R$ 9.00
f. Dinheiro: R$ 20.00
g. Troco: R$ 11.00
h. ...
"""

while True:
    print("Lojas Tabajara")

    total_compra = 0.0
    numero_produto = 1

    # Receber os preços dos produtos até que o usuário digite 0
    while True:
        preco_produto = float(input(f"Produto {numero_produto}: R$ "))
        if preco_produto == 0:
            break
        total_compra += preco_produto
        numero_produto += 1

    # Exibir o total da compra
    print(f"Total: R$ {total_compra:.2f}")

    # Solicitar o valor em dinheiro fornecido pelo cliente
    dinheiro_cliente = float(input("Dinheiro: R$ "))

    # Calcular e exibir o troco
    troco = dinheiro_cliente - total_compra
    print(f"Troco: R$ {troco:.2f}")

    # Perguntar se deseja registrar outra compra
    continuar = input("Deseja registrar outra compra? (S/N): ").strip().upper()
    if continuar != "S":
        break
