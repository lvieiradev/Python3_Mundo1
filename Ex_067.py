c = soma = 0
while True:
    n = int(input("Digite um número, quando quiser parar digete, 999: "))
    if n == 999:
        break
    c += 1
    soma = soma + n
    
print(f"A soma dos {c} algarismos digitados é de {soma}")    
print("Você desativou o programa")