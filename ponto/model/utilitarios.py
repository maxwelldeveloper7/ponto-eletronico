import re
from validate_docbr import CPF, PIS


class Entrada:
    def numero_inteiro(valor: str) -> int:
        """ Remove caracteres que não sejam dígitos

        Args:
            valor (str): recebe dados digitados pelo usuário

        Returns:
            int: retona um número inteiro caso o campo filtro não esteja vazio
        """
        # filtra o valor informado e remove tudo que não for dígito
        filtro: str = ''.join([i for i in valor if i.isdigit()])
        # atribue None ao filtro caso esteja vazio
        if len(filtro) == 0:
            filtro = None
        # tenta atribuir os digitos filtrados ao campo dígitos e o retorna
        try:
            digitos = int(filtro)
            return digitos
        except Exception:
            # ao falhar exibe esta mensagem
            print('Campo vazio')
            # raise
            return None

    def recebe_matricula(label: str) -> str:
        """ Recebe um número de matrícula pelo teclado e verifica se possui
            apenas digitos. Caso possua caracteres alfa os remove.
        
        Args:
            label (str): texto informando o que deve ser inserido
        
        Returns:
            str: Número de matrícula. apenas dígitos
        """
        try:
            matricula: str = str(Entrada.numero_inteiro(label))
            padrao: str = "[0-9]{1,6}"
            matricula_valida: bool = re.findall(padrao, matricula)
            if matricula_valida:
                resposta = re.search(padrao, matricula)            
                # Se a matrícula for 0 lança uma exceção e retorna None
                if int(resposta.group()) == 0:
                    raise
                # Resposta da busca convertida em inteiro para formatar
                # matrícula
                # com zeros a esquerda            
                return str("{:06d}".format(int(resposta.group())))
            # se não estiver dentro do padrão lança exceçao e retorna None
            else:
                raise
        except Exception:
            print('Matrícula inválida...')
            return None

    def recebe_cpf(label: str) -> str:
        """Recebe um CPF pelo teclado e verifica se possui 11 dígitos e se é
            válido.

        Args:
            label (str): texto informando o que deve ser inserido

        Returns:
            str: CPF válido ou None caso seja inválido
        """
             
        cpf: str = label
        try:
            if len(cpf) == 11:
                padrao: str = "[0-9]{11}"
                documento = re.search(padrao, cpf).group()
                validador = CPF()
                if validador.validate(documento):
                    return documento
                else:
                    raise
            else:
                raise
        except Exception:
            print('CPF inválido.')
            return None

    def recebe_pis_pasep(label: str) -> str:
        """ Recebe um PIS/PASEP pelo teclado e verifica se possui 11 dígitos
            e se é válido.
            
        Args:
            label (str): texto informando o que deve ser inserido    
            
        Returns:
            str: PIS/PASEP válido ou None caso seja inválido
        """
        pis_pasep: str = label
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

    def recebe_texto(label: str) -> str:
        """Remove dígitos do nome completo

        Args:
            label (str): texto informando o que deve ser inserido

        Returns:
            str: Nome Completo
        """
        entrada: str = label
        nome: str = ''.join([i for i in entrada if not i.isdigit()])
        nome = nome.lower()
        if len(nome) > 1:
            return nome
        else:
            return None    

    def recebe_data(dt: str) -> str:
        """Recebe uma data no formato ddMMaaa ou dd/MM/aaaa

        Args:
            dt (str): texto informando o que deve ser inserido

        Returns:
            str: retorna uma data no formato dd/MM/aaaa
        """
        data: str = dt
        padrao: str = "[0-9]{2}/[0-9]{2}/[0-9]{4}"        
        dado_valido: bool = re.findall(padrao, data)
        if dado_valido:
            resposta = re.search(padrao, data)            
            return resposta.group()            
        else:
            return None

class Validar:
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
        anos: range = range(1900,2091)# 2091 exclusive
        meses: range = range(1,13)# 13 exclusive
        dias: range = range(1,32)# 32 exclusive
        mes_com_trinta_um_dias: tuple = (1,3,5,7,8,10,12)
        mes_com_trinta_dias: tuple = (4,6,9,11)
        mes_vinte_oito_ou_vinte_nove_dias: int = 2
        dia_valido = False
        mes_valido = False
        ano_valido = False
        try:
            # testa se dia, mês e ano estão dentro do padrão
            if (dia not in dias or mes not in meses or ano not in anos):
                raise
            # a partir daqui todos os anos são válidos
            ano_valido = True
            if mes in mes_com_trinta_um_dias and dia <=31:
                mes_valido = True
                dia_valido = True
            elif mes in mes_com_trinta_dias and dia <=30:
                mes_valido = True
                dia_valido = True
            elif mes == mes_vinte_oito_ou_vinte_nove_dias:
                mes_valido = True
                if Validar.ano_bissexto(ano) and dia <=29:
                    dia_valido = True
                elif dia <=28:
                    dia_valido = True
                else:
                    raise
            else:
                raise
        except Exception:
            print('Data inválida')
        return ano_valido and mes_valido and dia_valido

    def ano_bissexto(ano: int) -> bool:
        """ Verifica se um ano é bissexto

        Args:
            ano (int): Ano no formato aaaa

        Returns:
            bool: retorna True se verdadeiro ou False caso não seja bissexto
        """
        if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
            return True
        else:
            return False
