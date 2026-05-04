import random 

print("=-"*30)
print("Vamos jogar par ou ímpar")
print("=-"*30)

while True:
    pc = random.randint(0,10)
    n = int(input("Digite um número: "))
    e = str(input("Par ou Ímpar?  [P/I]: ")).upper()
    if (n + pc) % 2 == 0 and e == "P":
        print(f"Você digitou {n} e o pc escolheu {pc}, sua escolha foi par, PARABÉNS VOCÊ GANHOUU")
    elif (n + pc) % 2 != 0 and e == "I":
        print(f"Você digitou {n} e o pc escolheu {pc}, sua escolha foi ímpar, PARABÉNS VOCÊ GANHOUU")

    else:
        print(f"Você escolheu {n} e o pc escolheu {pc}, você perdeu :c ")
        break
    

