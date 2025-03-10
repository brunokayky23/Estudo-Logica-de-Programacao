import os
os.system("clear")

valor_produto = float(input("Digite o Valor do Produto: "))
forma_de_pagamento = int(input(""" 
1 - A Vista
2 - A Prazo
Digite a forma de pagamento: """))

match forma_de_pagamento:
    case 1: 
        desconto = valor_produto * 0.10
        valor_pagar = valor_produto - desconto

        print(f"\n Valor do Produto: R$ {valor_produto}")
        print(f" Forma de Pagamento: à vista")
        print(f" Valor do Desconto: R$ {desconto}")
        print(f" Total a Pagar: R$ {valor_pagar}")
    case 2: 
        quantidade_parcelas = int(input("Digite a quantidade de parcelas: "))
        if quantidade_parcelas >= 1 and quantidade_parcelas <= 6:
            valor_parcela = valor_produto / quantidade_parcelas

            print(f"\nValor do produto: R$ {valor_produto}")
            print(f"Forma de pagamento: à prazo")
            print(f"Quantidade de parcelas: {quantidade_parcelas}")
            print(f"Valor por parcela: R$ {valor_parcela:.2f}")
            print(f"Total à prazo: R$ {valor_produto}")
        else: 
            print("O parcelamento deve ser feito em até 6 parcelas.")
    case _: 
        print ("Opção Inválida")