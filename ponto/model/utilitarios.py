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
        except TypeError:
            # ao falhar exibe esta mensagem
            print('Campo vazio')
            # raise

    def recebe_matricula(label: str) -> str:
        """ Recebe um número de matrícula pelo teclado e verifica se possui
            apenas digitos. Caso possua caracteres alfa os remove.
        
        Args:
            label (str): texto informando o que deve ser inserido
        
        Returns:
            str: Número de matrícula. apenas dígitos
        """
        matricula: str = label
        padrao: str = "[0-9]{1,6}"
        matricula_valida: bool = re.findall(padrao, matricula)
        if matricula_valida:
            resposta = re.search(padrao, matricula)            
            # Se a matrícula for 0 retorna None
            if int(resposta.group()) == 0:
                return None
            # Resposta da busca convertida em inteiro para formatar matrícula
            # com zeros a esquerda            
            return str("{:06d}".format(int(resposta.group())))
        else:
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

    def data_valida(self, data: str) -> bool:
        # verifica de a data é válida
        dia: int = int(data[0:2])
        mes: int = int(data[3:5])
        ano: int = int(data[6:])
        data_valida: bool = False
        if ano in range(1900,2090):
            data_valida = True
            if mes in range(1,13):
                if dia in range(1,32):
                    # Meses com 31 dias
                    if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or \
                        mes == 8 or mes == 10 or mes == 12):
                        if(dia <= 31):
                            data_valida = True
                    # Meses com 30 dias
                    elif (mes == 4 or mes == 6 or mes == 9 or mes == 11):
                        if(dia<=30):
                            data_valida = True
                    elif mes == 2:
                        # Testa se é bissexto
                        if(ano%4 == 0 and ano%100 !=0) or (ano%400 == 0):
                            if(dia<=29):
                                data_valida = True
                        elif(dia<=28):
                            data_valida = True
                else:
                    print("dia inválido")
                    data_valida = False
            else: 
                print("mês inválido")
                data_valida = False
        else:
            print("ano inválido")
            data_valida = False
        return data_valida