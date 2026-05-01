import random
numero = random.randint(0, 10)
numero2 = int(input("Digite um número de 0 a 10 para tentar adivinha em qual o computador está pensando: "))
c = 0

while numero2 != numero:
    numero2 = int(input("Tente novamente: "))
    c += 1
print(f"Você precisou de: {c} tentativas para acertar o número.")
