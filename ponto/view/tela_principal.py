"""Este módulo possui a Classe TelaPrincipal"""
import re

from view.tela import Tela
from view.tela_cadastros import TelaCadastros
from view.tela_registros import TelaRegistros


class TelaPrincipal(Tela):
    """Classe TelaPrincipal"""
    def exibe_menu(self):
        """Exibe cabeçalho do sistema e menu da tela principal"""
        opcao: int = 0
        mensagem: str = ""
        while True:
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
                    self.abre_tela_de_registros()
                elif opcao == 2:
                    self.abre_tela_de_cadastros()
                elif opcao == 3:
                    break
            else:
                mensagem = "Opção inválida!!!\n"

    def abre_tela_de_registros(self) -> None:
        """Instancia tela de registros e exibe o menu"""
        tela_registros = TelaRegistros()
        tela_registros.exibir_menu()

    def abre_tela_de_cadastros(self):
        """Instancia tela de cadastros e exibe o menu"""
        tela_cadastros = TelaCadastros()
        tela_cadastros.exibir_menu()
