ano = int(input("Digite um ano para descobrir se ele é bissexto: "))

resto = ano % 4

if resto == 0:
    print(ano, "é um ano bissexto")
else:
    print(ano, "não é um ano bissexto")