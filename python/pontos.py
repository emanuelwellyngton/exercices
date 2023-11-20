import math

x1 = float(input("Digite a cordenada x do primeiro plano: "))
y1 = float(input("Digite a cordenada y do primeiro plano: "))
x2 = float(input("Digite a cordenada x do segundo plano: "))
y2 = float(input("Digite a cordenada y do primeiro plano: "))

subX = (x1 - x2) ** 2
subY = (y1 -y2) ** 2

distancia = math.sqrt(subX + subY)

if distancia >= 10:
    print("longe")
else:
    print("perto")