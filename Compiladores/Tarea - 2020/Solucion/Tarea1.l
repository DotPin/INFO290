/**/
%{
#include <stdio.h>
#include <string.h> /* para strdup*/
#include "y.tab.h"
%}

digito  [0-9]

id      "L"[a-z]*{digito}+

%%

"PARTIR"        {return(PARTIR);}
"INICIAR"       {return(INICIAR);}
"METER"         {return(METER);}
"SACAR"         {return(SACAR);}
"MIRAR"         {return(MIRAR);}
"DATO"          {return(DATO);}
"FINALIZAR"     {exit(0);
                    return(FINALIZAR);}

\n              {return(NL);}

"("             {return(APAR);}

","             {return(COMA);}

")"             {return(CPAR);}

{id}            {yylval.id = (char *) strdup(yytext);
                return(ID);}

{digito}+       {yylval.intval = atoi(yytext);
                return(ENTERO);} 

[a-zA-Z0-9]+       {printf("\nError: %s no pertenece al lenguaje\n", yytext);}

%%

int yywrap(){} 
