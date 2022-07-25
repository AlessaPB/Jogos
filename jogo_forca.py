def jogar():

    print("  o__ __o__/_                                          ")
    print(" <|    v                                               ")
    print(" < >                                                   ")
    print("  |         o__ __o    \o__ __o      __o__    o__  __o/ ")
    print("  o__/_    /v     v\    |     |>    />  \    /v      |  ")
    print("  |       />       <\  / \   < >  o/        />      / \ ")
    print(" <o>      \         /  \o/       <|         \       \o/ ")
    print("  |        o       o    |         \\         o       |  ")
    print(" / \       <\__ __/>   / \         _\o__</   <\__   / \ ")
    
    palavra_oculta = "lapis"
    letras_corretas = ["_", "_", "_", "_", "_"]

    perdeu = False
    venceu = False
    
    print(letras_corretas)

    while(not perdeu and not venceu):
        
        tentativa = input("Digite uma letra: ")
        tentativa = tentativa.strip()
        
        index = 0
        for letra in palavra_oculta:
            if (tentativa.upper() == letra.upper()):
                letras_corretas[index] = letra
            index = index + 1
        
        print(letras_corretas)
        
    print("Fim do jogo")
        
if(__name__ == "__main__"):
    jogar()
        
    