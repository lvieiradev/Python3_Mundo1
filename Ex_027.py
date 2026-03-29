frase = input("Digite uma frase qualquer:")
print(f"A letra 'A' aparece {frase.lower().count('a')} vezes na frase.")
print(f"A primeira vez que a letra 'A' aparece é na posição {frase.lower().find('a')}.")
print(f"A última vez que a letra 'A' aparece é na posição {frase.lower().rfind('a')}.")

