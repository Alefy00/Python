menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>  """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor para deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R${valor:.2f}\n"

        else:
            print("Operação falhou valor invalido.")
    
    
    elif opcao == "s":
       valor = float(input("Informe o valor para sacar: "))

       excedeu_saldo = valor > saldo

       excedeu_limite = valor > limite

       excedeu_saques = numero_saques >= LIMITE_SAQUES

       if excedeu_saldo:
           print(" vc não tem saldo suficiente.")
        
       elif excedeu_limite:
           print("vc não tem limite suficiente.")
        
       elif excedeu_saques:
           print("vc atingiu o limite de saques")

       elif valor > 0:
           saldo -= valor
           extrato += f"Saque: R$ {valor:.2f}\n"
           numero_saques += 1

       else:
           print("Operação falhou informe um valor valido")

    elif opcao == "e":
        print("\n===========================Extrato=========================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("==============================================================")
    
    elif opcao == "q":
        break

    else:
        print("Operação invalida, por favor selecione novamente a operação desejada")
    