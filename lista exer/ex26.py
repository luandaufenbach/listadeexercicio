"""26) Faça um programa que leia e valide as seguintes informações:
a. Nome: maior que 3 caracteres;
b. Idade: entre 0 e 150;
c. Salário: maior que zero;
d. Sexo: 'f' ou 'm';
e. Estado Civil: 's', 'c', 'v', 'd';
Use a função len(string) para saber o tamanho de um texto (número de caracteres)"""

nome = input("Informe o nome: ")

if len(nome) <= 3:
    print("Nome inválido. O nome deve conter mais de 3 caracteres.")
else:
    idade = int(input("Informe a idade: "))

    if 0 <= idade <= 150:
        salario = float(input("Informe o salário: "))

        if salario > 0:
            sexo = input("Informe o sexo (f para feminino, m para masculino): ")

            if sexo.lower() in ['f', 'm']:
                estado_civil = input("Informe o estado civil (s para solteiro, c para casado, v para viúvo, d para divorciado): ")

                if estado_civil.lower() in ['s', 'c', 'v', 'd']:
                    print("Informações válidas. Cadastro concluído.")
                else:
                    print("Estado civil inválido. Informe 's', 'c', 'v' ou 'd'.")
            else:
                print("Sexo inválido. Informe 'f' para feminino ou 'm' para masculino.")
        else:
            print("Salário inválido. Deve ser maior que zero.")
    else:
        print("Idade inválida. Deve estar entre 0 e 150 anos.")
