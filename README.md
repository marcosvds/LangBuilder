# LangBuilder - MusicScript

### Objetivo da Linguagem MusicScript

**MusicScript** é uma linguagem de programação projetada para permitir aos usuários definir sequências de notas musicais, acordes e ritmos. Ela é especialmente útil para compositores iniciantes e programadores interessados em música, facilitando a experimentação musical e a composição automática.

### Funcionalidades Principais

- **Composição de Notas**: Especificar notas individuais com duração.
- **Definição de Acordes**: Compor acordes com várias notas.
- **Controle de Ritmo**: Estabelecer ritmos através de pausas e durações de notas.
- **Repetições e Loops**: Definir partes da música para repetir.

### Gramática EBNF da MusicScript

```
programa           ::= { instrucao } ;

instrucao          ::= nota | acorde | pausa | repeticao ;

nota               ::= NOTA '(' tom ',' duracao ')' ';' ;

acorde             ::= ACORDE '(' lista_tons ',' duracao ')' ';' ;

pausa              ::= PAUSA '(' duracao ')' ';' ;

repeticao          ::= REPETIR '(' numero ')' '{' programa '}' ;

lista_tons         ::= tom { ',' tom } ;

tom                ::= 'A' | 'B' | 'C' | 'D' | 'E' | 'F' | 'G' |
                      'A#' | 'Bb' | 'C#' | 'Db' | 'D#' | 'Eb' | 'F#' | 'Gb' | 'G#' | 'Ab' ;

duracao            ::= 'breve' | 'semi' | 'minima' | 'seminima' | 'colcheia' | 'semicolcheia' ;

numero             ::= [0-9]+ ;
```

### Exemplo de Uso da MusicScript

Suponha que queremos compor uma pequena peça que toque uma sequência de notas seguida de um acorde:

```
NOTA("C", "seminima");
NOTA("E", "seminima");
NOTA("G", "seminima");
ACORDE("C,E,G", "minima");
PAUSA("semi");
REPETIR(2) {
    NOTA("E", "colcheia");
    NOTA("G", "colcheia");
    NOTA("C", "colcheia");
}
```

### Estrutura do Projeto

A estrutura do projeto deve conter os seguintes arquivos:

- `lexer.l`: Define as regras de análise léxica usando Flex.
- `parser.y`: Define as regras de análise sintática usando Bison.
- `Makefile` (opcional): Para facilitar a compilação usando `make`.

### Instruções de Compilação e Execução

1. **Instalar as dependências:**
   - Flex
   - Bison
   - GCC (ou outro compilador C/C++)

2. **Compilar o analisador léxico e sintático:**
   ```sh
   flex lexer.l
   bison -d -v parser.y
   gcc lex.yy.c parser.tab.c -o mycompiler
   ```

3. **Executar o compilador com um arquivo de entrada:**
   ```sh
   ./mycompiler < teste1.txt
   ```

### Arquivos de Teste

Exemplo de arquivos de teste para verificar o funcionamento do compilador:

**Arquivo `teste1.txt`**
```
NOTA("C", "seminima");
NOTA("E", "seminima");
NOTA("G", "seminima");
ACORDE("C,E,G", "minima");
PAUSA("semi");
REPETIR(2) {
    NOTA("E", "colcheia");
    NOTA("G", "colcheia");
    NOTA("C", "colcheia");
}
```

**Arquivo `teste2.txt`**
```
ACORDE("A,C,E", "minima");
PAUSA("breve");
NOTA("F#", "colcheia");
NOTA("G#", "colcheia");
```

**Arquivo `teste3.txt`**
```
REPETIR(3) {
    NOTA("D", "seminima");
    ACORDE("D,F#,A", "minima");
}
```

**Arquivo `teste4.txt`**
```
NOTA("G", "semicolcheia");
PAUSA("minima");
ACORDE("B,D#,F#", "colcheia");
```

**Arquivo `teste5.txt`**
```
NOTA("C#", "semi");
ACORDE("C#,E,G#", "seminima");
PAUSA("colcheia");
REPETIR(4) {
    NOTA("F", "semicolcheia");
    PAUSA("semi");
}
```