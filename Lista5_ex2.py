def depositar(saldoAtual, valor):
    if valor <= 0:
        print("Erro: O valor do depósito deve ser maior que zero.")
        return saldoAtual
    saldo_atual += valor
    print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    return saldoAtual
def sacar(saldoAtual, valor):
    if valor <= 0:
        print("Erro: O valor do saque deve ser maior que zero.")
        return saldoAtual
    if valor > saldoAtual:
        print("Erro: Saldo insuficiente para realizar a operação.")
        return saldoAtual
    saldoAtual -= valor
    print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    return saldoAtual
def caixa():
    saldo = 0.0
    while True:
        print("MENU")
        print("1. Ver Saldo")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            print(f"Seu saldo atual é: R$ {saldo:.2f}")
        elif opcao == "2":
            v_deposito = float(input("Digite o valor para depósito: R$ "))
            saldo = depositar(saldo, v_deposito)
        elif opcao == "3":
            v_saque = float(input("Digite o valor para saque: R$ "))
            saldo = sacar(saldo, v_saque)
        elif opcao == "4":
            print("Encerrando sessão. Obrigado por usar nosso banco!")
            break
        else:
            print("Opção inválida! Tente novamente.")

caixa()