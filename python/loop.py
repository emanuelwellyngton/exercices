i = 0
soma = 0
quantidade = int(input("Quantos números você quer somar?"))

while i < quantidade:
    n = int(input("Digite um número: "))

    soma = soma + n
    i = i + 1

print("O resultado da soma é", soma)