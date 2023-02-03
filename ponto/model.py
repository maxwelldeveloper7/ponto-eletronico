"""Este módulo contém a classe Colaborador"""
from utilitarios import Entrada


class Colaborador:
    """Classe Colaborador"""
    def __init__(self, matricula: str, cpf: str, pispasep: str, nome: str,
                 cargo: str, admissao: str) -> None:
        """Método construtor"""
        self._matricula = Entrada.recebe_matricula(matricula)
        self._cpf = Entrada.recebe_cpf(cpf)
        self._pispasep = Entrada.recebe_pis_pasep(pispasep)
        self._nome = Entrada.recebe_nome(nome)
        self._cargo = Entrada.recebe_nome(cargo)
        self._admissao = Entrada.recebe_data(admissao)

    @property
    def matricula(self):
        """Retorna uma matrícula"""
        return self._matricula

    @property
    def cpf(self):
        """Retorna um CPF"""
        return self._cpf

    @property
    def pispasep(self):
        """Retorna um PIS/PASEP"""
        return self._pispasep

    @property
    def nome(self):
        """Retorna um Nome"""
        return self._nome

    @property
    def cargo(self):
        """Retorna um Cargo"""
        return self._cargo

    @property
    def admissao(self):
        """Retorna uma data de admissão"""
        return self._admissao

    @matricula.setter
    def matricula(self, matricula):
        self._matricula = Entrada.recebe_matricula(matricula)

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = Entrada.recebe_cpf(cpf)

    @pispasep.setter
    def pispasep(self, pispasep):
        self._pispasep = Entrada.recebe_pis_pasep(pispasep)

    @nome.setter
    def nome(self, nome):
        self._nome = Entrada.recebe_nome(nome)

    @cargo.setter
    def cargo(self, cargo):
        self._cargo = Entrada.recebe_nome(cargo)

    @admissao.setter
    def admissao(self, admissao):
        self._admissao = Entrada.recebe_data(admissao)

    def verifica_dados_incompletos(self) -> list:
        """ Verifica se há atributos com valor None e retorna uma lista
        com os dados imcompletos
        Returns:
            list:
        """
        dados_incompletos: list = []
        if self.matricula is None:
            dados_incompletos.append('matricula')
        if self.cpf is None:
            dados_incompletos.append('cpf')
        if self.pispasep is None:
            dados_incompletos.append('pispasep')
        if self.nome is None:
            dados_incompletos.append('nome')
        if self.cargo is None:
            dados_incompletos.append('cargo')
        if self.admissao is None:
            dados_incompletos.append('admissao')
        return dados_incompletos

    def dados_incompletos(self) -> bool:
        """Verifica de há se a campos incompletos na lista"""
        return len(self.verifica_dados_incompletos()) != 0

    def __str__(self) -> str:
        # return 'Matrícula: {}\nCPF: {}\nPIS/PASEP: {}\nNome: {}\nCargo: {}\
        #     \nAdmissão: {}\nCampos Vazios: {}'.format(
        #     self.matricula, self.cpf, self.pispasep, self.nome,
        #     self.cargo, self.admissao, self.dados_incompletos()
        # )
        colaborador_str = ''
        colaborador_str += f'Matrícula: {self.matricula}\n'
        colaborador_str += f'CPF: {self.cpf}\n'
        colaborador_str += f'PIS/PASEP: {self.pispasep}\n'
        colaborador_str += f'Nome: {self.nome}\n'
        colaborador_str += f'Cargo: {self.cargo}\n'
        colaborador_str += f'Data de admissão: {self.admissao}\n'
        return colaborador_str
