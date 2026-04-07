velocidade = float(input("Insira o valor em KM/H do carro: "))

multa = int(7)
multa_t = (velocidade - 80) * multa
if velocidade > 80:
    print("Você passouacima do limite de velocidade da via")
    print(f"Você será multado em R$ {multa_t} ")
else:
    print("Você passou dentro do limite de velocidade e não  será multado :D")
