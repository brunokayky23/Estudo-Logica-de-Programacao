import os
os.system("cls||clear")

QUANTIDADES_NOTAS = 2
soma = 0

for i in range(QUANTIDADES_NOTAS):
    while True:
        nota = float(input(f"Digite uma nota: "))
        
        if nota > 10 or nota < 0:
            print("DIGITE NOTAS VÁLIDAS.")
        else:
            soma += nota 
            break

media = soma / QUANTIDADES_NOTAS


print(f"Média: {media}")