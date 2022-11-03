import os


os.system('clear')


def limpar_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


def escreve_titulo(titulo):
    limpar_console()
    largura_titulo = int(len(titulo)) + 4  # pega a largura do titulo
    pc = "\u001b[32m\U00002721\u001b[m"  # emoji de um pc
    print(pc * (largura_titulo))  # desenha borda superior
    print(pc, titulo, pc)  # desenha titulo e bordas laterais
    print(pc * (largura_titulo), "\n")  # desenha borda inferior
    # print("\u001b[32m\U00002721\u001b[m")