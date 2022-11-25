import re
from validate_docbr import CPF, PIS


class Entrada:    
    def recebe_matricula(label: str) -> str:
        """ Recebe um número de matrícula pelo teclado e verifica se possui
            apenas digitos. Caso possua caracteres alfa os remove.
        
        Args:
            label (str): texto informando o que deve ser inserido
        
        Returns:
            str: Número de matrícula. apenas dígitos
        """
        matricula: str = input(label)
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

    def recebe_cpf(label: str) -> str:
        """Recebe um CPF pelo teclado e verifica se possui 11 dígitos e se é
            válido.

        Args:
            label (str): texto informando o que deve ser inserido

        Returns:
            str: CPF válido ou None caso seja inválido
        """
             
        cpf: str = input(label)
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
        pis_pasep: str = input(label)
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
        entrada: str = input(label)
        nome: str = ''.join([i for i in entrada if not i.isdigit()])
        nome = nome.lower()
        if len(nome) > 1:
            return nome
        else:
            return None    

    def recebe_data(label: str) -> str:
        """Recebe uma data no formato ddMMaaa ou dd/MM/aaaa

        Args:
            label (str): texto informando o que deve ser inserido

        Returns:
            str: retorna uma data no formato dd/MM/aaaa
        """
        dia: int = None
        mes: int = None
        ano: int = None
        print(label)
        # tenta receber os dados no formato inteiro
        try:            
            dia: int = int(input("Dia: "))
            try:            
                mes: int = int(input("Mês: "))
                try:            
                    ano: int = int(input("Ano: "))
                except:
                    print("tipo ano inválido")
                    return None
            except:
                print("tipo mês inválido")
                return None
        except:
            print("tipo dia inválido")
            return None
        # verifica se o dia, mês e ano informádo são válidos
        data_valida: bool = False
        if ano in range(1900,2090):
            if mes in range(1,13):
                if dia in range(1,32):
                    # verifica de a data é válida
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
                    return None
            else:
                print("mês inválido")
                return None
        else:
            print("ano inválido")
            return None
        if data_valida:
            return "{:02d}/{:02d}/{:04d}".format(dia, mes, ano)
        else:
            return None