print("*********************************")
print("***Bem vindo ao jogo da Forca!***")
print("*********************************")

palavra_secreta = 'banana'

acertou = False
enforcou = False

while not acertou and not enforcou:
    chute = input("Qual letra? ")

    posicao = 0
    for letra in palavra_secreta:
        if(chute.upper() == letra.upper()):
            print('Encontrei a letra {} na posição {}'.format(letra, index))
        posicao += 1
        print("Jogando")

print("Fim do jogo")