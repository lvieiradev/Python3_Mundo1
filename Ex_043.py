a = float(input("Digite o lado A: "))
b = float(input("Digite o lado B: "))
c = float(input("Digite o lado C: "))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Triângulo Equilátero: todos os lados iguais")
    elif a == b or a == c or b == c:
        print("Triângulo Isósceles: dois lados iguais")
    else:
        print("Triângulo Escaleno: todos os lados diferentes")
else:
    print("Esses valores não formam um triângulo válido!")