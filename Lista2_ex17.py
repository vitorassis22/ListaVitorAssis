a = int(input("Digite um numero: "))
b = int(input("Digite um numero: "))
c = int(input("Digite um numero: "))

if (a < b + c) and (b < c + a) and (c < a + b):
    if (a == b == c):
        print("O triangulo existe e é equilátero")
    elif (a == b) or (a == c) or (b == c):
        print("O triangulo existe e é isósceles")
    else: print("O triangulo existe e é escaleno")
else: print("O triangulo não existe")