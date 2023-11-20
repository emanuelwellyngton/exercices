a = float(input("Digite o primeiro número"))
b = float(input("Digite o segundo número"))
c = float(input("Digite o terceiro número"))

hipotenuza = 0
cateto1 = 0
cateto2 = 0

if a > b and a > c:
    hipotenuza = a
    cateto1 = b
    cateto2 = c
elif b > a and b > c:
    hipotenuza = b
    cateto1 = a
    cateto2 = c
else:
    hipotenuza = c
    cateto1 = a
    cateto2 = b

if cateto1**2 + cateto2**2 == hipotenuza ** 2:
    print("Os números", a, b, c,"são os lados de um triangulo retangulo")
else:
    print("Os números", a, b, c, "não são os lados de um triangulo")