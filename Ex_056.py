maior = 0
menor = 9999
for i in range(0,5):
    peso = float(input("Digite  seu peso em (KG): "))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso 
print(f"O maior peso foi: {maior}")    
print(f"O menor peso foi: {menor}")

     
