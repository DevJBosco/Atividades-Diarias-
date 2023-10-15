import random


def escolher_palavra():
    palavras = ["cachorro", "dinheiro", "cdd", "estudar", "carro", "civic", "programação", "estudar"]
    return random.choice(palavras)


def jogar_forca():
    palavra = escolher_palavra()
    letras_corretas = set()
    erros = 7

    while True:
        letra = input("Digite uma letra: ").lower()

        if letra in letras_corretas:
            print("Você já tentou esta letra.")
        elif letra in palavra:
            letras_corretas.add(letra)
            print("Letra correta!")
        else:
            erros -= 1
            print("Letra incorreta. Você tem {} tentativas restantes.".format(erros))
        print("  ___     ")
        print(" |/      |    ")

        if (erros == 6):
            print(" |     (̶◉͛‿◉̶)   ")
            print(" |            ")
            print(" |            ")
            print(" |            ")

        if (erros == 5):
            print(" |     (͡• ͜ʖ ͡•)    ")
            print(" |      \     ")
            print(" |            ")
            print(" |            ")

        if (erros == 4):
            print(" |     (─‿‿─)   ")
            print(" |      \|    ")
            print(" |            ")
            print(" |            ")

        if (erros == 3):
            print(" |     (¬‿¬)   ")
            print(" |      \|/   ")
            print(" |            ")
            print(" |            ")

        if (erros == 2):
            print(" |    (ㆆ_ㆆ)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |            ")

        if (erros == 1):
            print(" |     (╥︣﹏᷅╥)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      /     ")

        if (erros == 0):
            print(" |     (-̶●̃益●̶̃)̲")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      / \   ")

        print(" |            ")
        print("|__         ")
        print()

        palavra_escondida = ""
        for letra_palavra in palavra:
            if letra_palavra in letras_corretas:
                palavra_escondida += letra_palavra
            else:
                palavra_escondida += "_"

        print("Palavra: " + palavra_escondida)

        if erros == 0:
            print("Você perdeu! A palavra era: " + palavra)
            break

        if set(palavra_escondida) == set(palavra):
            print("Parabéns! Você venceu!")
            break


jogar_forca()
