#Funçoes


#Eu Preciso calcular a Média
#Metodo 1
valor1=4.5
valor2=7
valor3=8.5

media=(valor1+valor2+valor3)/3
print(media)
# 2 maneira de calcular a media
#Metodo 2
valores=[4.5,7,8.5]
media=sum(valores)/len(valores)
print(media)

# Imagina que fazer meida na inha empresa e uma rotima diaria
# vou fazer essa acção de modo pratico
# se eu for cirar uma função para o (metodo 1) posso fazer assim

#para cria uma função preciso usar uma palavra reservada "def"
#O que vai entre os parenteses e chamado de parametros
def media(n1 , n2 , n3):
   if n1.isdigit() and n2.isdigit() and n3.isdigit().isdigit():
    print((int(n1)+int(n2)+int(n3)/3))
   else:
       print("Voce Precisa digitar um numero inteiro")


def soma(n1,n2,n3):
    print(n1+n2+n3)




n1 = input("Digite Valor 1: ")
n2 = input("Digite Valor 2: ")
n3 = input("Digite Valor 3: ")

soma(int(23),int(55),int(10))




media=(2,4,7.8)


def contarTamanho(lista):
    cont=0
    for valor in lista:
        cont=cont+1
        
        
    return cont


