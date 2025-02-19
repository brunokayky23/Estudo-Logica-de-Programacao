import os
os.system("clear")

num_um = int(input("Digite o primeiro número: "))
num_dois = int(input("Digite o segundo número: "))
num_tres = int(input("Digite o terceiro número: "))
maior = max(num_um, num_dois, num_tres)
menor = min(num_um, num_dois, num_tres)
print('')

print(f"Número um: {num_um}")
print(f"Número dois:{num_dois}")
print(f"Número três: {num_tres}")
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")