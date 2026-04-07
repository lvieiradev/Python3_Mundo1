numero = float(input("Insira um número para saber se ele é par ou ímpar: "))
resultado = numero %2 
if resultado == 0:
    print(f"O número {numero} é par :D")
else:
    print(f"O número {numero} é ímpar :P")   
