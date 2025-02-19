import os
os.system("clear")


login = "julindamoca@gmail.com"
senha = 123456

login = (input("Digite seu email: "))
senha = (input("Digite sua senha: "))


if login != "julindamoca@gmail.com":
    print("Login ou Senha inválidos")
elif senha != 123456:
    print("Login ou Senha inválidos")
else:("Bem vindo!")