import random
numero = random.randint(0, 5)
numero2 = int(input("Digite um número de 0 a 5 para tentar adivinha em qual o computador está pensando: "))

if numero == numero2: 
    print("Você acertou o número que a máquina estava pensando :D")
else:
    print("Você errou :p")