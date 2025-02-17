import os
os.system("clear")


idade = int(input("Digite sua idade: "))  

if idade < 12:
    print("Acesso Negado.")
elif idade < 18: 
    print("Somente com permissão do responsável")
else: 
    print("Acesso Permitido.")


print("== FIM ==")