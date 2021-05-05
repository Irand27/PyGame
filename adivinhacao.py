import random
def jogar():
    pontos = 1000
    numero_secreto = random.randrange(1, 100)
    total_de_tentativas = 0

    print("Qual o nível de dificuldade?")
    print("(1) Fácil \n(2) Médio \n(3) Díficil")

    nível = int(input("Defina o nível: "))

    if nível == 1:
        total_de_tentativas = 20
    elif nível == 2:
        total_de_tentativas = 10
    elif nível == 3:
        total_de_tentativas = 5
    else:
        print("Não é um nível válido")

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite o seu número: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {}!".format(pontos))
            break
        else:
            if (maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif (menor):
                print("Você errou! O seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
    print("O número secreto era {}".format(numero_secreto))
    print("Fim do jogo")
if(__name__ == "__main__"):
    jogar()