from tokenizer import Tokenizer, Token
from Compilador.symbol_table import SymbolTable
from nodes import *

class Parser:
    """
    A classe Parser é responsável por analisar o código-fonte e construir uma árvore sintática
    que será utilizada para a execução do programa.
    """

    def __init__(self, source):
        """
        Inicializa o parser com o código-fonte e obtém o primeiro token.

        Parâmetros:
            source (str): O código-fonte a ser analisado.
        """
        self.tokenizer = Tokenizer(source)
        self.current_token = self.tokenizer.get_next_token()

    def eat(self, token_type):
        """
        Avança para o próximo token se o tipo do token atual for o esperado.

        Parâmetros:
            token_type (str): O tipo do token esperado.
        """
        if self.current_token.type == token_type:
            self.current_token = self.tokenizer.get_next_token()
        else:
            self.error(token_type)

    def error(self, token_type):
        """
        Lança uma exceção se o tipo do token atual não for o esperado.

        Parâmetros:
            token_type (str): O tipo do token esperado.
        """
        raise Exception(f'Esperado token {token_type}, mas recebeu {self.current_token.type}')

    def parse(self):
        """
        Analisa o código-fonte e constrói a árvore sintática.

        Retorna:
            Program: A árvore sintática do programa.
        """
        routines = []
        while self.current_token.type != 'EOF':
            routines.append(self.parse_study_routine())
        return Program(routines)

    def parse_study_routine(self):
        """
        Analisa uma rotina de estudo no código-fonte e retorna o nó correspondente.

        Retorna:
            Node: O nó correspondente à rotina de estudo.
        """
        if self.current_token.type == 'STD':
            return self.parse_var_decl()
        if self.current_token.type == 'IDENTIFIER':
            return self.parse_assignment()
        if self.current_token.type == 'PRINT':
            return self.parse_print()
        if self.current_token.type == 'REPEAT':
            return self.parse_repeat()
        if self.current_token.type == 'IF':
            return self.parse_if()
        if self.current_token.type in ('READING', 'WRITING', 'EXERCISES', 'LECTURES', 'RESEARCH'):
            return self.parse_study_instruction()
        self.error('Routine')

    def parse_var_decl(self):
        """
        Analisa uma declaração de variável no código-fonte e retorna o nó correspondente.

        Retorna:
            VarDecl: O nó correspondente à declaração de variável.
        """
        self.eat('STD')
        name = self.current_token.value
        self.eat('IDENTIFIER')
        self.eat('ASSIGN')
        value = self.parse_expression()
        return VarDecl(name, value)

    def parse_assignment(self):
        """
        Analisa uma atribuição de variável no código-fonte e retorna o nó correspondente.

        Retorna:
            Assignment: O nó correspondente à atribuição de variável.
        """
        name = self.current_token.value
        self.eat('IDENTIFIER')
        self.eat('ASSIGN')
        value = self.parse_expression()
        return Assignment(name, value)

    def parse_print(self):
        """
        Analisa uma instrução de impressão no código-fonte e retorna o nó correspondente.

        Retorna:
            Print: O nó correspondente à instrução de impressão.
        """
        self.eat('PRINT')
        self.eat('LPAREN')
        expression = self.parse_expression()
        self.eat('RPAREN')
        return Print(expression)

    def parse_repeat(self):
        """
        Analisa uma instrução de repetição no código-fonte e retorna o nó correspondente.

        Retorna:
            Repeat: O nó correspondente à instrução de repetição.
        """
        self.eat('REPEAT')
        self.eat('LPAREN')
        times = self.parse_expression()
        self.eat('RPAREN')
        self.eat('LBRACE')
        routines = []
        while self.current_token.type != 'RBRACE':
            routines.append(self.parse_study_routine())
        self.eat('RBRACE')
        return Repeat(times, routines)

    def parse_if(self):
        """
        Analisa uma instrução condicional no código-fonte e retorna o nó correspondente.

        Retorna:
            If: O nó correspondente à instrução condicional.
        """
        self.eat('IF')
        self.eat('LPAREN')
        condition = self.parse_expression()
        self.eat('RPAREN')
        self.eat('LBRACE')
        if_routines = []
        while self.current_token.type != 'RBRACE':
            if_routines.append(self.parse_study_routine())
        self.eat('RBRACE')
        else_routines = None
        if self.current_token.type == 'ELSE':
            self.eat('ELSE')
            self.eat('LBRACE')
            else_routines = []
            while self.current_token.type != 'RBRACE':
                else_routines.append(self.parse_study_routine())
            self.eat('RBRACE')
        return If(condition, if_routines, else_routines)

    def parse_expression(self):
        """
        Analisa uma expressão no código-fonte e retorna o nó correspondente.

        Retorna:
            Node: O nó correspondente à expressão.
        """
        node = self.parse_term()
        while self.current_token.type in ('PLUS', 'MINUS', 'GT', '=='):
            op = self.current_token.value
            self.eat(self.current_token.type)
            node = BinaryOp(node, op, self.parse_term())
        return node

    def parse_term(self):
        """
        Analisa um termo no código-fonte e retorna o nó correspondente.

        Retorna:
            Node: O nó correspondente ao termo.
        """
        node = self.parse_factor()
        while self.current_token.type in ('MULTIPLY', 'DIVIDE'):
            op = self.current_token.value
            self.eat(self.current_token.type)
            node = BinaryOp(node, op, self.parse_factor())
        return node

    def parse_factor(self):
        """
        Analisa um fator no código-fonte e retorna o nó correspondente.

        Retorna:
            Node: O nó correspondente ao fator.
        """
        token = self.current_token
        if token.type == 'NUMBER':
            self.eat('NUMBER')
            return Number(token.value)
        if token.type == 'IDENTIFIER':
            self.eat('IDENTIFIER')
            return Identifier(token.value)
        if token.type == 'STRING':
            self.eat('STRING')
            return String(token.value)
        if token.type == 'LPAREN':
            self.eat('LPAREN')
            node = self.parse_expression()
            self.eat('RPAREN')
            return node
        self.error('Factor')

    def parse_study_instruction(self):
        """
        Analisa uma instrução de estudo no código-fonte e retorna o nó correspondente.

        Retorna:
            StudyInstruction: O nó correspondente à instrução de estudo.
        """
        name = self.current_token.type
        if name == 'READING':
            self.eat('READING')
        elif name == 'WRITING':
            self.eat('WRITING')
        elif name == 'EXERCISES':
            self.eat('EXERCISES')
        elif name == 'LECTURES':
            self.eat('LECTURES')
        elif name == 'RESEARCH':
            self.eat('RESEARCH')
        else:
            self.eat('IDENTIFIER')
        self.eat('LPAREN')
        duration = self.parse_expression()
        self.eat('RPAREN')
        return StudyInstruction(name, duration)

    def parse_study_routine(self):
        """
        Analisa uma rotina de estudo no código-fonte e retorna o nó correspondente.

        Retorna:
            Node: O nó correspondente à rotina de estudo.
        """
        if self.current_token.type == 'STD':
            return self.parse_var_decl()
        if self.current_token.type == 'IDENTIFIER':
            return self.parse_assignment()
        if self.current_token.type == 'PRINT':
            return self.parse_print()
        if self.current_token.type == 'REPEAT':
            return self.parse_repeat()
        if self.current_token.type == 'IF':
            return self.parse_if()
        if self.current_token.type in ('READING', 'WRITING', 'EXERCISES', 'LECTURES', 'RESEARCH'):
            return self.parse_study_instruction()
        self.error('Routine')
