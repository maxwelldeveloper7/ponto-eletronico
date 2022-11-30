import os

from view.constantes import TITULO_PRINCIPAL


class Tela:
    def clear(self) -> None:
        os.system('clear')
        command: str = 'clear'
        if os.name in ('nt', 'dos'):
            command = 'cls'
        os.system(command)

    def escreve_titulo(self) -> str:
        self.clear()
        largura_titulo: int = int(len(TITULO_PRINCIPAL)) + 4  # pega a largura do titulo
        pc: str = "\u001b[32m\U00002721\u001b[m"  # emoji de um pc
        print(pc * (largura_titulo))  # desenha borda superior
        print(pc, TITULO_PRINCIPAL, pc)  # desenha titulo e bordas laterais
        print(pc * (largura_titulo), "\n")  # desenha borda inferior
        # print("\u001b[32m\U00002721\u001b[m")
