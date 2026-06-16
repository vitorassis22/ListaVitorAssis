def ordenar(a, b, c):
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b
    print(f"Valores em ordem crescente: {a}, {b}, {c}")
teste = ordenar(10,5,7)