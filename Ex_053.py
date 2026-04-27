numero = int(input("Digite um número para saber se ele é um número primo: "))
primo = True
for i in range(2, numero):
    if numero % i == 0:
        primo = False
if primo:
    print("O número digitado é primo :D")
else:
    print("O número digitado não é primo :P")
    