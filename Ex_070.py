maiores = 0
homens = 0
mulheres_jovens = 0

while True:
    idade = int(input("Digite a idade: "))
    while idade < 0 or idade > 120:
        print("Idade inválida!")
        idade = int(input("Digite a idade: "))

    sexo = str(input("Digite o sexo [M/F]: ")).upper()
    while sexo != "M" and sexo != "F":
        print("Valor inválido!")
        sexo = str(input("Digite o sexo [M/F]: ")).upper()

    if idade > 18:
        maiores += 1
    if sexo == "M":
        homens += 1
    if sexo == "F" and idade < 20:
        mulheres_jovens += 1

    continua = str(input("Deseja continuar? [S/N]: ")).upper()
    while continua != "S" and continua != "N":
        print("Valor inválido!")
        continua = str(input("Deseja continuar? [S/N]: ")).upper()

    if continua == "N":
        break

print(f"Pessoas com mais de 18 anos: {maiores}")
print(f"Homens cadastrados: {homens}")
print(f"Mulheres com menos de 20 anos: {mulheres_jovens}")