class Token:
    """
    Classe Token representa uma unidade básica de significado dentro de um código-fonte analisado,
    usada para facilitar a análise sintática e semântica posterior pelo compilador.

    Atributos:
        type (str): Tipo do token, que indica a categoria sintática à qual o token pertence.
                    Exemplos comuns incluem 'INT' para números inteiros, 'PLUS' para o operador de adição '+',
                    'MINUS' para o operador de subtração '-', e 'EOF' para indicar o fim da entrada.
        value: O valor literal do token. Para tokens de tipo 'INT', este é um valor numérico.
               Para tokens 'PLUS' ou 'MINUS', é o próprio caractere operador ('+' ou '-').
               Para 'EOF', geralmente é uma string vazia, indicando o fim da entrada.

    Métodos:
        __init__(self, type, value): Construtor da classe. Inicializa um novo Token com um tipo e valor especificados.
        __repr__(self): Fornece uma representação em string do Token, útil para depuração e logging.
    """

    def __init__(self, type: str, value: any) -> None:
        """
        Inicializa um novo Token.

        Parâmetros:
            type (str): Tipo do token.
            value: Valor do token.
        """
        self.type = type
        self.value = value

    def __repr__(self) -> str:
        """
        Retorna uma representação em string do Token, facilitando a identificação do seu valor e tipo.

        Retorna:
            str: Representação do Token no formato '(valor, tipo)'.
        """
        token_repr = f"({self.value}, {self.type})"
        return token_repr
