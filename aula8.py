

nome=input("Digite o seu nome: ")
rg=input("Digite seu RG: ")
ano_nasc=input("Digite o ano em que nasceu: ")
telefones=list()
tel1=input("Digite seu primeiro telefone")
tel2=input("Digite seu segundo telefone")
telefones.append(tel1)
telefones.append(tel2)
dicionario={"nome":nome,"rg":rg,"ano_nasc":ano_nasc,"telefones":["1199014245"]}
print("nome",nome,"rg",rg,"ano_nasc",ano_nasc,"telefones", dicionario["telefones"][0])