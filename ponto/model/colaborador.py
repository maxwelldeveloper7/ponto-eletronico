from model.utilitarios import Entrada


class Colaborador:
    def __init__(self, matricula: str, cpf: str, pispasep: str, nome: str,
                 cargo: str, admissao: str) -> None:
        self._matricula = Entrada.recebe_matricula(matricula)
        self._cpf = Entrada.recebe_cpf(cpf)
        self._pispasep = Entrada.recebe_pis_pasep(pispasep)
        self._nome = Entrada.recebe_nome(nome)
        self._cargo = Entrada.recebe_nome(cargo)
        self._admissao = Entrada.recebe_data(admissao)

    @property
    def matricula(self):
        return self._matricula

    @property
    def cpf(self):
        return self._cpf

    @property
    def pispasep(self):
        return self._pispasep

    @property
    def nome(self):
        return self._nome

    @property
    def cargo(self):
        return self._cargo

    @property
    def admissao(self):
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

    def dados_incompletos(self) -> list:
        """ Verifica se há atributos com valor None e os inclui em uma lista
        de String. Caso contrário retorna None:

        Returns:
            list: or None:
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
        if len(dados_incompletos) > 0:
            return dados_incompletos
        else:
            return None

    def __str__(self) -> str:
        return 'Matrícula: {}\nCPF: {}\nPIS/PASEP: {}\nNome: {}\nCargo: {}\
            \nAdmissão: {}\nCampos Vazios: {}'.format(
            self.matricula, self.cpf, self.pispasep, self.nome,
            self.cargo, self.admissao, self.dados_incompletos()
        )
