while True:
    valor = int(input("Digite o valor a ser sacado: "))

    cedulas_50 = valor // 50
    resto = valor % 50

    cedulas_20 = resto // 20
    resto = resto % 20

    cedulas_10 = resto // 10
    resto = resto % 10

    cedulas_1 = resto // 1

    print(f"\nCédulas de R$50: {cedulas_50}")
    print(f"Cédulas de R$20: {cedulas_20}")
    print(f"Cédulas de R$10: {cedulas_10}")
    print(f"Cédulas de R$1:  {cedulas_1}")

    continua = str(input("\nDeseja fazer outro saque? [S/N]: ")).upper()
    while continua != "S" and continua != "N":
        print("Valor inválido!")
        continua = str(input("Deseja fazer outro saque? [S/N]: ")).upper()

    if continua == "N":
        print("Obrigado por usar nosso caixa!")
        break