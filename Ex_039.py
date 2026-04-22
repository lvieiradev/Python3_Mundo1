num1 = int(input("Digite o primeiro numero para comparação: "))
num2 = int(input("Digite o segundo numero para comparar: "))
if num1 > num2:
    print(f"O primeiro valor: {num1}, é maior que o segundo valor: {num2}")
elif num2 > num1:
    print(f"O segundo valor: {num2}, é maior que o primeiro valor: {num1}")
else:
    print(f"Os valores: {num1} e: {num2} são iguais")