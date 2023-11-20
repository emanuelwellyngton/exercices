n = int(input("Digite um número grande: "))
d = int(input("Qual dígito você quer procurar? : "))

numero = n
ocorrencia = 0

if 0 <= d <= 9:
    while n > 0:
        dig = n % 10
        n = n // 10
        if dig == d:
            ocorrencia = ocorrencia + 1
    print("O dígito", d, "ocorre", ocorrencia, "vezes no número", numero)