class SymbolTable:
    """
    A classe SymbolTable representa uma tabela de símbolos que armazena variáveis e seus valores associados.
    Ela facilita a gestão de variáveis durante a análise sintática e execução de um programa.

    Atributos:
        table (dict): Um dicionário que mapeia nomes de variáveis (str) para seus valores.

    Métodos:
        get(self, name): Retorna o valor associado ao nome da variável.
        set(self, name, value): Define o valor de uma variável na tabela de símbolos.
        exists(self, name): Verifica se uma variável está definida na tabela de símbolos.
    """
    
    def __init__(self):
        # Inicializa a tabela de símbolos como um dicionário vazio
        self.table = {}

    def get(self, name):
        # Verifica se a variável existe na tabela
        if self.exists(name):
            return self.table[name]
        # Lança uma exceção se a variável não estiver definida
        raise KeyError(f'Variável "{name}" não encontrada na tabela de símbolos')

    def set(self, name, value):
        # Define o valor de uma variável na tabela de símbolos
        self.table[name] = value

    def exists(self, name):
        # Verifica se a variável está definida na tabela de símbolos
        return name in self.table
