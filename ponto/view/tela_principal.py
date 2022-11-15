import re

from view.tela import Tela
from view.tela_cadastros import TelaCadastros
from view.tela_registros import TelaRegistros


class TelaPrincipal(Tela):
    def __init__(self) -> None:
        super().__init__()

    def exibe_menu(self):
        opcao: int = 0
        mensagem: str = ""
        while (True):
            # Menu
            self.escreve_titulo()
            print("Menu\n")
            print("1 - Registrar")
            print("2 - Cadastros")
            print("3 - Sair\n")
            # Tratamento do que é informado pelo teclado utilizando regex
            entrada: str = input(f"{mensagem}Digite uma opção: ")
            # O valor deve ser entre 1 a 3 inclusive, e deve conter apenas
            # um caractere
            padrao: str = "[1-3]"
            opcao_valida: bool = re.search(padrao, entrada) and len(
                entrada) == 1
            # Verifica se a opção é válida
            if opcao_valida:
                # reinicia conteúdo da mensagem
                mensagem: str = ""
                opcao = int(entrada)
                if opcao == 1:
                    tela_registros = TelaRegistros()
                    tela_registros.exibir_menu()
                elif opcao == 2:
                    tela_cadastros = TelaCadastros()
                    tela_cadastros.exibir_menu()
                elif opcao == 3:
                    break
            else:
                mensagem = "Opção inválida!!!\n"
