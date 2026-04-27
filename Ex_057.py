media1 = float(0)
homem_velho_idade = 0
homem_velho_nome = ""
qmulheres = 0

for i in range(0, 4):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    sexo = input("Digite seu sexo: 'M' = masculino, 'F' = feminino: ")
    
    media1 = media1 + idade
    
    if sexo == "M" and idade > homem_velho_idade:
        homem_velho_idade = idade
        homem_velho_nome = nome
    
    if sexo == "F" and idade < 20:
        qmulheres = qmulheres + 1

media_idade = media1 / 4
print(f"A média de idade do grupo é de: {media_idade}")
print(f"O nome do homem mais velho é: {homem_velho_nome}")
print(f"{qmulheres} mulher(es) tem menos de 20 anos")