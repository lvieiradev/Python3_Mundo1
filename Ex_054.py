frase = str(input("Digite uma frase para saber se ela é palíndromo: ").lower().replace( " ",""))
if frase == frase[::-1]:
    print("É palíndromo")
else:
    print("Não é palíndormo")
