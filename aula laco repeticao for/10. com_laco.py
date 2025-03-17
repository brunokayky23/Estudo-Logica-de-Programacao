import os 
import time
os.system("cls || clear")

pares = 0 
impares = 0
for i in range(5):
  numero = int(input(f"Digite a {i+1}º número: "))
  if numero % 2 == 0:
    pares += 1
  else:
    impares += 1

print()
print(f"Pares: {pares}")
print(f"Ímpares: {impares}")

print("Fim do Programa")