import random as rand
from os import system, name
import unicodedata
def limpa_tela():
    #Windows
    if name == "nt":
        _ = system("cls")
    #Mac ou Linux
    else:
        _ = system("clear")
class Forca:
    def __init__(self):
        self.chances = 6
        with open("wl.txt", "r", encoding="utf-8") as wl:
            self.wl = wl.read().replace(" ", "").split(",")
        self.palavra = rand.choice(self.wl).lower()
        self.ocultada = ["_" for letra in self.palavra]
        self.letras_erradas = []
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
    def imprime_forca(self):
        print(self.board[len(self.letras_erradas)])
    def get_secreta(self):
        return self.palavra
    def set_erro(self, erro):
        self.letras_erradas.append(erro)
    def get_erro(self): 
        return self.letras_erradas
    def verificar_letra(self, letra):
        if len(letra) == 1 and letra.isalpha():
            return True
    def revelar_letra(self, tentativa):
        normalized_tentativa = tentativa
        for index, letra in enumerate(self.palavra):
            if self.normalize(letra) == normalized_tentativa:
                self.ocultada[index] = letra
    def normalize(self, letra):
        return unicodedata.normalize('NFKD', letra).encode('ASCII', 'ignore').decode('ASCII')
    def verifica_vitoria(self):
        if "_" not in self.ocultada:
            return True
        return False
    def verifica_derrota(self):
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
        while(True):
            tentativa = input("\nDigite uma letra: ").lower()
            if game.verificar_letra(tentativa):
                break
            else:
                print("Você digitou um caracter invalido")
        if game.normalize(tentativa) in [game.normalize(letra) for letra in game.palavra]:
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
