print("------Bem Vindo ao Jogo----")


print("-" * 36)
print("Options modo Treinamento ")
print("-" * 36)

print(" Para Pular clique na (barra)")
print(" Para anda para frente clique no (d)")
print(" Para voltar para trás clique na (a)")
print("Para se agachar clique na (z)")
print("Para sair digite sim")


print("-" * 36)
print("Options modo Mata-Mata")
print("-" * 36)

print(" Para Equipar arma Aperte (p)")
print(" Para Mira no Oponente Aperte (v)")
print(" Para atirar no Oponente Aperte (c)")
print("Para recarregar sua Arma Aperte (r)")
print("Para equipar colete Aperte (h)")
print("Para sair digite sim")


print("-" * 36)
while True:
    # ----> Configuraçoes Modo Treinamento

    btn = input("Digite o Comando que Deseja: ")

    if btn == "d":
        print("Voce Acabou de andar para Frente")

    elif btn == "a":
        print("Voce Acabou de Volta para Trás ")

    elif btn == "barra":
        print("Voce Acabou de Pular ")

    elif btn == "z":
        print("Voce Acabou de Agachar ")

    elif btn=="p":
        print("Voce Acabou de equipar Desert Eagle")

    elif btn=="v":
        print("Voce esta Mirando no Oponente")

    elif btn=="c":
        print("Voce Acabou de Atirar no Oponente")

    elif btn=="r":
        print("Voce esta recarregando sua Arma")

    elif btn=="h":
        print("Voce Acabou de equipar o Colete")


    elif btn=="sim":


     break


