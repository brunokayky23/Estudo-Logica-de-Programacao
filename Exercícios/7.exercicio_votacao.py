import os
os.system("clear")

idade = int(input("Digite sua idade: "))


if idade >= 18 and idade <= 65:
    print("Voto Obrigatório")
elif idade < 16:
    print("Não Vota")
else:
    print("Voto opicional")
print('')