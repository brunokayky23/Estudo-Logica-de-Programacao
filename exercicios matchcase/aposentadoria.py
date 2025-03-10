import os
os.system("clear")

matricula = input("Digite sua matrícula: ")
ano_nascimento = int(input("Digite o ano de seu nascimento: "))
tempo_de_trabalho = int(input("Digite seu tempo de trabalho em anos: "))


idade = 2025 - ano_nascimento

if idade >= 65 or tempo_de_trabalho >= 30:
    resultado = "Requerer aposentadoria."
else:
    resultado = "Não requerer aposentadoria."


print(f"\nMatrícula: {matricula}")
print(f"Idade: {idade}")
print(f"Tempo de Trabalho: {tempo_de_trabalho}")
print(f"Resultado: {resultado}")

