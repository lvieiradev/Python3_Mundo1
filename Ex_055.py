from datetime import date
atual = date.today().year
menor = 0
maior = 0
for i in range(0,7):
    data = int(input("Qual seu ano de nascimento, responda apenas com números: "))
    if atual - data < 21:
        menor = menor + 1 
    elif atual - data >= 21:
        maior = maior + 1
print(menor)
print(maior)



