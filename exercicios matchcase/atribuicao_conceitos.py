import os
os.system("clear")

nome = input("Digite seu nome: ")
nota_um = float(input("Digite sua primeira nota: "))
nota_dois = float(input("Digite sua segunda nota: "))


media = (nota_um + nota_dois) / 2


if media >= 9:
    conceito = "A"
elif media >= 7.5:
    conceito = "B"
elif media >= 6:
    conceito = "C"
elif media >= 4:
    conceito = "D"
elif media < 4:
    conceito = "E"
print("")

match conceito:
    case "A" | "B" | "C":
        print(f"Conceito: {conceito}")
        print("APROVADO")
    case "D" | "E":
        print(f"Conceito: {conceito}")
        print("REPROVADO")
    case _: 
        print("Opção Inválida")


print(f"Nome: {nome}")
print(f"Primeira Nota: {nota_um}")
print(f"Segunda Nota: {nota_dois}")
print(f"Média: {media}")