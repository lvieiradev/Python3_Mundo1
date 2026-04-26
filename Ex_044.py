peso = float(input("Digite seu peso (KG): "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura ** 2)

if imc < 18.5:
    print(f"Seu IMC é de: {imc:.2f} você está abaixo da média do peso ideal")
elif imc < 25:
    print(f"Seu IMC é de: {imc:.2f} você está no peso ideal")
elif imc < 30:
    print(f"Seu IMC é de: {imc:.2f} você está com sobrepeso")
elif imc < 40:
    print(f"Seu IMC é de: {imc:.2f} você está com obesidade morbida")
else:
    print(f"Seu IMC é de: {imc:.2f} você está com obesidade mórbida")
