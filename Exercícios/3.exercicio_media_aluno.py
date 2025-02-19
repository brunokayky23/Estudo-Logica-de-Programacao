import os
os.system("clear")

nota_um = float(input("Digite a nota 1: "))
nota_dois = float(input("Digite a nota 2: "))
nota_tres = float(input("Digite a nota 3: "))

media = (nota_um + nota_dois + nota_tres) // 3 
print(media)

if media > 7:
    print("APROVADO!")
elif media < 7:
    print("REPROVADO!")
else:
    print("APROVADO!")

print('')

print(f"Primeira Nota: ")

print("==== FIM ====")