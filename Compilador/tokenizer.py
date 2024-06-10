from token_base import Token

class Tokenizer:
    """
    A classe Tokenizer é responsável por transformar um código-fonte em uma sequência de tokens,
    que são unidades básicas de significado que o analisador sintático pode entender.
    """

    def __init__(self, source):
        """
        Inicializa o Tokenizer com o código-fonte e configura a posição inicial.

        Parâmetros:
            source (str): O código-fonte a ser tokenizado.
        """
        self.source = source
        self.position = 0
        self.current_char = source[0] if source else None

    def advance(self):
        """
        Avança para o próximo caractere no código-fonte e atualiza a posição atual.
        """
        self.position += 1
        self.current_char = self.source[self.position] if self.position < len(self.source) else None

    def get_next_token(self):
        """
        Obtém o próximo token no código-fonte, ignorando espaços em branco e identificando o tipo de token.

        Retorna:
            Token: O próximo token identificado no código-fonte.
        """
        self.skip_whitespace()

        if self.current_char is None:
            return Token('EOF', None)

        if self.current_char.isalpha():
            return self.get_identifier_or_keyword()

        if self.current_char.isdigit():
            return self.get_number()

        if self.current_char == '=':
            self.advance()
            return Token('ASSIGN', '=')

        if self.current_char == '(':
            self.advance()
            return Token('LPAREN', '(')

        if self.current_char == ')':
            self.advance()
            return Token('RPAREN', ')')

        if self.current_char == '{':
            self.advance()
            return Token('LBRACE', '{')

        if self.current_char == '}':
            self.advance()
            return Token('RBRACE', '}')

        if self.current_char == '>':
            self.advance()
            return Token('GT', '>')

        if self.current_char == '<':
            self.advance()
            return Token('LT', '<')

        if self.current_char == '+':
            self.advance()
            return Token('PLUS', '+')

        if self.current_char == '-':
            self.advance()
            return Token('MINUS', '-')

        if self.current_char == '*':
            self.advance()
            return Token('MULTIPLY', '*')

        if self.current_char == '/':
            self.advance()
            return Token('DIVIDE', '/')

        if self.current_char == '"':
            self.advance()
            return self.get_string()

        self.error()

    def get_identifier_or_keyword(self):
        """
        Identifica e retorna um identificador ou palavra-chave no código-fonte.

        Retorna:
            Token: O token correspondente ao identificador ou palavra-chave.
        """
        result = ''
        while self.current_char is not None and (
            self.current_char.isalnum() or self.current_char == '_'
        ):
            result += self.current_char
            self.advance()
        if result in (
            'print', 'while', 'if', 'else', 'then', 'do', 'end', 'not', 
            'read', 'or', 'and', 'local', 'repeat', 'std', 'reading', 
            'writing', 'exercises', 'lectures', 'research'
        ):
            return Token(result.upper(), result)
        return Token('IDENTIFIER', result)

    def get_number(self):
        """
        Identifica e retorna um número no código-fonte.

        Retorna:
            Token: O token correspondente ao número.
        """
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return Token('NUMBER', int(result))

    def get_string(self):
        """
        Identifica e retorna uma string no código-fonte.

        Retorna:
            Token: O token correspondente à string.
        """
        result = ''
        while self.current_char is not None and self.current_char != '"':
            result += self.current_char
            self.advance()
        self.advance()
        return Token('STRING', result)

    def skip_whitespace(self):
        """
        Ignora espaços em branco no código-fonte, avançando até encontrar um caractere não branco.
        """
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def error(self):
        """
        Lança uma exceção ao encontrar um caractere inesperado no código-fonte.
        """
        raise Exception(f'Caractere inesperado: {self.current_char}')
