try:
    num = int(input("Digite o número inteiro que você deseja converter: "))
    escolha = int(input("Digite 1 para binário, 2 para octal ou 3 para hexadecimal: "))

    if escolha == 1:
        print(f"Em binário, {num} = {bin(num)[2:]}")
    elif escolha == 2:
        print(f"Em octal, {num} = {oct(num)[2:]}")
    elif escolha == 3:
        print(f"Em hexadecimal, {num} = {hex(num)[2:].upper()}")
    else:
        print("Opção inválida! Digite 1, 2 ou 3.")

except ValueError:
    print("Erro: digite apenas números inteiros.")