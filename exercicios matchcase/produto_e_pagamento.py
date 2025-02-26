import os
os.system("clear")



valor_produto = float(input("Digite o valor do produto: "))
forma_pagamento = int(input("Digite 1 ou 2 para a forma de pagamento: "))

match forma_pagamento:
    case 1:
        desconto = valor_produto * 0.1
        preco_final_desconto = valor_produto - desconto
    case 2: 
        preco_parcelado = valor_produto / 6 


print(f"Valor do Produto: {valor_produto} ")

if forma_pagamento == 1:
    print(f"Forma de Pagamento: {case 1} ")
elif forma_pagamento == 2: 
    print((f"Forma de Pagemnto: {case 2}"))
else: 
    print("Inválido")

print(f"Valor do desconto: {desconto}")

if forma_pagamento == 1:
    print(f"Valor Final: {} ")
elif forma_pagamento == 2: 
    print((f"Forma de Pagemnto: {case 2}"))
else: 

