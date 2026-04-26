valor = float(input("Digite o calor da sua compra em (R$): "))
pagamento = float(input(" \nInforme a forma de pagamento, \n digite 1 : para pagamento à vista dinheiro/pix \n digite 2 : para pagamento á vista no cartão \n digite 3 : para pagamento no cartão em 2x \n digite 4 : para pagamento no cartão em 3x ou mais \n"))
if pagamento == 1:
    valor = valor * 0.9
    print(f"Você recebeu 10% de desonto, o valor final que você vai pagar vai ser de: {valor}")
elif pagamento == 2:
    valor = valor * 0.95
    print(f"Você recebeu 5% de desconto o valor total que você vai pagar é de: {valor}")
elif pagamento == 3:
    print(f"Por esse método de pagamento é impossível aplicar desconto, o valor de: {valor} será cobrado por completo")
elif pagamento == 4:
    valor = valor * 1.20
    print(f"Por esse metódo o valor tem um acrécimo de 20% o valor final que você vai paga é de: {valor}")
