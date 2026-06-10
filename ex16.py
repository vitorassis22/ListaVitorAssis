b = int(input("Insira o tipo de bilhete: \nSimples(1)\nDuplo(2)\n10Bilhetes(3)\n: "))
c = int(input("Insira a quantidade a ser comprada: "))
v = float(input("Insira o valor pago: "))
match b:
    case b if b == 1:
        b = 1.30 * c
        q = v // b
        if q < 1:
            print("Não é possível comprar")
        else:print(f"Troco: {v % b:.2}")
    case b if b == 2:
        b = 2.6
        q = v // b
        if q < 1:
            print("Não é possível comprar")
        else:print(f"Troco: {v % b:.2}")
    case b if b == 3:
        b = 12
        q = v // b
        if q < 1:
            print("Não é possível comprar")
        else:print(f"Troco: {v % b:.2}")