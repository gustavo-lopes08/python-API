'''
# Laço While com tentativas ilimitadas
numero_secreto = 10
acertou = False
while acertou == False:
    chute = int(input("Adivinhe o numero secreto: "))
    if chute == numero_secreto:
        acertou = True
        print("Acertou! O numero secreto é ", numero_secreto)
    else:
        print("Errou! Tente novamente")
        desistir = input("Para sair digite 'desistir', para continuar tecle enter ")
        if desistir == 'desistir' or desistir == 'Desistir':
            print("Você desistiu! O número secreto é ", numero_secreto)
            acertou = True
print("Fim do programa")
'''


'''
# Laço while com tentativas limitadas
numero_secreto = 10
tentativas = 3
while tentativas != 0:
    if tentativas != 1:
        print ("Você tem ", tentativas, " tentativas")
    else:
        print ("Você tem 1 tentativa")
    chute = int(input("Adivinhe o numero secreto: "))
    if (chute == numero_secreto ):
        print("Acertou! O numero secreto é: ", numero_secreto)
        tentativas = 0
    else:
        tentativas -= 1
        if tentativas != 0:
            print("Errou! Tente novamente")
        else:
            print("Errou! Fim das tentativas")
            print("O número secreto é: ", numero_secreto)
print("Fim do programa")
'''

'''
# Laço for com niveis de dificuldade
numero_secreto = 10
print("\n*****Guess the number game******\n")
print("Níveis de dificuldade\n")
print("Nível 1: 10 tentativas")
print("Nível 2: 5 tentativas")
print("Nível 3: 3 tentativas")
nivel = int(input("\nEscolha o nível: "))
if nivel == 1:
    tentativas = 10
    print ("Nível 1 selecionado")
elif nivel == 2:
    tentativas = 5
    print ("Nível 2 selecionado")
elif nivel == 3:
    tentativas = 3
    print ("Nível 3 selecionado")
else:
    print("Nível inválido!")
    exit()
for t in range(tentativas,0,-1):
    print ("Voce tem ",t, "tentativas")
    chute = int(input("Adivinhe o numero secreto: "))
    if chute == numero_secreto:
        print ("Acertou! O numero secreto é ",numero_secreto)
        break
    else:
        if t > 1:
            print("Errou! Tente novamente")
        else:
            print("Errou! Fim das tentativas. O numero secreto é: ", numero_secreto)
'''