import os
import datetime
from constantes import TITULO_PRINCIPAL
import re
from model import Colaborador

class Tela:
    """Classe Tela"""
    def clear(self) -> None:
        """Limpa o terminal"""
        os.system('clear')
        command: str = 'clear'
        if os.name in ('nt', 'dos'):
            command = 'cls'
        os.system(command)

    def escreve_titulo(self) -> str:
        """Escreve o cabeçalho da tela com título"""
        self.clear()
        # pega a largura do titulo
        largura_titulo: int = int(len(TITULO_PRINCIPAL)) + 4
        emoji: str = "\u001b[32m\U00002721\u001b[m"  # emoji de um pc
        print(emoji * (largura_titulo))  # desenha borda superior
        # desenha titulo e bordas laterais
        print(emoji, TITULO_PRINCIPAL, emoji)
        print(emoji * (largura_titulo), "\n")  # desenha borda inferior
        # print("\u001b[32m\U00002721\u001b[m")

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

class TelaColaboradores(Tela):
    """Cria uma tela de cadastro de colaboradores"""
    def exibir_menu(self) -> None:
        """Exibe cabeçalho e tela de menu"""
        opcao: int = 0
        mensagem: str = ""
        while True:
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
        """Exibe tela de cadastro de colaboradores"""
        self.escreve_titulo()
        print("Novo colaborador\n")
        ''' lista de dados incompletos que serão utilizados num loop 
            e finalizará assim que essa lista seja esvaziada a media
            que todos os dados forem informados
        '''
        campos_incompletos = ['matricula', 'cpf', 'pispasep', 'nome', 'cargo',
                              'admissao']
        matricula: str = input("Matrícula: ")
        cpf: str = input("CPF: ")
        pis_pasep: str = input("PIS/PASEP: ")
        nome: str = input("Nome Completo: ")
        cargo: str = input("Cargo: ")
        data_admissao: str = input("Data de Admissão(dd/mm/aaaa): ")
        colaborador: Colaborador = Colaborador(matricula, cpf, pis_pasep, nome,
                                               cargo, data_admissao)
        print()
        print(colaborador, "\n")
        input("pressione qualquer tecla para voltar")

class TelaRegistros(Tela):
    """Exibe tela de registros"""
    def exibir_menu(self):
        """Exibe o menu"""
        opcao = ""
        while True:
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
        """Exibe data e hora do sistema"""
        data = datetime.datetime.now()
        data_texto = data.strftime('Data e Hora: %d/%m/%Y - %H:%M')
        print(data_texto)
