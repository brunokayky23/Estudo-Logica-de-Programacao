import os
os.system("clear")

idade = int(input("Digite sua idade: "))


if idade > 17 and idade < 65:
    print("Voto Obrigatório")
elif idade < 16:
    print("Não Vota")
elif idade >= 65:
    print("Voto opicional.")
else:
    print("Voto opicional")
print('')