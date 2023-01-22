import math

def calcula_delta (a, b, c):
    delta = (b ** 2) - 4 * a * c

    if delta < 0:
        print("esta equação não possui raízes reais")
    else:
        delta_sqrt = math.sqrt(delta)
        calcula_raizes(a, b, delta_sqrt, delta)

def calcula_raizes (a, b, delta_sqrt, delta):
    x = (-b + delta_sqrt) / (2 * a)
    y = (-b - delta_sqrt) / (2 * a)
    
    if delta == 0:
        print("a raiz desta equação é", x)
    elif y < x:
        print("as raízes da equação são", y, "e", x)
    else:
        print("as raízes da equação são", x, "e", y)

a = float(input("Digite um número inteiro: "))
b = float(input("Digite outro número inteiro: "))
c = float(input("Digite mais um número inteiro: "))

calcula_delta(a, b, c)