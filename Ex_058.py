sexo = str(input("Digite se sexo; 'M', para masculino e 'F', Para feminino: ")).upper()
while sexo != "M" and sexo != "F":
    print("Digite uma opção válida")
    sexo = str(input("Digite se sexo; 'M', para masculino e 'F', Para feminino: ")).upper()
print(f"O sexo selecionado foi {sexo}")
