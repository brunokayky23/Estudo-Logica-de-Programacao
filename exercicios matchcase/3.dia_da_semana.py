import os
os.system("clear")


dia_da_semana = int(input("""
Número \t Dia \t\t Útil ou Fim de Semana  
1 \t Domingo \t\t Fim de semana                      
2 \t Segunda \t\t Dia útil                      
3 \t Terça \t\t\t Dia útil
4 \t Quarta \t\t Dia útil
5 \t Quinta \t\t Dia útil
6 \t Sexta \t\t\t Dia útil
7 \t Sábado \t\t Fim de semana

                                                 
Digite um número: """))

match dia_da_semana:
    case 1:
        print("Domingo, fim de semana")
    case 2:
        print("Segunda-feira, dia útil")
    case 3:
        print("Terça-feira, dia útil")
    case 4:
        print("Quarta-feira, dia útil")
    case 5:
        print("Quinta-feira, dia útil")
    case 6:
        print("Sexta-feira, dia útil")
    case 7:
        print("Sábado, fim de semana")
    case _: 
        print("Número inválido")

print ("")