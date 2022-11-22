import re

from model.colaborador import Colaborador
from view.tela import Tela
from view.entrada import Entrada


class TelaColaboradores(Tela):
    def __init__(self) -> None:
        super().__init__()

    def exibir_menu(self) -> None:
        opcao: int = 0
        mensagem: str = ""
        while (True):
            # Menu
            self.escreve_titulo()
            print("Colaboradores\n")
            print("1 - Cadastrar")
            print("2 - Alterar")
            print("3 - Inativar")
            print("4 - Listar")
            print("5 - Retornar\n")
            # Tratamento do que é informado pelo teclado utilizando regex
            entrada: str = input(f"{mensagem}Digite uma opção: ")
            # O valor de ser entre 1 a 5 inclusive, e deve conter apenas
            # um caractere
            padrao: str = "[1-5]"
            opcao_valida: bool = re.search(padrao, entrada) and len(
                entrada) == 1
            # Verifica se a opção é válida
            if opcao_valida:
                mensagem = ""
                opcao = int(entrada)
                if opcao == 1:
                    self.cadastro()
                elif opcao == 2:
                    continue
                elif opcao == 3:
                    continue
                elif opcao == 4:
                    continue
                elif opcao == 5:
                    break
            else:
                mensagem = "Opção inválida!!!\n"

    def cadastro(self) -> None:
        self.escreve_titulo()
        print("Novo colaborador\n")
        matricula: str = Entrada.recebe_matricula("Matrícula: ")
        cpf: str = Entrada.recebe_cpf("CPF: ")
        pis_pasep: str = Entrada.recebe_pis_pasep("PIS/PASEP: ")
        nome: str = Entrada.recebe_texto("Nome Completo: ")
        cargo: str = Entrada.recebe_texto("Cargo: ")
        data: str = Entrada.recebe_data("Data de Admissão(dd/MM/aaaa): ")
        print(matricula, cpf, pis_pasep, nome, cargo, data)
        input("pressione qualquer tecla para voltar")
        
        # data_admissao: str = input("Data de Admissão(dd/mm/aaaa): ")
        # colaborador: Colaborador = Colaborador(matricula, cpf, pis_pasep, nome,
        #                                        cargo, data_admissao)
        # print()
        # print(colaborador, "\n")
        # input("pressione qualquer tecla para voltar")
