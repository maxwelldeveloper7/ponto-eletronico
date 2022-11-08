class Colaborador:
    def __init__(self, matricula: str, cpf: str, pispasep: str, nome: str,
                 cargo: str, admissao: str) -> None:
        self._matricula = matricula
        self._cpf = cpf
        self._pispasep = pispasep
        self._nome = nome
        self._cargo = cargo
        self._admissao = admissao

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
        return self._nome.title()

    @property
    def cargo(self):
        return self._cargo.title()

    @property
    def admissao(self):
        return self._admissao

    @matricula.setter
    def matricula(self, matricula):
        self._matricula = matricula

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    @pispasep.setter
    def pispasep(self, pispasep):
        self._pispasep = pispasep

    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()

    @cargo.setter
    def cargo(self, cargo):
        self._cargo = cargo.title()

    @admissao.setter
    def admissao(self, admissao):
        self._admissao = admissao

    def __str__(self) -> str:
        return 'Matrícula: {}\nCPF: {}\nPIS/PASEP: {}\nNome: {}\nCargo: {}\
            \nAdmissão: {}'.format(
            self.matricula, self.cpf, self.pispasep, self.nome,
            self.cargo, self.admissao
        )
