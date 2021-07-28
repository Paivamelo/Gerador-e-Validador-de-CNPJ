
import cnpj
while True:
    print("Escolha uma das opções abaixo:")
    print("1 - Validar CNPJ")
    print("2 - Gerar CNPJ")
    print("3 - Sair")
    escolha = input("")

    if escolha == "1":
        cnpj1 = input("Digite seu cnpj: ")

        if cnpj.valida_cnpj(cnpj1):
            print("CNPJ válido")
            print(" ")
        else:
            print("CNPJ inválido")
            print(" ")

    elif escolha == "2":
        novo_cnpj = cnpj.gera()
        formatado = cnpj.formata(novo_cnpj)
        print(formatado)
        print(" ")
    
    elif escolha == "3":
        break
