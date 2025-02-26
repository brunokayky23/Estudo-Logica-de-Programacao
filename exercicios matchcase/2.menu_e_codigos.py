import os
os.system("clear")

opcao = int(input("""
 Código \t Prato \t\t Valor 
1 \t Picanha \t\t  R$ 25,00 
2 \t Lasanha \t\t R$ 20,00 
3 \t Strogonoff \t\t R$ 18,00 
4 \t Bife acebolado \t R$ 15,00
5 \t Pão com ovo \t\t R$ 5,00 

Digite a opção desejada:                 
"""))


match opcao: 
    case 1: 
        print("Você escolheu: Picanha, Valor: R$ 25,00")
    case 2: 
        print("Você escolheu: Lasanha, Valor: R$ 20,00")
    case 3: 
        print("Você escolheu: Strogonoff, Valor: R$ 18,00")
    case 4: 
        print("Você escolheu: Bife acebolado, Valor: R$ 15,00")
    case 5: 
        print("Você escolheu: Pão com ovo, Valor: R$ 5,00")
    case _: 
        print("Opção inválida, escolha um código válido.")


print ("")