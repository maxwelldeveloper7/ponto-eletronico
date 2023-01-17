"""Este módulo contém classe e métodos da tela de cadastros"""
import re

from view.tela import Tela
from view.tela_colaboradores import TelaColaboradores


class TelaCadastros(Tela):
    """Desenha na tela uma tela de menu de Cadastros"""
    def exibir_menu(self) -> None:
        """Exibe cabeçalho e tela de menu"""
        opcao: int = 0
        mensagem: str = ""
        while True:
            # Menu
            self.escreve_titulo()
            print("Cadastros\n")
            print("1 - Colaboradores")
            print("2 - Horários")
            print("3 - Retornar\n")
            # Tratamento do que é informado pelo teclado utilizndo regex
            entrada: str = input(f"{mensagem}Digite uma opção: ")
            # O valor deve ser entre 1 e 3 inclusive, e deve conter apenas
            # um caractere
            padrao: str = "[1-3]"
            opcao_valida: bool = re.search(padrao,
                                           entrada) and len(entrada) == 1
            # Verifica se a opção é válida
            if opcao_valida:
                # reinicia o conteúda da mensagem
                mensagem: str = ""
                opcao = int(entrada)
                if opcao == 1:
                    self.abre_tela_colaboradores()
                elif opcao == 2:
                    continue
                elif opcao == 3:
                    break
            else:
                mensagem = "Opção inválida!!!\n"

    def abre_tela_colaboradores(self) -> None:
        """Abre a tela de Colaboradores"""
        tela_colaboradores = TelaColaboradores()
        tela_colaboradores.exibir_menu()
