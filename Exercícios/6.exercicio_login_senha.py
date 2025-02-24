import os
os.system("clear")

login_cadastrado = "julindamoca"
senha_cadastrada = "123456"

login = input("Digite seu Login: ")
senha = input("Digite sua senha: ")

if login == login_cadastrado and senha == senha_cadastrada:
    print("Bem Vindo!")
else:
    print("Login ou senha inválidos")
print('')
