#Importando pacotes úteis
import random as rand # Para trabalhar com números aleatórios
import os # Para trabalhar com funcionalidades do sistema operacional
os.system("cls") #Limpa a tela
#Função para definir uma palavra aleatória dentro da lista
def palavra_secreta():
    palavras = ["Borboleta", "Relâmpago", "Harmonia", "Escada", "Fantasia", "Algoritmo", "Serenidade", "Labirinto", "Equilíbrio", "Fragmento"]
    return rand.choice(palavras)
def game():
    #Definição das variáveis úteis
    palavra = palavra_secreta()
    palavra = palavra.upper()
    #Definindo a palavra oculta como underlines do mesmo tamanho que a palavra selecionada
    palavra_ocultada = ["_" for letra in palavra]
    tentativas_restantes = 6
    letras_erradas = []
    #Loop realizado até o jogo finalizar ou a palavra ser descoberta
    while tentativas_restantes > 0 and "_" in palavra_ocultada:
        print(palavra_ocultada)
        print(f"Tentativas restantes: {tentativas_restantes}")
        if letras_erradas:
            print(f"Letras erradas: {letras_erradas}")
        while (True):
                letra = input("Digite uma letra: ")
                if len(letra) == 1 and letra.isalpha():
                     break
                else:
                     print("Você digitou um caracter inválido")
        letra = letra.upper()
        #Se a letra estiver na palavra, percorre a palavra inteira verificando onde se repete e troca o valor na palavra oculta
        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavra_ocultada[i] = letra
        #Se a letra não estiver ainda nas letras erradas (para evitar repetições), adiciona a letra a lista de letras erradas e diminui uma tentativa
        elif letra not in letras_erradas:
                letras_erradas.append(letra)
                tentativas_restantes -= 1
        #Caso não tenha nenhuma letra ocultada, toda a palavra foi descoberta, quebrando o loop e mostrando a palavra completa
        if "_" not in palavra_ocultada:
            print("Parabéns, você adivinhou a palavra: " + palavra)
            break
        os.system("cls")
    #Se as tentativas acabaram, mostra o game over
    if tentativas_restantes == 0:
        print("Você perdeu! A palavra era: " + palavra)
if __name__ == "__main__":
    game()
