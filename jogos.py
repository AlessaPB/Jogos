import jogo_forca
import jogo_adivinhacao

def escolher_jogo():
    print("   (        (  (           ")
    print("   )\   (   )\))(  (   (   ")
    print("  ((_)  )\ ((_))\  )\  )\  ")
    print(" _ | | ((_) (()(_)((_)((_) ")
    print("| || |/ _ \/ _` |/ _ \(_-< ")
    print(" \__/ \___/\__, |\___//__/ ")
    print("           |___/           ")
    
    print("[1] Adivinhação [2] Forca ")

    jogo = int(input("Escolha um dos jogos: "))

    if (jogo == 1):
        print("Jogando forca")
        jogo_adivinhacao.jogar()
    elif (jogo == 2):
        print("Jogando adivinhação")
        jogo_forca.jogar()
    
if(__name__ == "__main__"):
    escolher_jogo()