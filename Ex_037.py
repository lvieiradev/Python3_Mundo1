valor_casa = float(input("Digite o valor da casa que deseja comprar em R$: "))
salario = float(input("Digite o valor do seu salário mensal em R$: "))
anos = int(input("Digite em quantos anos você pretende pagar a casa: "))
pretencao = valor_casa / (anos * 12)
if pretencao > salario * 0.3:
    print("Infelizmente o você não consegue apenas com esse numero de parcelas, tente parcelar em mais vezes :C ")
else:
    print(f"Parabéns você conseguiu sua casa , você vai pagar por mês R$: {pretencao}, durante {anos} anos")