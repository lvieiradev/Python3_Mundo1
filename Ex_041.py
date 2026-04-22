nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
media = (nota1 + nota2) / 2

if media >= 7:
    print(f"Sua média foi de: {media}. Parabéns você foi aprovado")
elif media >= 5:
    print(f"Sua média foi de: {media}. Você ficou de recuperação. Mas se esforce você ainda vai conseguir")
elif media < 5:
    print(f"Sua média foi de: {media}. Infelizmente você foi reprovado :(")
