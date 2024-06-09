%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h> // Inclua para strdup
void yyerror(const char *s);
extern int yylex();
#define YYDEBUG 1
%}

%union {
    char *str;
    int num;
}

%token <str> NOTA ACORDE PAUSA REPETIR
%token <str> STRING NOTENAME BREVE SEMI MINIMA SEMINIMA COLCHEIA SEMICOLCHEIA
%token <num> NUMERO

%type <str> tom duracao lista_tons

%%

programa: /* vazio */
        | programa instrucao { printf("Instrucao reconhecida\n"); } ;

instrucao: nota { printf("Nota reconhecida\n"); }
         | acorde { printf("Acorde reconhecido\n"); }
         | pausa { printf("Pausa reconhecida\n"); }
         | repeticao { printf("Repeticao reconhecida\n"); } ;

nota: NOTA '(' tom ',' duracao ')' ';' { printf("Nota: %s %s\n", $3, $5); free($3); free($5); } ;

acorde: ACORDE '(' lista_tons ',' duracao ')' ';' { printf("Acorde: %s %s\n", $3, $5); free($3); free($5); } ;

pausa: PAUSA '(' duracao ')' ';' { printf("Pausa: %s\n", $3); free($3); } ;

repeticao: REPETIR '(' NUMERO ')' '{' programa '}' { printf("Repetir %d vezes\n", $3); } ;

lista_tons: tom
          | lista_tons ',' tom { 
                char *temp = malloc(strlen($1) + strlen($3) + 2);
                sprintf(temp, "%s,%s", $1, $3);
                $$ = temp;
                free($1);
                free($3);
            } ;

tom: STRING ;

duracao: STRING ;

%%

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}

int main(void) {
    yydebug = 1;
    return yyparse();
}
