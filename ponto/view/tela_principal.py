import datetime

from view.tela import Tela
from view.tela_cadastros import TelaCadastros
from view.tela_colaboradores import TelaColaboradores


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
                self.registrar()
            elif opcao == 2:
                tela_cadastros = TelaCadastros()
                tela_cadastros.exibir_menu()
            elif opcao == 3:
                break

    def registrar(self):
        opcao = ""
        while (True):
            self.escreve_titulo()
            self.exibir_data_hora()
            matricula = int(input("Digite o número de sua matrícula: "))
            print(matricula)
            opcao = input(
                "Deseja realizar outro registro?(S para sim ou enter para sair):"
                ).lower()
            if opcao != "s":
                break
    
    def exibir_data_hora(self):
        data = datetime.datetime.now()
        data_texto = data.strftime('Data e Hora: %d/%m/%Y - %H:%M')
        print(data_texto)
