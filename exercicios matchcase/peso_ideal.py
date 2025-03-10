import os
os.system("clear")


altura = float(input("Digite sua altura: "))

qual_sexo = input("""
M - Masculino 
F - Feminino 
Digite o seu sexo: """)

match qual_sexo:
    case "M"|"m":
        peso_ideal = (72.7 * altura) - 58   
        print(f"Seu peso ideal é: {peso_ideal:.2f}")

    case "F"|"f": 
        peso_ideal = (62.1 * altura) - 44.7
        print(f"Seu peso ideal é: {peso_ideal:.2f}")

    case _: 
        print("Opção inexistente.")