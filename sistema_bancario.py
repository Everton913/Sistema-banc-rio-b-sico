menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> '''
saldo = 0
limite = 500
extrato = ""
numero_saques = 0 
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
      valor = float(input("informe o valor do depósito:"))

      if valor > 0: 
         saldo+= valor 
         extrato += f"Depósito: R$ {valor: .2f}\n"
         print(f"Depósito no valor de R${valor} realizado com sucesso. ")
         
      else:
          print("Valor inválido, por favor digite um valor possitivo.")
          


    elif opcao == "s":
        valor = float(input("Informe o valor do saque:"))

        verificando_saldo = valor > saldo 

        limite_diario = valor > limite

        excedeu_limite = numero_saques >= LIMITE_SAQUES

        if verificando_saldo:
            print("Operação falhou, Saldo insuficiênte ")
        
        elif limite_diario:
            print(" Operação falhou, O valor do saque excede o limite, entre em contato com seu gerente!")

        elif excedeu_limite :
            print("Número máximo de saques atingido")

        elif valor > 0: 
            saldo -= valor 
            extrato += f"Saque : R$ {valor: .3f}\n"
            numero_saques += 1
            print(" Saque no valor de R${valor}, Realizado com sucesso.")
        
        else:
            print("Operação falhou, Por favor insira um valor válido")

    elif opcao == "e":
        print("\n#####Extrato#####")
        print("Nenhuma movimentação encontrada." if not extrato else extrato)
        print(f"\n Saldo:{saldo:.3f}")
    
    elif opcao == "q":
        print("Obrigado por utilizar nosso banco ")
        break
        
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
