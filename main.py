# dicionario
conta = {
    'usuario': '',
    'senha': '',
    'saldo': 100
}
#exibe saldo atualizado
def exibe_saldo():
    print(f"\n\nUsuário: {conta['usuario']}")
    print(f"Saldo atual: R$ {conta['saldo']}\n")
# função para depositar na conta 
def depositar(valor_deposito):
    if valor_deposito > 0:
        conta['saldo'] = conta['saldo'] + valor_deposito
    else:
        print("\n\nERRO! Saldo digitado invalido!\n\n")
#função para sacar
def saque(valor_saque):
    if valor_saque > conta['saldo']:
        print("\n\nERRO! você não possui saldo suficiente!\n\n")
    else:
        conta['saldo'] = conta['saldo'] - valor_saque
        #exibe o valor que foi sacado
        print(f"\n\nValor sacado: R${valor_saque}")
#sistema de cadastro
print(" - - - Pagina de cadastro - - - -")
conta['usuario'] = input("crie um usuario: ")
conta['senha'] = input("crie uma senha: ")
#sistema de login
print("--- PAGINA DE LOGIN ----")
user = input("Usuario: ")
senha = input("Senha: ")
if user == conta['usuario'] and senha == conta['senha']:
    opcao = ''
    while opcao != '0':
        print("---- MENU -----\n")
        print("1 - depositar\n2 - Sacar\n0 - Sair\n")
        opcao = input("\nDigite a opção desejada: \n")
        if opcao == '1':
            deposito = float(input("\nDigite o valor a ser depositado: R$"))
            depositar(deposito)
            exibe_saldo()
        elif opcao == '2':
            valor = float(input("\nDigite o valor de saque: \n"))
            saque(valor)
            exibe_saldo()
        elif opcao == '0':
            print("\n\n\nFechando programa...\n\n\n ")
else:
    print("erro de login") 