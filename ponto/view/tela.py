"""Este módulo possui a Classe Tela"""
import os

from view.constantes import TITULO_PRINCIPAL


class Tela:
    """Classe Tela"""
    def clear(self) -> None:
        """Limpa o terminal"""
        os.system('clear')
        command: str = 'clear'
        if os.name in ('nt', 'dos'):
            command = 'cls'
        os.system(command)

    def escreve_titulo(self) -> str:
        """Escreve o cabeçalho da tela com título"""
        self.clear()
        # pega a largura do titulo
        largura_titulo: int = int(len(TITULO_PRINCIPAL)) + 4
        emoji: str = "\u001b[32m\U00002721\u001b[m"  # emoji de um pc
        print(emoji * (largura_titulo))  # desenha borda superior
        print(emoji, TITULO_PRINCIPAL, emoji)  # desenha titulo e bordas laterais
        print(emoji * (largura_titulo), "\n")  # desenha borda inferior
        # print("\u001b[32m\U00002721\u001b[m")
