def celsius_f(c):
    return (c * 9/5) + 32
def metros_cm(m):
    return m * 100
def menu():
    while True:
        print("\nMENU DE CONVERSÕES")
        print("1. Converter Celsius para Fahrenheit")
        print("2. Converter Metros para Centímetros")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            c = float(input("Digite a temperatura em °C: "))
            f = celsius_f(c)
            print(f" Conversão feita -> {f:.2f}°F")
        elif opcao == "2":
            m = float(input("Digite a medida em metros: "))
            cm = metros_cm(m)
            print(f"Conversão feita -> {cm:.2f} centímetros")
        elif opcao == "3":
            print("Programa encerrado")
            break
        else:
            print("Opção inválida, tente novamente.")
menu()