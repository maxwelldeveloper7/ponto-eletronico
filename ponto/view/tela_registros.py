import datetime

from view.tela import Tela


class TelaRegistros(Tela):
    def __init__(self) -> None:
        super().__init__()

    def exibir_menu(self):
        opcao = ""
        while (True):
            self.escreve_titulo()
            self.exibir_data_hora()
            matricula = int(input("Digite o número de sua matrícula: "))
            print(matricula)
            opcao = input(
                "Deseja realizar outro registro?\
                    (S para sim ou enter para sair):"
                ).lower()
            if opcao != "s":
                break

    def exibir_data_hora(self):
        data = datetime.datetime.now()
        data_texto = data.strftime('Data e Hora: %d/%m/%Y - %H:%M')
        print(data_texto)
