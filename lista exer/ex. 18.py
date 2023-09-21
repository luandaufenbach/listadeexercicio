#18) Faca um algoritmo que calcule a media das notas de 3 provas. A primeira e a segunda prova tem
#peso 5 e a terceira tem peso 10. Ao final, mostrar a média do aluno e indicar se o aluno foi
#aprovado ou reprovado. A nota para aprovação deve ser igual ou superior a 6.0 pontos.


p1 = float(input("Digite a n1 (peso 5): "))
if p1 > 5:
    p1 = 5
p2 = float(input("Digite a n2 (peso 5): "))
if p2 > 5:
    p2 = 5
p3 = float(input("Digite a n3 (peso 10): "))
if p3 > 10:
    p3 = 10

media = ((p1+p2+p3)/2)
print(f"A média total do aluno é de {media}")

if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")