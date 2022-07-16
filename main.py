print("SEU BANCO")
numero1 = 0
cadastro = ''

while numero1 != 5:
    print("Numero (1) CADASTRO")
    print("Numero (2) DEPOSITAR")
    print("Numero (3) SAQUE")
    print("Numero (4) IMPRIMIR")
    print("Numero (5) SAIR")

    numero1 = int(input("Digite sua opção: "))

    if numero1 == 1:
        cadastro = str(input("Digite aqui o seu nome de usuario: "))
        print('Seja bem-vindo a sua conta {} <3'.format(cadastro))
    elif numero1 == 2:
        senha = int(input("Digite o valor do deposito: "))
    elif numero1 == 3:
        saque = int(input("Digite o valor de saque: "))
    elif numero1 == 4:
        Resultado = senha - saque
        print(f"{Resultado}" + " <<< Saldo atual em conta")    
    else:
        print("OBRIGADO POR USAR O NOSSO BANCO <3")

# salario_do_usuario = int(input("Digite o seu salario: "))
# saque_do_usuario = int(input("Digite o valor que você deseja sacar: "))
# total_atual_da_conta = salario_do_usuario - saque_do_usuario
# print(total_atual_da_conta)

