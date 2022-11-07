import datetime

from view.tela import Tela
from model.colaborador import Colaborador


class TelaPrincipal(Tela):
    def __init__(self) -> None:
        ...


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
                self.cadastrar()
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


    def cadastrar(self):
        opcao = 0
        while (True):
            self.escreve_titulo()
            print("Cadastros\n")
            print("1 - Colaboradores")
            print("2 - Horários")
            print("3 - Retornar\n")
            opcao = int(input("Digite uma opção: "))
            if opcao == 1:
                self.colaboradores()
            elif opcao == 3:
                break


    def colaboradores(self):
        opcao = 0
        while (True):
            self.escreve_titulo()
            print("Colaboradores\n")
            print("1 - Cadastrar")
            print("2 - Alterar")
            print("3 - Inativar")
            print("5 - Listar")
            print("6 - Retornar\n")
            opcao = int(input("Digite uma opção: "))
            if opcao == 1:
                self.cadastrar_colaborador()
            elif opcao == 6:
                break


    def cadastrar_colaborador(self):
        self.escreve_titulo()
        print("Novo colaborador\n")
        matricula = int(input("Matrícula: "))
        cpf = input("CPF: ")
        pis_pasep = int(input("PIS/PASEP: "))
        nome = input("Nome Completo: ")
        cargo = input("Cargo: ")
        data_admissao = input("Data de Admissão(dd/mm/aaaa): ")
        colaborador = Colaborador(matricula, cpf, pis_pasep, nome, cargo, data_admissao)
        print()
        print(colaborador)
        print()
        input("pressione qualquer tecla para voltar")


    def exibir_data_hora(self):
        data = datetime.datetime.now()
        data_texto = data.strftime('Data e Hora: %d/%m/%Y - %H:%M')
        print(data_texto)