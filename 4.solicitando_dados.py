import os
os.system("clear")

# Solicitando dados.
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))      #Para ler um número inteiro ou real, coloca a variável na frente e as aspas antes da aplicação)
altura = float(input("Digite sua altura: "))
# Input = pede dados ao usuário
# Output = mostra dados ao usuário


print(f"Nome: {nome}") #  <---- Equivalente no Visual G 3 ----> escreval("Nome: ", nome)
print(f"Idade: {idade}")
print(f"Altura: {altura}")