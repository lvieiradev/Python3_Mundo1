from datetime import date
idade = int(input("Digite seu ano de nascimento: "))
data = date.today().year
ano_nascimento = data - idade
if ano_nascimento <= 9:
    print(f"Você tem {ano_nascimento}, você pertence a categoria mirim")
elif ano_nascimento <= 14:
    print(f"Você tem {ano_nascimento}, você pertence a categoria Infantil")
elif ano_nascimento <= 19:
    print(f"Você tem {ano_nascimento}, você pertence a categoria juvenil")
elif ano_nascimento <= 20:
    print(f"Você tem {ano_nascimento}, você pertence a categoria sênior")
else: 
    print("Você pertence a categoria Master")