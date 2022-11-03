class Colaborador:
    def __init__(self, matricula, cpf, pispasep, nome, cargo, admissao):
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
    def cargo(self) -> str:
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
    def cpf(self, pispasep):
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

    def __str__(self):
        return f'Matricula: {self._matricula}\
            nCPF: {self._cpf}\
                nPIS/PASEP: {self._pispasep}\
                    nNome: {self.nome}\
                        nCargo: {self.cargo}\
                            nAdmissao: {self._admissao}'