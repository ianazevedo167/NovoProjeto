import  datetime as dt
usuarios = list()

while True:
    print("Seja Bem - Vindo! ")
    print("#"*30,"menu","#"*20)
    print(""" 
          "Para Cadastrar Digite--.1
           "para sair digite -.2  
    """)
    btn=input("Deseja Sair do Sistema Aperta-->2")

    #Cadastra Usuarios
    if btn=="1":
        nome:str=input("Nome")
        rg: str = input("RG")
        ano_nasc: str = input("Ano Nascimento")
        #Vamos Tratar Ano de Nascimento

        tel1:str=input("Digite o seu Telefone 1:")
        tel2: str = input("Digite o seu Telefone 2:")
        telefones=[tel1,tel2]#Adicionando Telefones

    print("#"*20, "Cadastro de Despesas", "#"*20)
        #Despesas
    descricao:str=input("Descrição de Despesas:")
    valor=input("Digite o seu Valor R$: ")

    #Tratar o valor da entrada
    data_despesa=dt.date.today()

    if btn=="2":
        break