%{
#include "parser.tab.h"
%}

%%

"NOTA"         { printf("TOKEN: NOTA\n"); return NOTA; }
"ACORDE"       { printf("TOKEN: ACORDE\n"); return ACORDE; }
"PAUSA"        { printf("TOKEN: PAUSA\n"); return PAUSA; }
"REPETIR"      { printf("TOKEN: REPETIR\n"); return REPETIR; }
[A-G]          { printf("TOKEN: NOTENAME %s\n", yytext); yylval.str = strdup(yytext); return NOTENAME; }
"A#"           { printf("TOKEN: NOTENAME %s\n", yytext); yylval.str = strdup(yytext); return NOTENAME; }
"Bb"           { printf("TOKEN: NOTENAME %s\n", yytext); yylval.str = strdup(yytext); return NOTENAME; }
"C#"           { printf("TOKEN: NOTENAME %s\n", yytext); yylval.str = strdup(yytext); return NOTENAME; }
"Db"           { printf("TOKEN: NOTENAME %s\n", yytext); yylval.str = strdup(yytext); return NOTENAME; }
"D#"           { printf("TOKEN: NOTENAME %s\n", yytext); yylval.str = strdup(yytext); return NOTENAME; }
"Eb"           { printf("TOKEN: NOTENAME %s\n", yytext); yylval.str = strdup(yytext); return NOTENAME; }
"F#"           { printf("TOKEN: NOTENAME %s\n", yytext); yylval.str = strdup(yytext); return NOTENAME; }
"Gb"           { printf("TOKEN: NOTENAME %s\n", yytext); yylval.str = strdup(yytext); return NOTENAME; }
"G#"           { printf("TOKEN: NOTENAME %s\n", yytext); yylval.str = strdup(yytext); return NOTENAME; }
"Ab"           { printf("TOKEN: NOTENAME %s\n", yytext); yylval.str = strdup(yytext); return NOTENAME; }
"breve"        { printf("TOKEN: BREVE\n"); yylval.str = strdup(yytext); return BREVE; }
"semi"         { printf("TOKEN: SEMI\n"); yylval.str = strdup(yytext); return SEMI; }
"minima"       { printf("TOKEN: MINIMA\n"); yylval.str = strdup(yytext); return MINIMA; }
"seminima"     { printf("TOKEN: SEMINIMA\n"); yylval.str = strdup(yytext); return SEMINIMA; }
"colcheia"     { printf("TOKEN: COLCHEIA\n"); yylval.str = strdup(yytext); return COLCHEIA; }
"semicolcheia" { printf("TOKEN: SEMICOLCHEIA\n"); yylval.str = strdup(yytext); return SEMICOLCHEIA; }
[0-9]+         { printf("TOKEN: NUMERO %s\n", yytext); yylval.num = atoi(yytext); return NUMERO; }
"("            { printf("TOKEN: (\n"); return '('; }
")"            { printf("TOKEN: )\n"); return ')'; }
","            { printf("TOKEN: ,\n"); return ','; }
"{"            { printf("TOKEN: {\n"); return '{'; }
"}"            { printf("TOKEN: }\n"); return '}'; }
";"            { printf("TOKEN: ;\n"); return ';'; }
\"([A-G#b,]+|[a-z]+)\" { printf("TOKEN: STRING %s\n", yytext); yylval.str = strdup(yytext+1); yylval.str[strlen(yylval.str)-1] = '\0'; return STRING; }
[ \t\n]        ;  // Ignorar espaços em branco
.              { printf("TOKEN: %c\n", yytext[0]); return yytext[0]; }

%%

int yywrap() {
    return 1;
}
