km_p = float(input("Insira o valor percorrido em quilometros: "))
km_v =  km_p * 0.50
km_v2 = km_p * 0.45 
if km_p < 200:
    print(f"O valor da sua viagem foi de: {km_v}")
else:
    print(f"Sua viagem ficou no valor de: {km_v2}")