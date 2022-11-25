from ponto.view.entrada import Entrada
from pytest import MonkeyPatch

class TestClass:
    def test_quando_matricula_for_0_deve_retornar_000000(self):
        # Given - contexto
        monkeypatch = MonkeyPatch()
        monkeypatch.setattr('builtins.input', lambda _: "0")
        esperado = "000000"
        # When - ação
        entrada_teste = Entrada()
        resultado = entrada_teste.recebe_matricula()
        # Then - desfecho
        assert resultado == esperado
        