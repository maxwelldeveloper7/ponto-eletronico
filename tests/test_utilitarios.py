import pytest

from ponto.model.utilitarios import Entrada

from ponto.model.utilitarios import Validar


class TestRecebeData:
    def test_quando_a_data_for_vazia_deve_retornar_Exception(self):
        with pytest.raises(Exception):
            data = ''  # contexto
            resultado = Entrada.recebe_data(data)  # ação
            assert resultado  # desfecho

    def test_quando_a_data_for_24072013_deve_retornar24072013(self):
        data = '24/07/2013'  # contexto
        esperado = '24/07/2013'
        resultado = Entrada.recebe_data(data)  # ação
        assert esperado == resultado  # desfecho


class TestRecebNome:
    def test_quando_o_nome_for_fazio_deve_retornar_Exception(self):
        with pytest.raises(Exception):
            nome = ''  # contexto
            resultado = Entrada.recebe_nome(nome)  # ação
            assert resultado  # desfecho

    def test_quando_o_nome_for_1_deve_retornar_Exception(self):
        with pytest.raises(Exception):
            nome = '1'  # contexto
            resultado = Entrada.recebe_nome(nome)  # ação
            assert resultado  # desfecho

    def test_quando_o_nome_for_maxwell7_deve_retornar_maxwell(self):
        nome = 'maxwell7'
        esperado = 'maxwell'
        resultado = Entrada.recebe_nome(nome)
        assert resultado == esperado


class TestRecebePisPasep:
    def test_quando_o_pispasep_for_vazio_deve_retornar_Exception(self):
        with pytest.raises(Exception):
            pispasep = ''  # contexto
            resultado = Entrada.recebe_pis_pasep(pispasep)  # ação
            assert resultado  # desfecho

    def test_quando_o_pispasep_tem_mais_de_11_dig_deve_retornar_Except(self):
        with pytest.raises(Exception):
            pispasep = '123456789123'  # contexto
            resultado = Entrada.recebe_pis_pasep(pispasep)  # ação
            assert resultado  # desfecho

    def test_quando_o_pispasep_for_12345678912_deve_retornar_Exception(self):
        with pytest.raises(Exception):
            pispasep = '12345678912'  # contexto
            resultado = Entrada.recebe_pis_pasep(pispasep)  # ação
            assert resultado  # desfecho

    def test_quando_o_pispase_for_26621161644_deve_retornar_26621161644(self):
        pispasep = '26621161644'  # contexto
        esperado = '26621161644'
        resultado = Entrada.recebe_pis_pasep(pispasep)  # ação
        assert resultado == esperado  # desfecho


class TestRecebeCpf:
    def test_quando_o_cpf_for_vazio_deve_retornar_Exception(self):
        with pytest.raises(Exception):
            cpf = ''  # contexto
            resultado = Entrada.recebe_cpf(cpf)  # ação
            assert resultado  # desfecho

    def test_quando_o_cpf_tiver_mais_de_11_digitos_deve_retornar_Except(self):
        with pytest.raises(Exception):
            cpf = '123456789123'  # contexto
            resultado = Entrada.recebe_cpf(cpf)  # ação
            assert resultado  # desfecho

    def test_quando_o_cpf_for_12345678912_deve_retornar_Exception(self):
        with pytest.raises(Exception):
            cpf = '12345678912'  # contexto
            resultado = Entrada.recebe_cpf(cpf)  # ação
            assert resultado  # desfecho

    def test_quando_o_cpf_for_84981191030_deve_retornar_84981191030(self):
        cpf = '84981191030'  # contexto
        esperado = '84981191030'
        resultado = Entrada.recebe_cpf(cpf)  # ação
        assert resultado == esperado  # desfecho


class TestRecebeMatricula:
    def test_quando_a_matricula_for_0_deve_retornar_Exception(self):
        with pytest.raises(Exception):
            matricula = '0'  # contexto
            resultado = Entrada.recebe_matricula(matricula)  # ação
            assert resultado  # desfecho

    def test_quando_a_matricula_for_vazia_deve_retornar_Exception(self):
        with pytest.raises(Exception):
            matricula = ''  # contexto
            resultado = Entrada.recebe_matricula(matricula)  # ação
            assert resultado  # desfecho

    def test_quando_a_matricula_for_7702_deve_retornar_007702(self):
        matricula = '7702'  # contexto
        esperado = '007702'
        resultado = Entrada.recebe_matricula(matricula)  # ação
        assert resultado == esperado  # desfecho


class TestNumeroInteiro:
    def test_quando_o_texto_for_vazio_deve_retornar_Exception(self):
        with pytest.raises(Exception):
            texto = ''  # contexto
            resultado = Entrada.numero_inteiro(texto)  # ação
            assert resultado

    def test_quando_o_texto_for_a1b2c3d4f5g6_deve_retornar_123456(self):
        texto: str = 'a1b2c3d4f5g6'  # contexto
        esperado: int = 123456
        resultado = Entrada.numero_inteiro(texto)  # ação
        assert resultado == esperado  # desfecho


class TestAnoBissexto:
    def test_quando_o_ano_for_2023_deve_retornar_False(self):
        ano: int = 2023  # contexto
        esperado = False
        resultado = Validar.ano_bissexto(ano)  # ação
        assert resultado == esperado  # desfecho

    def test_quando_o_ano_for_2024_deve_retornar_True(self):
        ano: int = 2024  # contexto
        esperado = True
        resultado = Validar.ano_bissexto(ano)  # ação
        assert resultado == esperado  # desfecho


class TestData:
    def test_quando_a_data_for_00_00_0000_deve_retornar_False(self):
        data: str = '00/00/0000'  # contexto
        esperado = False
        resultado = Validar.data(data)  # ação
        assert resultado == esperado

    def test_quando_a_data_for_31_12_1899_deve_retornar_False(self):
        data: str = '31/12/1899'  # contexto
        esperado = False
        resultado = Validar.data(data)  # ação
        assert resultado == esperado

    def test_quando_a_data_for_01_01_2091_deve_retornar_False(self):
        data: str = '01/01/2091'  # contexto
        esperado = False
        resultado = Validar.data(data)  # ação
        assert resultado == esperado

    def test_quando_a_data_for_01_13_2090_deve_retornar_False(self):
        data: str = '01/13/2090'  # contexto
        esperado = False
        resultado = Validar.data(data)  # ação
        assert resultado == esperado

    def test_quando_a_data_for_31_4_2023_deve_retornar_False(self):
        data: str = '31/04/2023'  # contexto
        esperado = False
        resultado = Validar.data(data)  # ação
        assert resultado == esperado

    def test_quando_a_data_for_29_02_2023_deve_retornar_False(self):
        data: str = '29/02/2023'  # contexto
        esperado = False
        resultado = Validar.data(data)  # ação
        assert resultado == esperado

    def test_quando_a_data_for_29_02_2024_deve_retornar_True(self):
        data: str = '29/02/2024'  # contexto
        esperado = True
        resultado = Validar.data(data)  # ação
        assert resultado == esperado

    def test_quando_a_data_for_31_01_2023_deve_retornar_True(self):
        data: str = '31/01/2023'  # contexto
        esperado = True
        resultado = Validar.data(data)  # ação
        assert resultado == esperado

    def test_quando_a_data_for_30_04_2024_deve_retornar_True(self):
        data: str = '30/04/2024'  # contexto
        esperado = True
        resultado = Validar.data(data)  # ação
        assert resultado == esperado

    def test_quando_a_data_for_28_02_2023_deve_retornar_True(self):
        data: str = '28/02/2023'  # contexto
        esperado = True
        resultado = Validar.data(data)  # ação
        assert resultado == esperado
