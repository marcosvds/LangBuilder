#LangBuilder

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
NOTA('C', 'seminima');
NOTA('E', 'seminima');
NOTA('G', 'seminima');
ACORDE('C,E,G', 'minima');
PAUSA('semi');
REPETIR('2') {
    NOTA('E', 'colcheia');
    NOTA('G', 'colcheia');
    NOTA('C', 'colcheia');
}
```
