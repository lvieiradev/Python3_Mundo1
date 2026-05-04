while True:
    n = int(input("Digite um número para ver sua tabuada: "))
    if n < 0:
        break
    for i in range(0,11):
        print(f"[ {n} X {i} = {n * i} ]")