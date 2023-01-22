n = int(input("Digite o valor de n: "))
t = 1
triangular = False

while t < n:
    p = t * (t+1) * (t+2)

    if p == n:
        print(n, "é um número triangular")
        triangular = True
        break

    t = t+1

if triangular == False:
    print(n, "não é um número triangular")