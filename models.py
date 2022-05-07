class Jogo:
    def __init__(self, nome, console, categoria, id=None):
        self.id = id
        self.nome = nome
        self.console = console
        self.categoria = categoria

class Usuario:
    def __init__(self, id, nome, senha):
        self.id = id
        self.nome = nome
        self.senha = senha