from ponto.model.utilitarios import Entrada
from ponto.model.utilitarios import Validar
from pytest import MonkeyPatch, mark
import pytest

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