import os 
import time
os.system("cls || clear")

numero = int(input("Digite um número para contagem regressiva: "))
print("Contagem Regressiva")
for i in range(numero,0,-1):
    print(f"Contagem Regressiva: {i}")
    time.sleep(1)

print("Fim do Programa")