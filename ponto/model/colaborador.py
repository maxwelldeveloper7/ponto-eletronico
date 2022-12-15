from view.entrada import Entrada


class Colaborador:
    def __init__(self, matricula: str, cpf: str, pispasep: str, nome: str,
                 cargo: str, admissao: str) -> None:
        self._matricula = Entrada.numero_inteiro(matricula)
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
        self._matricula = Entrada.numero_inteiro(matricula)

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

    def dados_incompletos(self) -> list:
        """ Verifica se há atributos com valor None e os inclui em uma lista de String.
            Caso contrário retorna None:

        Returns:
            list: or None: 
        """
        dados_incompletos: list = []
        if self.matricula == None:
            dados_incompletos.append('matricula')
        elif self.cpf == None:
            dados_incompletos.append('cpf')
        elif self.pispasep == None:
            dados_incompletos.append('pispasep')
        elif self.nome == None:
            dados_incompletos.append('nome')
        elif self.cargo == None:
            dados_incompletos.append('cargo')
        elif self.admissao == None:
            dados_incompletos.append('admissao')
        if(len(dados_incompletos) > 0):
            return dados_incompletos
        else:
            return None

    def __str__(self) -> str:
        return 'Matrícula: {}\nCPF: {}\nPIS/PASEP: {}\nNome: {}\nCargo: {}\
            \nAdmissão: {}\nCampos Vazios: {}'.format(
            self.matricula, self.cpf, self.pispasep, self.nome,
            self.cargo, self.admissao, self.dados_incompletos()
        )
