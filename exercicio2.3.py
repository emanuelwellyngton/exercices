n = int(input("Digite um número"))
exp = int(input("Digite outro número"))

if exp >= 0:
    calc = n ** exp
else:
    n = int(input("Digite um número inteiro"))
    calc = n ** exp

print("O resultado é", calc)