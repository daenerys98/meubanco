print ("Meu banquinho")
input("Digite aqui o seu nome de usuario:")
salario_do_usuario = int(input("Digite o seu salario"))
saque_do_usuario = int(input("Digite o valor que deseja sacar"))
total_atual_da_conta = salario_do_usuario - saque_do_usuario
if (salario_do_usuario > total_atual_da_conta):
    print ("economiza mais amigo")
else:
    print ("parabens você é pão duro")