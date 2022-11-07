from view.tela_principal import TelaPrincipal
from model.colaborador import Colaborador


principal = TelaPrincipal()


if (__name__ == "__main__"):
    principal.clear()
    colaborador = Colaborador('007702', '04960780622', '1900833194-5',
                          'maxwell de oliveira chaves',
                          'instrutor de informática',
                          '24/07/2013')
    print(colaborador)
    # principal.exibe_menu()
    # principal.clear()
