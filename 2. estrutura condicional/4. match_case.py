import os
os.system("clear")

dia = input("Digite um dia da semana: ")

print('')
match dia:
    case "segunda" | "Segunda" | "SEGUNDA":
        print("Hoje é segunda-feira.")
    case "terça" | "Terça" | "TERÇA":
        print("Hoje é terça-feira.")
    case "quarta" | "Quarta" | "QUARTA":
        print("Hoje é quarta-feira.")
    case "quinta" | "Quinta"| "QUINTA":
        print("Hoje é quinta-feira.")
    case "sexta" | "Sexta" | "SEXTA":
        print("Hoje é sexta-feira.")
    case "sábado" | "domingo" | "Sábado" | "Domingo" |"SÁBADO"| "DOMINGO":
        print("Hoje é fim de semana.")
    case _: 
        print("Dia inválido.")
print('')

print(dia)

print("")

print("=== FIM ===")
