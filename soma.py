q = int(input("Quantos número você quer somar?"))

i = 1

somaPar = 0
somaImpar = 0
numeroPares = 0
numerosImpares = 0

while i <= q:
    n = int(input("Degite o número: "))

    if n % 2 == 0:
        somaPar = somaPar + n
        numeroPares = numeroPares + 1
    else:
        somaImpar = somaImpar + n
        numerosImpares = numerosImpares + 1

    i = i + 1

print("A soma dos números pares é:", somaPar)
print("A soma dos números ímpares é:", somaImpar)
print("Entre os número digitados,", numeroPares, "são pares e", numerosImpares, "são ímpares")