from view.tela import Tela
from view.tela_cadastros import TelaCadastros
from view.tela_registros import TelaRegistros


class TelaPrincipal(Tela):
    def __init__(self) -> None:
        super().__init__()

    def exibe_menu(self):
        opcao = 0
        while (True):
            self.escreve_titulo()
            print("Menu\n")
            print("1 - Registrar")
            print("2 - Cadastros")
            print("3 - Sair\n")
            opcao = int(input("Digite uma opção: "))
            if opcao == 1:
                tela_registros  = TelaRegistros()
                tela_registros.exibir_menu()
            elif opcao == 2:
                tela_cadastros = TelaCadastros()
                tela_cadastros.exibir_menu()
            elif opcao == 3:
                break
