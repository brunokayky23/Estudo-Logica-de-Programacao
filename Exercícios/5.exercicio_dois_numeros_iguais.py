import os
os.system("clear")

numero_um = int(input("Digite o primeiro número: "))
numero_dois = int(input("Digite o segundo número: "))


media = (numero_um + numero_dois) / 2
soma = numero_um + numero_dois
produto = numero_um * numero_dois

print(f"Média: {media}")
print(f"Soma: {soma}")
print(f"Produto: {produto}")

if numero_um > numero_dois:
    print("O primeiro número é maior!")
elif numero_um < numero_dois: 
    print("O segundo número é maior!")
else: 
    print("Os números são iguais!")
print("==== FIM ====")
