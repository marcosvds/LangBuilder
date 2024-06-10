from tokenizer import Tokenizer, Token
from Compilador.symbol_table import *

# Classe base para todos os nós na árvore sintática
class Node:
    def evaluate(self, st):
        pass

# Classe para o nó do programa, que contém uma lista de rotinas
class Program(Node):
    def __init__(self, routines):
        self.routines = routines

    def evaluate(self, st):
        # Avalia cada rotina no contexto fornecido
        for routine in self.routines:
            routine.evaluate(st)

# Classe para a declaração de variáveis
class VarDecl(Node):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def evaluate(self, st):
        # Define o valor da variável na tabela de símbolos
        st.set(self.name, self.value.evaluate(st))

# Classe para a atribuição de valores a variáveis
class Assignment(Node):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def evaluate(self, st):
        # Atualiza o valor da variável na tabela de símbolos
        st.set(self.name, self.value.evaluate(st))

# Classe para a instrução de impressão
class Print(Node):
    def __init__(self, expression):
        self.expression = expression

    def evaluate(self, st):
        # Avalia a expressão e imprime o resultado
        print(self.expression.evaluate(st))

# Classe para a instrução de repetição
class Repeat(Node):
    def __init__(self, times, routines):
        self.times = times
        self.routines = routines

    def evaluate(self, st):
        # Avalia a expressão que determina o número de repetições
        for _ in range(self.times.evaluate(st)):
            for routine in self.routines:
                routine.evaluate(st)

# Classe para a instrução condicional
class If(Node):
    def __init__(self, condition, if_routines, else_routines=None):
        self.condition = condition
        self.if_routines = if_routines
        self.else_routines = else_routines

    def evaluate(self, st):
        # Avalia a condição e executa as rotinas apropriadas
        if self.condition.evaluate(st):
            for routine in self.if_routines:
                routine.evaluate(st)
        elif self.else_routines:
            for routine in self.else_routines:
                routine.evaluate(st)

# Classe para a declaração de funções
class FunctionDecl(Node):
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body

    def evaluate(self, st):
        # Armazena a função na tabela de símbolos
        st.set(self.name, self)

# Classe para a chamada de funções
class FunctionCall(Node):
    def __init__(self, name, args):
        self.name = name
        self.args = args

    def evaluate(self, st):
        # Obtém a função da tabela de símbolos e avalia com os argumentos fornecidos
        function = st.get(self.name)
        local_st = SymbolTable()
        for param, arg in zip(function.params, self.args):
            local_st.set(param, arg.evaluate(st))
        function.body.evaluate(local_st)

# Classe para números
class Number(Node):
    def __init__(self, value):
        self.value = value

    def evaluate(self, st):
        return self.value

# Classe para identificadores (variáveis)
class Identifier(Node):
    def __init__(self, name):
        self.name = name

    def evaluate(self, st):
        return st.get(self.name)

# Classe para operações binárias (adição, subtração, etc.)
class BinaryOp(Node):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def evaluate(self, st):
        if self.op == '+':
            return self.left.evaluate(st) + self.right.evaluate(st)
        if self.op == '-':
            return self.left.evaluate(st) - self.right.evaluate(st)
        if self.op == '*':
            return self.left.evaluate(st) * self.right.evaluate(st)
        if self.op == '/':
            return self.left.evaluate(st) / self.right.evaluate(st)
        if self.op == '>':
            return self.left.evaluate(st) > self.right.evaluate(st)
        if self.op == '==':
            return self.left.evaluate(st) == self.right.evaluate(st)
        if self.op == '<':
            return self.left.evaluate(st) < self.right.evaluate(st)
        if self.op == '<=':
            return self.left.evaluate(st) <= self.right.evaluate(st)
        if self.op == '>=':
            return self.left.evaluate(st) >= self.right.evaluate(st)
        if self.op == '!=':
            return self.left.evaluate(st) != self.right.evaluate(st)
        raise Exception(f'Operador binário desconhecido: {self.op}')

# Classe para strings
class String(Node):
    def __init__(self, value):
        self.value = value

    def evaluate(self, st):
        return self.value

# Classe para instruções de estudo (personalizadas para a linguagem)
class StudyInstruction(Node):
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def evaluate(self, st):
        print(f"Passe {self.duration.evaluate(st)} minutos em {self.name}")
