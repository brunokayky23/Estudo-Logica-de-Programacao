import os 
import time
os.system("cls || clear")

nota = 0 
media = 0
soma = 0
for i in range(4):
  nota = float(input(f"Digite a {i+1}ª nota: "))
  soma += nota
  
  media = soma /4 

print(f"Média: {media}")

print("Fim do Programa")