resultado = 0
for i in range(0, 6):
    num = int(input("Digite um numero, mas vou somar apenas os pares: "))
    if num % 2 == 0:
        resultado += num
print(f"A soma dos números pares digitado é de: {resultado}")
        


