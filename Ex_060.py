def ler_numeros():
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    return a, b

a, b = ler_numeros()

while True:
    print("\n===== MENU =====")
    print("[1] Somar")
    print("[2] Multiplicar")
    print("[3] Maior")
    print("[4] Novos números")
    print("[5] Sair do programa")

    opcao = int(input("\nEscolha uma opção: "))

    if opcao == 1:
        print(f"Resultado: {a + b}")
    elif opcao == 2:
        print(f"Resultado: {a * b}")
    elif opcao == 3:
        if a > b:
            print(f"O maior número é: {a}")
        elif b > a:
            print(f"O maior número é: {b}")
        else:
            print("Os números são iguais")
    elif opcao == 4:
        a, b = ler_numeros()
        print("Números atualizados!")
    elif opcao == 5:
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida! Escolha entre 1 e 5.")