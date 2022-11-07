from view.tela import Tela
from model.colaborador import Colaborador


class TelaColaboradores(Tela):
    def __init__(self) -> None:
        super().__init__()

    def exibir_menu(self) -> None:
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
                self.cadastro()
            elif opcao == 6:
                break

    def cadastro(self) -> None:
        self.escreve_titulo()
        print("Novo colaborador\n")
        matricula = input("Matrícula: ")
        cpf = input("CPF: ")
        pis_pasep = input("PIS/PASEP: ")
        nome = input("Nome Completo: ")
        cargo = input("Cargo: ")
        data_admissao = input("Data de Admissão(dd/mm/aaaa): ")
        colaborador = Colaborador(matricula, cpf, pis_pasep, nome, cargo,
                                  data_admissao)
        print()
        print(colaborador,"\n")
        input("pressione qualquer tecla para voltar")
