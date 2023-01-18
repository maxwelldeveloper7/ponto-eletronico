import re
from validate_docbr import CPF, PIS


class Entrada:
    """Classe Entrada - recebe dados, tratamento de exceções,
    e retorna dados devidamente tratados ou None
    """
    @staticmethod
    def numero_inteiro(valor: str) -> int:
        """ Remove caracteres que não sejam dígitos

        Args:
            valor (str): recebe dados digitados pelo usuário

        Returns:
            int: retona um número inteiro e None caso o campo filtro não esteja
        vazio
        """
        # filtra o valor informado e remove tudo que não for dígito
        filtro: str = ''.join([i for i in valor if i.isdigit()])
        # tenta atribuir os digitos filtrados ao campo dígitos e o retorna
        try:
            # dispara exceção caso esteja vazio
            if len(filtro) == 0:
                raise ValueError
            digitos = int(filtro)
            return digitos
        except ValueError:
            valor = "''"
            print('Campo vazio ->', valor)
            return None

    @staticmethod
    def recebe_matricula(arg: str) -> str:
        """ Recebe um número de matrícula pelo teclado e verifica se possui
            apenas digitos. Caso possua caracteres alfa os remove.
        Args:
            label (str): texto informando o que deve ser inserido
        Returns:
            str: Número de matrícula. apenas dígitos
        """
        matricula: str = str(Entrada.numero_inteiro(arg))
        try:
            padrao: str = "[0-9]{1,6}"
            matricula_valida: bool = re.findall(padrao, matricula)
            if matricula_valida:
                resposta = re.search(padrao, matricula)
                # Se a matrícula for 0 lança uma exceção e retorna None
                if int(resposta.group()) == 0:
                    raise ValueError
                # Resposta da busca convertida em inteiro para formatar
                # matrícula
                # com zeros a esquerda
                # return str("{:06d}".format(int(resposta.group())))
                return f'{int(resposta.group()):06d}'
            # se não estiver dentro do padrão lança exceçao e retorna None
            raise ValueError
        except ValueError:
            if len(arg) == 0:
                arg = 'Campo vazio'
            print('Matrícula inválida ->', arg)
            return None

    @staticmethod
    def recebe_cpf(arg: str) -> str:
        """Recebe um CPF pelo teclado e verifica se possui 11 dígitos e se é
            válido.

        Args:
            label (str): texto informando o que deve ser inserido

        Returns:
            str: CPF válido ou None caso seja inválido
        """

        cpf: str = arg
        try:
            if len(cpf) == 11:
                padrao: str = "[0-9]{11}"
                documento = re.search(padrao, cpf).group()
                validador = CPF()
                if validador.validate(documento):
                    return documento
            raise ValueError
        except ValueError:
            if len(arg) == 0:
                arg = 'Campo vazio'
            print('CPF inválido ->', arg)
            return None

    @staticmethod
    def recebe_pis_pasep(arg: str) -> str:
        """ Recebe um PIS/PASEP pelo teclado e verifica se possui 11 dígitos
            e se é válido.
        Args:
            label (str): texto informando o que deve ser inserido
        Returns:
            str: PIS/PASEP válido ou None caso seja inválido
        """
        pis_pasep: str = arg
        try:
            if len(pis_pasep) == 11:
                padrao: str = "[0-9]{11}"
                documento = re.search(padrao, pis_pasep).group()
                validador = PIS()
                if validador.validate(documento):
                    return documento
            raise ValueError
        except ValueError:
            if len(arg) == 0:
                arg = 'Campo vazio'
            print('PIS/PASEP inválido ->', arg)
            return None

    @staticmethod
    def recebe_nome(arg: str) -> str:
        """Remove dígitos do nome completo

        Args:
            label (str): texto informando o que deve ser inserido

        Returns:
            str: Nome Completo
        """
        try:
            entrada: str = arg
            nome: str = ''.join([i for i in entrada if not i.isdigit()])
            nome = nome.lower()
            if len(nome) > 1:
                return nome
            raise ValueError
        except ValueError:
            if len(arg) == 0:
                arg = 'Campo vazio'
            print('Dado inválido ->', arg)
            return None

    @staticmethod
    def recebe_data(arg: str) -> str:
        """Recebe uma data no formato ddMMaaa ou dd/MM/aaaa

        Args:
            dt (str): texto informando o que deve ser inserido

        Returns:
            str: retorna uma data no formato dd/MM/aaaa
        """
        data: str = arg
        padrao: str = "[0-9]{2}/[0-9]{2}/[0-9]{4}"
        esta_no_padrao: bool = re.findall(padrao, data)
        if esta_no_padrao:
            data_padronizada = re.search(padrao, data)
            Validar.data(data_padronizada.group())
            return data_padronizada.group()
        if len(data) == 0:
            data = 'Campo vazio'
        print('Data inválida ->', data)
        return None


class Validar:
    """Realiza validações de datas"""
    @staticmethod
    def data(data: str) -> bool:
        """Recebe uma data em string e verifica se é uma data válida
        Args:
            data (str): data em string no formato dd/MM/YYYY
        Returns:
            bool: Retorna True se for uma data válida e False caso seja
            inválida
        """
        dia: int = int(data[0:2])
        mes: int = int(data[3:5])
        ano: int = int(data[6:])
        anos: range = range(1900, 2091)  # 2091 exclusive
        meses: range = range(1, 13)  # 13 exclusive
        dias: range = range(1, 32)  # 32 exclusive
        mes_com_trinta_um_dias: tuple = (1, 3, 5, 7, 8, 10, 12)
        mes_com_trinta_dias: tuple = (4, 6, 9, 11)
        mes_vinte_oito_ou_vinte_nove_dias: int = 2
        dia_valido = False
        mes_valido = False
        ano_valido = False
        try:
            # testa se dia, mês e ano estão dentro do padrão
            if (dia not in dias or mes not in meses or ano not in anos):
                raise ValueError
            # a partir daqui todos os anos são válidos
            ano_valido = True
            if mes in mes_com_trinta_um_dias and dia <= 31:
                mes_valido = True
                dia_valido = True
            elif mes in mes_com_trinta_dias and dia <= 30:
                mes_valido = True
                dia_valido = True
            elif mes == mes_vinte_oito_ou_vinte_nove_dias:
                mes_valido = True
                if Validar.ano_bissexto(ano) and dia <= 29:
                    dia_valido = True
                elif dia <= 28:
                    dia_valido = True
                else:
                    raise ValueError
            else:
                raise ValueError
        except ValueError:
            print('Data inválida ->', data)
        return ano_valido and mes_valido and dia_valido

    @staticmethod
    def ano_bissexto(ano: int) -> bool:
        """ Verifica se um ano é bissexto

        Args:
            ano (int): Ano no formato aaaa

        Returns:
            bool: retorna True se verdadeiro ou False caso não seja bissexto
        """
        return (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0
