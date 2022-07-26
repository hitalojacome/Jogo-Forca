from random import randrange

introdução_ao_jogo()
palavra_secreta = carrega_palavra_secreta()

letras_certas = inicializa_letras_acertadas(palavra_secreta)
print(letras_certas)

enforcou = False
acertou  = False
erros    = 0

while(not enforcou and not acertou):

    chute = chutes()

    if (chute in palavra_secreta):
        chute_correto(chute, letras_certas, palavra_secreta)
    else:
        erros += 1
        desenha_forca(erros)

    enforcou = erros == 7
    acertou = '_' not in letras_certas

    print(letras_certas)

if(acertou):
    imprime_vitoria()
else:
    imprime_derrota(palavra_secreta)

print('Fim de jogo.')

# Funções usadas no projeto

def introdução_ao_jogo():
    print('-=-' * 15)
    print('-=-=Bem vindo ao Jogo de Forca em Python!=-=-')
    print('-=-' * 15)

# Função responsável para carregar a palavra secreta dentro do arquivo 'palavras.txt'
def carrega_palavra_secreta():
    arquivo = open('palavras.txt', 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

# Desenho da forca acontecendo conforme os erros, o intuito é somente para deixar o projeto mais apresentável ao usuário
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

# Função básica onde o usuário seleciona a letra para o jogo
def chutes():
    chute = str(input('Qual letra? ')).strip().upper()
    return chute

# Alteração assim que o usuário acerta uma das letras na palavra
def chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra
        index += 1


def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]


def imprime_vitoria():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_derrota(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


if(__name__ == "__main__"):
    jogo()