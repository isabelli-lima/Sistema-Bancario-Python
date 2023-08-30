menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
"""
saldo = 0
limite_por_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opção = input(menu)

    if opção == "1":
       valor = float(input("Informe o valor do depósito:"))

       if valor > 0:
          saldo += valor
          extrato  += f"Depósito: R$ {valor:.2f}\n"

       else:
           print("Operação falhou o valor informado é inválido.")

    elif opção == "2":
       valor = float(input("Informe o valor do saque: "))
       excedeu_saldo = valor > saldo
       excedeu_limite = valor > limite_por_saque
       excedeu_saques = numero_saques >= LIMITE_SAQUES

       if excedeu_saldo:
           print("Operação falhou!Você não tem saldo suficiente.")

       elif excedeu_limite:
           print("Operação falhou!O valor do saque execede o limite.")

       elif excedeu_saques:
           print("Operação falhou!Número máximo de saques excedido.")

       elif valor > 0:
            saldo -= valor
            extrato += f"saque: R$ {valor:.2f}\n"
            numero_saques += 1

       else:
          print("Operação falhou!O valor informado é inválido.")


    elif opção == "3":
        print("\n=====Extrato=====")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==================")
        

    elif opção == "4":
        break

    else:
     print("Operação inválida, por favor selecione novamente a opção desejada.")