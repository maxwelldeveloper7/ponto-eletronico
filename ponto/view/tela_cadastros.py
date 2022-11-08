from view.tela import Tela
from view.tela_colaboradores import TelaColaboradores


class TelaCadastros(Tela):
    def __init__(self) -> None:
        super().__init__()

    def exibir_menu(self) -> None:
        opcao = 0
        while (True):
            self.escreve_titulo()
            print("Cadastros\n")
            print("1 - Colaboradores")
            print("2 - Horários")
            print("3 - Retornar\n")
            opcao = int(input("Digite uma opção: "))
            if opcao == 1:
                tela_colaboradores = TelaColaboradores()
                tela_colaboradores.exibir_menu()
            elif opcao == 3:
                break