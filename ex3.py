def verificar(valor):
    if valor > 0:
        return 1
    elif valor < 0:
        return -1
    else:
        return 0

positivo10 = print(f" O valor {10} é positivo e a função retornou {verificar(10)}")
negativo10 = print(f" O valor {-10} é negativo e a função retornou {verificar(-10)}")