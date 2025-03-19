import os
os.system("cls||clear")



nota = int(input("Digite sua nota: "))

while nota < 0 or nota > 10: 
    print("Digite uma nota correta")
    nota = int(input("Digite sua nota: "))


print(f"Nota: {nota}")
print("FIM")
    