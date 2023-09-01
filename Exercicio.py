
print("Seja Bem vindo")
print("-" *30, "Menu", "-"*30 )
print("Para Visualizar Cadastro do usuario Digite.1")

usuarios=list()
while True:
    btn = input("Digite qual Opção : ")
    if btn =="1":
        nome1= input("Digite seu nome: ")
        while nome1.isdigit():
            nome1 = input("Digite seu nome: ")

        rg1 = input("Digite o seu RG: ")
        while not rg1.isdigit():
            rg1 = input("Digite o seu RG: ")

        cpf1 = input("Digite seu CPF: ")
        while not cpf1.isdigit():
            cpf1 = input("Digite seu CPF: ")

        dat1 = input("digite sua Data de Nascimento :")
        while not dat1.isdigit():
            dat1 = input("digite sua data de nascimento")

        tel1 = input("Digite seu Telefone:  ")
        while not tel1.isdigit():
            tel1 = input("digite o seu telefone")

        email1 = input("Digite seu E-mail:  ")

        cep1 = input("digite seu CEP: ")
        while not cep1.isdigit():
            cep1 = input("digite o seu cep")

        usuario ={"nome":nome1,"RG":rg1,"CPF":cpf1,"Data de Nascimento":dat1,"TELEFONE":tel1,"EMAIL":email1,"CEP":cep1}
        print(usuario)

print("-" * 36)
























