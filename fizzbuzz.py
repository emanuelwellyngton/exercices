n = int(input("Digite um número inteiro: "))

d3 = n % 3
d5 = n % 5

if d3 == 0 and d5 ==0:
    print("FizzBuzz")
else:
    print(n)