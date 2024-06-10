%{
#include "parser.tab.h"

extern YYSTYPE yylval;

int yywrap(void);
%}

%%
"std"          return STD;
"print"        return PRINT;
"read"         return READ;
"if"           return IF;
"else"         return ELSE;
"repeat"       return REPEAT;
"or"           return OR;
"and"          return AND;
"=="           return EQ;
">"            return GT;
"<"            return LT;
"+"            return PLUS;
"-"            return MINUS;
"*"            return TIMES;
"/"            return DIVIDE;
"not"          return NOT;
"reading"      return READING;
"writing"      return WRITING;
"exercises"    return EXERCISES;
"lectures"     return LECTURES;
"research"     return RESEARCH;
[0-9]+         { yylval.number = atoi(yytext); return NUMBER; }
[a-zA-Z_][a-zA-Z0-9_]* { yylval.identifier = strdup(yytext); return IDENTIFIER; }
\n             return NEWLINE;
"("            return LPAREN;
")"            return RPAREN;
"="            return ASSIGN;
"{"            return LBRACE;
"}"            return RBRACE;
[ \t]          ;
.              { printf("Caracter desconhecido: %s\n", yytext); exit(1); }
%%

int yywrap(void) {
    return 1;
}
