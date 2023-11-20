total_investido = int(input("Qual valor incial do investimento? (Apenas números)"))
n = 12
r = 0.08
anos = int(input("Por quantos anos você vai deixar o investimento ativo?"))

juros_compostos = total_investido*(1+r/n)**(n*anos)

print("Ao final de", anos, "anos, o valor total do investimento será de R$", int(juros_compostos))