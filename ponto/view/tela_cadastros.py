import re

from view.tela import Tela
from view.tela_colaboradores import TelaColaboradores


class TelaCadastros(Tela):
    def __init__(self) -> None:
        super().__init__()

    def exibir_menu(self) -> None:
        opcao: int = 0
        mensagem: str = ""
        while (True):
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
            padrao = "([1-3])"
            opcao_valida = re.search(padrao, entrada) and len(entrada) == 1
            # Verifica se a opção é válida
            if opcao_valida:
                # reinicia o conteúda da mensagem
                mensagem = ""
                opcao = int(entrada)
                if opcao == 1:
                    tela_colaboradores = TelaColaboradores()
                    tela_colaboradores.exibir_menu()
                elif opcao == 2:
                    continue
                elif opcao == 3:
                    break
            else:
                mensagem = "Opção inválida!!!\n"
