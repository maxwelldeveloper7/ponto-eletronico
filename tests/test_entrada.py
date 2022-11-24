from ponto.view.entrada import Entrada

class TestClass:
    def test_quando_matricula_for_0_deve_retornar_000000(self):
        entrada = "0"# Given - contexto
        esperado = "000000"
        entrada_teste = Entrada()
        resultado = entrada_teste.recebe_matricula()# When - ação
        print(entrada)
        assert resultado == esperado# Then - desfecho