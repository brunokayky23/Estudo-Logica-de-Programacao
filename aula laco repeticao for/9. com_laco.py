import os 
import time
os.system("cls || clear")

soma = 0
for i in range(5):
  numero = int(input(f"Digite a {i+1}º número: "))
  soma = soma + numero 

  print()
  print(f"Soma: {soma}")

print("Fim do Programa")