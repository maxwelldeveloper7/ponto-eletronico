import re
from validate_docbr import CPF, PIS

from model.colaborador import Colaborador
from view.tela import Tela


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
        matricula: str = self.recebe_matricula()
        cpf: str = self.recebe_cpf()
        pis_pasep: str = self.recebe_pis_pasep()
        print(matricula, cpf, pis_pasep)
        input("pressione qualquer tecla para voltar")
        # pis_pasep: str = input("PIS/PASEP: ")
        # nome: str = input("Nome Completo: ")
        # cargo: str = input("Cargo: ")
        # data_admissao: str = input("Data de Admissão(dd/mm/aaaa): ")
        # colaborador: Colaborador = Colaborador(matricula, cpf, pis_pasep, nome,
        #                                        cargo, data_admissao)
        # print()
        # print(colaborador, "\n")
        # input("pressione qualquer tecla para voltar")

    def recebe_matricula(self) -> str:
        """ Recebe um número de matrícula pelo teclado e verifica se possui
            apenas digitos. Caso possua caracteres alfa os remove.
        Returns:
            str: Número de matrícula. apenas dígitos
        """
        matricula: str = input("Matrícula: ")
        padrao: str = "[0-9]{1,6}"
        matricula_valida: bool = re.findall(padrao, matricula)
        if matricula_valida:
            resposta = re.search(padrao, matricula)
            # Resposta da busca convertida em inteiro para formatar matrícula
            # com zeros a esquerda
            resposta_formatada = int(resposta.group())
            return str("{:06d}".format(resposta_formatada))
        else:
            return None

    def recebe_cpf(self) -> str:
        """ Recebe um CPF pelo teclado e verifica se possui 11 dígitos e se é
            válido.
        Returns:
            str: CPF válido ou None caso seja inválido
        """        
        cpf: str = input("CPF: ")
        if len(cpf) == 11:
            padrao: str = "[0-9]{11}"
            documento = re.search(padrao, cpf).group()
            validador = CPF()
            if validador.validate(documento):
                return documento
            else:
                return None
        else:
            return None

    def recebe_pis_pasep(self) -> str:
        """ Recebe um PIS/PASEP pelo teclado e verifica se possui 11 dígitos
            e se é válido.
        Returns:
            str: PIS/PASEP válido ou None caso seja inválido
        """        
        pis_pasep: str = input("PIS/PASEP: ")
        if len(pis_pasep) == 11:
            padrao: str = "[0-9]{11}"
            documento = re.search(padrao, pis_pasep).group()
            validador = PIS()
            if validador.validate(documento):
                return documento
            else:
                return None
        else:
            return None
