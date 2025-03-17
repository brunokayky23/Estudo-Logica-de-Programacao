import os 
import time
os.system("cls || clear")

nota = 0 
media = 0
soma = 0

for i in range(3):
  nota = float(input(f"Digite a {i+1}ª nota: "))
  soma += nota 
  media = soma / 3 


print(f"Média: {media:.2f}")

if media >= 7:
  print("ALUNO APROVADO")
elif media <= 4:
  print("ALUNO REPROVADO")
else:
  print("RECUPERAÇÃO")




print("Fim do Programa")