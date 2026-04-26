import random

jogador = input("Escolha pedra, papel ou tesoura: ").lower().strip()

numero = random.randint(1, 3)
if numero == 1:
    maquina = "pedra"
elif numero == 2:
    maquina = "papel"
else:
    maquina = "tesoura"

print("Você escolheu:", jogador)
print("Máquina escolheu:", maquina)

if jogador == maquina:
    print("Empate!")
elif (jogador == "pedra"   and maquina == "tesoura") or \
     (jogador == "tesoura" and maquina == "papel")   or \
     (jogador == "papel"   and maquina == "pedra"):
    print("Você venceu!")
else:
    print("A máquina venceu!")