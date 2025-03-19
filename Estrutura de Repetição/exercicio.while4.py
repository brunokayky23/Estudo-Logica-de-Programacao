import os
os.system("cls || clear")


login_cadastrado = "marta"
senha_cadastrada = "123"
contador = 0


while True:
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")

    if login_cadastrado == login and senha_cadastrada == senha:        
        print("Acesso permitido")
        break  
    else: 
        print("Acesso negado")
        contador += 1

    if contador == 3:
        print("Número de tentativas excedido.")
        break