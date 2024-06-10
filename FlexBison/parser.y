%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void yyerror(const char *s);
int yylex(void);

typedef struct {
    char *identifier;
    int number;
} YYSTYPE;

#define YYSTYPE_IS_DECLARED 1
%}

%union {
    char *identifier;
    int number;
}

%token <number> NUMBER
%token <identifier> IDENTIFIER

%token STD PRINT READ IF ELSE REPEAT OR AND EQ GT LT PLUS MINUS TIMES DIVIDE NOT
%token READING WRITING EXERCISES LECTURES RESEARCH
%token NEWLINE ASSIGN LPAREN RPAREN LBRACE RBRACE

%%

program:
    routines
    ;

routines:
    routines routine
    | /* empty */
    ;

routine:
    assignment NEWLINE
    | print NEWLINE
    | repeat NEWLINE
    | if NEWLINE
    | variable_declaration NEWLINE
    | instruction NEWLINE
    ;

variable_declaration:
    STD IDENTIFIER
    | STD IDENTIFIER ASSIGN expression
    ;

assignment:
    IDENTIFIER ASSIGN expression
    ;

print:
    PRINT LPAREN expression RPAREN
    ;

read:
    READ LPAREN RPAREN
    ;

instruction:
    activity_name LPAREN NUMBER RPAREN
    ;

if:
    IF LPAREN expression RPAREN NEWLINE LBRACE routines RBRACE
    | IF LPAREN expression RPAREN NEWLINE LBRACE routines RBRACE ELSE NEWLINE LBRACE routines RBRACE
    ;

repeat:
    REPEAT LPAREN NUMBER RPAREN NEWLINE LBRACE routines RBRACE
    ;

expression:
    term
    | expression PLUS term
    | expression MINUS term
    ;

term:
    factor
    | term TIMES factor
    | term DIVIDE factor
    ;

factor:
    PLUS factor
    | MINUS factor
    | NOT factor
    | NUMBER
    | IDENTIFIER
    | LPAREN expression RPAREN
    | read
    ;

activity_name:
    READING
    | WRITING
    | EXERCISES
    | LECTURES
    | RESEARCH
    ;

%%

void yyerror(const char *s) {
    fprintf(stderr, "Erro: %s\n", s);
}

int main() {
    return yyparse();
}
