from ponto.model.utilitarios import Entrada
from ponto.model.utilitarios import Validar
from pytest import MonkeyPatch, mark
import pytest

class TestNumeroInteiro:
    def test_quando_o_texto_for_vazio_deve_retornar_Exception(self):
        with pytest.raises(Exception):
            texto = '' # contexto
            resultado = Entrada.numero_inteiro('') # ação
            assert resultado

    def test_quando_o_texto_for_a1b2c3d4f5g6_deve_retornar_123456(self):
        texto: str = 'a1b2c3d4f5g6' #contexto
        esperado: int = 123456
        resultado = Entrada.numero_inteiro(texto) # ação
        assert resultado == esperado # desfecho

class TestAnoBissexto:
    def test_quando_o_ano_for_2023_deve_retornar_False(self):
        ano: int = 2023 # contexto
        esperado = False
        resultado = Validar.ano_bissexto(ano) # ação
        assert resultado == esperado # desfecho

    def test_quando_o_ano_for_2024_deve_retornar_True(self):
        ano: int = 2024 # contexto
        esperado = True
        resultado = Validar.ano_bissexto(ano) # ação
        assert resultado == esperado # desfecho

class TestData:
    def test_quando_a_data_for_00_00_0000_deve_retornar_False(self):
        data: str = '00/00/0000' # contexto
        esperado = False
        resultado = Validar.data(data) # ação
        assert resultado == esperado

    def test_quando_a_data_for_31_12_1899_deve_retornar_False(self):
        data: str = '31/12/1899' # contexto
        esperado = False
        resultado = Validar.data(data) # ação
        assert resultado == esperado

    def test_quando_a_data_for_01_01_2091_deve_retornar_False(self):
        data: str = '01/01/2091' # contexto
        esperado = False
        resultado = Validar.data(data) # ação
        assert resultado == esperado

    def test_quando_a_data_for_01_13_2090_deve_retornar_False(self):
        data: str = '01/13/2090' # contexto
        esperado = False
        resultado = Validar.data(data) # ação
        assert resultado == esperado

    def test_quando_a_data_for_31_4_2023_deve_retornar_False(self):
        data: str = '31/04/2023' # contexto
        esperado = False
        resultado = Validar.data(data) # ação
        assert resultado == esperado

    def test_quando_a_data_for_29_02_2023_deve_retornar_False(self):
        data: str = '29/02/2023' # contexto
        esperado = False
        resultado = Validar.data(data) # ação
        assert resultado == esperado

    def test_quando_a_data_for_29_02_2024_deve_retornar_True(self):
        data: str = '29/02/2024' # contexto
        esperado = True
        resultado = Validar.data(data) # ação
        assert resultado == esperado

    def test_quando_a_data_for_31_01_2023_deve_retornar_True(self):
        data: str = '31/01/2023' # contexto
        esperado = True
        resultado = Validar.data(data) # ação
        assert resultado == esperado

    def test_quando_a_data_for_30_04_2024_deve_retornar_True(self):
        data: str = '30/04/2024' # contexto
        esperado = True
        resultado = Validar.data(data) # ação
        assert resultado == esperado

    def test_quando_a_data_for_28_02_2023_deve_retornar_True(self):
        data: str = '28/02/2023' # contexto
        esperado = True
        resultado = Validar.data(data) # ação
        assert resultado == esperado

class TestRecebeMatricula:
    pass
    # def test_quando_matricula_for_vazia_deve_retornar_None(self):
    #     # Given - contexto
    #     monkeypatch = MonkeyPatch()
    #     monkeypatch.setattr('builtins.input', lambda _: "")
    #     esperado = None
    #     # When - ação
    #     entrada_teste = Entrada()
    #     resultado = entrada_teste.recebe_matricula()
    #     # Then - desfecho
    #     assert resultado == esperado

    # def test_quando_matricula_for_vazia_deve_retornar_exception(self):        
    #     with pytest.raises(Exception):
    #         monkeypatch = MonkeyPatch()
    #         monkeypatch.setattr('builtins.input', lambda _: "")# Given - contexto            
    #         # When - ação
    #         entrada_teste = Entrada()
    #         resultado = entrada_teste.recebe_matricula()
    #         # Then - desfecho
    #         assert resultado

    # @mark.matricula_0
    # def test_quando_matricula_for_0_deve_retornar_None(self):
    #     # Given - contexto
    #     monkeypatch = MonkeyPatch()
    #     monkeypatch.setattr('builtins.input', lambda _: "0")
    #     esperado = None
    #     # When - ação
    #     entrada_teste = Entrada()
    #     resultado = entrada_teste.recebe_matricula()
    #     # Then - desfecho
    #     assert resultado == esperado

    # def test_quando_matricula_for_9999999_deve_retornar_999999(self):
    #     # Given - contexto
    #     monkeypatch = MonkeyPatch()
    #     monkeypatch.setattr('builtins.input', lambda _: "9999999")
    #     esperado = "999999"
    #     # When - ação
    #     entrada_teste = Entrada()
    #     resultado = entrada_teste.recebe_matricula()
    #     # Then - desfecho
    #     assert resultado == esperado

    # def test_quando_matricula_for_1_deve_retornar_000001(self):
    #     # Given - contexto
    #     monkeypatch = MonkeyPatch()
    #     monkeypatch.setattr('builtins.input', lambda _: "1")
    #     esperado = "000001"
    #     # When - ação
    #     entrada_teste = Entrada()
    #     resultado = entrada_teste.recebe_matricula()
    #     # Then - desfecho
    #     assert resultado == esperado

    # @mark.skip
    # def test_quando_matricula_for_0000001_deve_retornar_000001(self):
    #     # Given - contexto
    #     monkeypatch = MonkeyPatch()
    #     monkeypatch.setattr('builtins.input', lambda _: "0000001")
    #     esperado = "000001"
    #     # When - ação
    #     entrada_teste = Entrada()
    #     resultado = entrada_teste.recebe_matricula()
    #     # Then - desfecho
    #     assert resultado == esperado

    # def test_quando_matricula_for_a000001_deve_retornar_000001(self):
    #     # Given - contexto
    #     monkeypatch = MonkeyPatch()
    #     monkeypatch.setattr('builtins.input', lambda _: "a000001")
    #     esperado = "000001"
    #     # When - ação
    #     entrada_teste = Entrada()
    #     resultado = entrada_teste.recebe_matricula()
    #     # Then - desfecho
    #     assert resultado == esperado

    # def test_quando_matricula_for_a1_deve_retornar_000001(self):
    #     # Given - contexto
    #     monkeypatch = MonkeyPatch()
    #     monkeypatch.setattr('builtins.input', lambda _: "a1")
    #     esperado = "000001"
    #     # When - ação
    #     entrada_teste = Entrada()
    #     resultado = entrada_teste.recebe_matricula()
    #     # Then - desfecho
    #     assert resultado == esperado

    # def test_quando_matricula_for_a999999_deve_retornar_999999(self):
    #     # Given - contexto
    #     monkeypatch = MonkeyPatch()
    #     monkeypatch.setattr('builtins.input', lambda _: "a999999")
    #     esperado = "999999"
    #     # When - ação
    #     entrada_teste = Entrada()
    #     resultado = entrada_teste.recebe_matricula()
    #     # Then - desfecho
    #     assert resultado == esperado

class TestRecebeCpf:
    ...