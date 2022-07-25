def jogar():
    
    import random

    print("              _ _       _       _                           ")     
    print("     /\      | (_)     (_)     | |                          ")
    print("    /  \   __| |___   ___ _ __ | |__   __ _  ___ __ _  ___  ")  
    print("   / /\ \ / _` | \ \ / / | '_ \| '_ \ / _` |/ __/ _` |/ _ \ ") 
    print("  / ____ \ (_| | |\ V /| | | | | | | | (_| | (_| (_| | (_) |")
    print(" /_/    \_\__,_|_| \_/ |_|_| |_|_| |_|\__,_|\___\__,_|\___/ ")


    numero_oculto = round(random.randrange(1,51))
    numero_de_tentativas = 0
    pontuacao = 100

    print("Escolha um nível de dificuldade:")
    print(" [1] Fácil [2] Médio [3] Difícil ")

    nivel_dificuldade = int(input("Defina o nível:"))

    if(nivel_dificuldade == 1):
        numero_de_tentativas = 12
    elif(nivel_dificuldade == 2):
        numero_de_tentativas = 6
    else:
        numero_de_tentativas = 3


    for posicao in range(1, numero_de_tentativas + 1):
        print("Tentativa {} de {}".format(posicao, numero_de_tentativas))
        
        adivinhacao = int(input("Digite o número de 1 a 50:"))
        print("Sua escolha foi:", adivinhacao)
        
        if (adivinhacao < 1 or adivinhacao > 50):
            print("Você deve digitar um número entre 1 e 50!")
            continue

        acertou = adivinhacao == numero_oculto 
        maior = adivinhacao > numero_oculto
        menor = adivinhacao < numero_oculto

        if (acertou):
            print("Parabéns! Você acertou e ganhou {} pontos!".format(pontuacao))
            break
        else:
            if (maior):
                print("Você errou! O seu número foi maior do que o número oculto.")
            elif (menor):
                print("Você errou! O seu número foi menor do que o número oculto.")
                pontuacao_perdida = abs(numero_oculto - adivinhacao)
                pontuacao = pontuacao - pontuacao_perdida
                
    print("Fim de jogo! O número oculto era", numero_oculto)

if(__name__ == "__main__"):
    jogar()
