#25) Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do
#usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
    n=input("Diga seu usuario")
    s=input("Diga sua senha")
    if (n!=s):
        break