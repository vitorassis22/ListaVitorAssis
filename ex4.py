def verificar(valor):
    
    if valor % 2 == 0:
        return 1
    else:
        return 0

par = print(f"A funcao recebe 10 e retorna {verificar(10)} para par")
impar = print(f"A funcao recebe 5 e retorna {verificar(5)} para ímpar")