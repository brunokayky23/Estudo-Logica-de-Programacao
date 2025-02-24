import os
os.system("clear")

num_um = int(input("Digite o primeiro número: "))
num_dois = int(input("Digite o segundo número: "))
maior = max(num_um, num_dois)
menor = min(num_um, num_dois)
print('')

print(f"Número um: {num_um}")
print(f"Número dois:{num_dois}")
if num_um == num_dois:
    print("Os números são iguais")
else:
    print(f"Maior número: {maior}")
    print(f"Menor número: {menor}")
print('')