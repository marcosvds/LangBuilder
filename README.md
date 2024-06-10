# LangBuilder

LangBuilder é uma linguagem de programação personalizada desenvolvida para facilitar a criação de rotinas de estudo. A principal motivação da LangBuilder é permitir que os usuários definam e organizem suas atividades de forma estruturada e intuitiva. A linguagem possui todas as estruturas básicas de uma linguagem de programação: variáveis, condicionais e loops.

## EBNF

<a name="EBNF"></a>

```ebnf
PROGRAM = { ROUTINE } ;
ROUTINE = ( ASSIGNMENT | PRINT | REPEAT | IF | VARIABLE_DECLARATION | INSTRUCTION ), "\n" ;
VARIABLE_DECLARATION = "std", IDENTIFIER, [ "=", EXPRESSION ] ;
ASSIGNMENT = IDENTIFIER, "=", EXPRESSION ;
PRINT = "print", "(", EXPRESSION, ")" ;
READ = "read", "(", ")" ;
INSTRUCTION = ACTIVITY_NAME, "(", NUMBER, ")" ;
IF = "if", "(", EXPRESSION, ")", "\n", "{", { ROUTINE }, "}", [ "else", "\n", "{", { ROUTINE }, "}" ] ;
REPEAT = "repeat", "(", NUMBER, ")", "\n", "{", { ROUTINE }, "}" ;
BOOLEAN_EXPRESSION = BOOLEAN_TERM, { "or", BOOLEAN_TERM } ;
BOOLEAN_TERM = REL_EXPRESSION, { "and", REL_EXPRESSION } ;
REL_EXPRESSION = EXPRESSION, { ("==" | ">" | "<"), EXPRESSION } ;
EXPRESSION = TERM, { ("+" | "-"), TERM } ;
TERM = FACTOR, { ("*" | "/"), FACTOR } ;
FACTOR = ( ("+" | "-" | "not"), FACTOR ) | NUMBER | IDENTIFIER | "(", EXPRESSION, ")" | READ ;
ACTIVITY_NAME = "reading" | "writing" | "exercises" | "lectures" | "research" ;
IDENTIFIER = LETTER, { LETTER | DIGIT | "_" } ;
NUMBER = DIGIT, { DIGIT } ;
LETTER = "a" | "..." | "z" | "A" | "..." | "Z" ;
DIGIT = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;
```

## Estrutura do Projeto

A estrutura do projeto LangBuilder é organizada em três principais diretórios: `Compilador`, `FlexBison` e `Testes`. Cada diretório contém arquivos específicos para diferentes partes do projeto, como a implementação do compilador, as definições léxicas e sintáticas, e os arquivos de teste.

### Diretório `Compilador`

Este diretório contém os arquivos Python responsáveis pela implementação do compilador da LangBuilder.

```
Compilador/
├── main.py
├── nodes.py
├── parser_base.py
├── preprocessor.py
├── symbol_table.py
├── tokenizer.py
└── token_base.py
```

- `main.py`: Arquivo principal que executa o compilador.
- `nodes.py`: Define as classes dos nós da árvore sintática.
- `parser_base.py`: Implementa o analisador sintático.
- `preprocessor.py`: Contém a classe que realiza o pré-processamento do código.
- `symbol_table.py`: Implementa a tabela de símbolos.
- `tokenizer.py`: Implementa o analisador léxico.
- `token_base.py`: Define a classe Token.

### Diretório `FlexBison`

Este diretório contém os arquivos necessários para a análise léxica e sintática utilizando Flex e Bison.

```
FlexBison/
├── lex.yy.c
├── lexer.l
├── mycompiler.exe
├── parser.tab.c
├── parser.tab.h
└── parser.y
```

- `lex.yy.c`: Arquivo gerado pelo Flex a partir de `lexer.l`.
- `lexer.l`: Definição do analisador léxico usando Flex.
- `mycompiler.exe`: Executável do compilador gerado pela compilação dos arquivos Flex e Bison.
- `parser.tab.c`: Arquivo gerado pelo Bison a partir de `parser.y`.
- `parser.tab.h`: Cabeçalho gerado pelo Bison a partir de `parser.y`.
- `parser.y`: Definição do analisador sintático usando Bison.

### Diretório `Testes`

Este diretório contém arquivos de teste escritos na linguagem LangBuilder, usados para validar o funcionamento do compilador.

```
Testes/
├── teste1.std
├── teste2.std
└── teste3.std
```

- `teste1.std`: Arquivo de teste com exemplos de código na linguagem LangBuilder.
- `teste2.std`: Arquivo de teste com exemplos de código na linguagem LangBuilder.
- `teste3.std`: Arquivo de teste com exemplos de código na linguagem LangBuilder.

## Como Compilar e Executar

### Flex e Bison

1. **Instalar Flex e Bison**

   Certifique-se de que você tenha o Flex e o Bison instalados no seu sistema. No Ubuntu, você pode instalá-los com:

   ```bash
   sudo apt-get install flex bison
   ```

2. **Compilar o Lexer e o Parser**

   Navegue até o diretório `FlexBison` e execute os seguintes comandos para compilar o lexer e o parser:

   ```bash
   cd FlexBison
   flex lexer.l
   bison -d parser.y
   gcc parser.tab.c lex.yy.c -o mycompiler
   ```

3. **Executar o Compilador**

   Utilize o arquivo `teste1.std` para testar o compilador. Certifique-se de estar no diretório `FlexBison`:

   ```bash
   ./mycompiler < ../Testes/teste1.std
   ```

### Python

1. **Executar o Compilador em Python**

   Navegue até o diretório `Compilador` e execute o compilador usando o script `main.py`:

   ```bash
   cd ../Compilador
   python main.py ../Testes/teste1.std
   ```

## Exemplo de Código

### Arquivo `teste1.std`

```plaintext
// declaração de variáveis
std num_sessao = 2;
std paginas_por_sessao = 10;

// loop de repetição
repeat(num_sessao) {
    reading(paginas_por_sessao);
    writing(20);
}

// condicional
if (paginas_por_sessao > 5) {
    research(15);
} else {
    exercises(30);
}

// impressão de mensagem
print("estudo concluído!");
```

### Resultado Esperado

Ao executar o compilador com o arquivo `teste1.std`, o resultado esperado é:

```plaintext
Iniciando estudo.
Passe 10 minutos em READING
Passe 20 minutos em WRITING
Passe 10 minutos em READING
Passe 20 minutos em WRITING
Passe 15 minutos em RESEARCH
estudo concluído!
Estudo finalizado.
```