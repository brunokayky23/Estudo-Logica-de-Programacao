import os
os.system("clear")

primeiro_numero = int(input("Digite um número: "))
operador = (input("Digite um operador (+ - * /): "))
segundo_numero = int(input("Digite o segundo número: "))

match operador:
    case "+":
        resultado = primeiro_numero + segundo_numero
    case "-": 
        resultado = primeiro_numero - segundo_numero
    case "*": 
        resultado = primeiro_numero * segundo_numero
    case "/": 
        resultado = primeiro_numero / segundo_numero
    case _: 
        resultado = "Opção inválida"


print(f"Primeiro número: {primeiro_numero}")
print(f"Segundo número: {segundo_numero}")
print(f"Resultado: {resultado}")