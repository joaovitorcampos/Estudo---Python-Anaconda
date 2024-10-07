import random as rand
from os import system, name
import unicodedata
def limpa_tela():#Função para limpar a tela
    #Windows
    if name == "nt":
        _ = system("cls")
    #Mac ou Linux
    else:
        _ = system("clear")
def normalize(letra):#Função para retornar a letra sem acentos
        return unicodedata.normalize('NFKD', letra).encode('ASCII', 'ignore').decode('ASCII')
class Forca:
    #Método construtor para definir parâmetros iniciais da classe
    def __init__(self):
        self.chances = 6
        with open("wl.txt", "r", encoding="utf-8") as wl:#Carrega as palavras da lista de palavras guardadas no arquivo e separa em uma lista
            self.wl = wl.read().replace(" ", "").split(",")
        self.palavra = rand.choice(self.wl).lower()#Escolhe uma palavra aleatória
        self.ocultada = ["_" for letra in self.palavra]#Faz uma string de _ do mesmo tamanho da palavra
        self.letras_erradas = []
        #Cria o quadro, com uma lista de possívels posições da forca
        self.board = ['''

            +---+
            |   |
                |
                |
                |
                |
            =========''', '''

            +---+
            |   |
            O   |
                |
                |
                |
            =========''', '''

            +---+
            |   |
            O   |
            |   |
                |
                |
            =========''', '''

            +---+
            |   |
            O   |
            /|  |
                |
                |
            =========''', '''

            +---+
            |   |
            O   |
            /|\ |
                |
                |
            =========''', '''

            +---+
            |   |
            O   |
            /|\ |
            /   |
                |
            =========''', '''

            +---+
            |   |
            O   |
            /|\  |
            / \  |
                |
            =========''']
    def imprime_forca(self):#Imprime o board da forca
        print(self.board[len(self.letras_erradas)])
    def get_secreta(self):#Retorna a palavra secreta
        return self.palavra
    def set_erro(self, erro):#Faz um append nas letras erradas
        self.letras_erradas.append(erro)
    def get_erro(self): #Retorna as letras erradas
        return self.letras_erradas  
    def requisitar_palavra(self):#Solicita uma letra ao usuario e mantém em loop até ele digitar uma letra
        while(True):
            letra = input("\nDigite uma letra: ").lower()
            if len(letra) == 1 and letra.isalpha():#Verifica se foi realmente enviado uma letra
                return letra
            else:
                print("Você digitou um caracter invalido")
    def verifica_letra(self, tentativa):#Verifica se a letra faz parte da palavra
        if normalize(tentativa) in [normalize(letra) for letra in self.palavra]:
            return True
    def revelar_letra(self, tentativa):#Revela a letra nas posições onde estiver
        normalized_tentativa = tentativa
        for index, letra in enumerate(self.palavra):
            if normalize(letra) == normalized_tentativa:
                self.ocultada[index] = letra
    def verifica_vitoria(self):#Verifica se o jogo acabou com vitória
        if "_" not in self.ocultada:
            return True
        return False
    def verifica_derrota(self):#Verifica se o jogo acabou com derrota
        if self.chances <= 0:
            print("Você perdeu, a palavra era:", self.palavra)
            return True
        return False
def ingame():
    game = Forca()
    while game.chances > 0:
        limpa_tela()
        game.imprime_forca()
        print(" ".join(game.ocultada))
        print("\nChances restantes: ", game.chances)
        print("Letras erradas: ", " ".join(game.get_erro()))
        tentativa = game.requisitar_palavra()
        if game.verifica_letra(tentativa):
            game.revelar_letra(tentativa)
        else:
            game.chances -= 1
            game.set_erro(tentativa)
        if game.verifica_vitoria():
            print("Parabéns! A palavra era: ", game.palavra)
            break
    game.verifica_derrota()
if __name__ == "__main__":
    ingame()
    print("\nParabéns!")
