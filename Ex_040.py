from datetime import date
idade = int(input("Informe seu ano de nascimento: "))
ano_atual = date.today().year
idade_atual = ano_atual - idade
if idade_atual == 18:
    print("Você deve se apresentar ao serviço militar")
elif idade_atual > 18:
    anosp = idade_atual - 18
    print(f"Já se passou {anosp} anos desde que você devia se apresentar")
else:
    anosf = 18 - idade_atual
    print(f"Ainda faltam {anosf} anos para você se apresentar no serviço militar")



