import os
os.system("clear")

idade = int(input("Digite sua idade: "))


if idade > 64:
    print("Sem obrigatoriedade de voto!!!")
elif idade < 18:
    print("Não precisa votar!!!")
else: 
    print("Voto Obrigatório!!!")