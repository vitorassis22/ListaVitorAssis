def bhaskara(a, b, c):
    if a == 0:
        print("a não pode ser igual a zero")
        return 0
    delta = (b ** 2) - (4 * a * c)
    print(f"Delta = {delta}")
    if delta < 0:
        print("A equação não possui raízes reais")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"A equação possui uma raiz real: x = {x:.2f}")
    else:
        raiz_delta = delta ** 0.5
        x1 = (-b + raiz_delta) / (2 * a)
        x2 = (-b - raiz_delta) / (2 * a)
        print(f"As raízes da equação são: \nx1 = {x1:.2f} \nx2 = {x2:.2f}")
print("Duas raízes: ")
bhaskara(1, -5, 6)
print("\nDelta negativo:")
bhaskara(1, 2, 5)
print("\nUma raiz:")
bhaskara(1, -4, 4)