/**/

letra   [a-zA-Z]
digito  [0-9]
%%

empiece|listo|ver|dato|asigna|inserta|elimina     {printf("\n Palabra Reservada: %s",yytext);}

"("|")"|","|"="     {printf("\nIngresa Símbolo %s", yytext);}

{digito}+     {printf("\nIngresa numero entero %d", atoi(yytext));}

[Ll]{digito}+    {printf("\nIngresa nombre %s", yytext);}

{letra}+({letra}|{digito})*        {printf("\nIdentificador %s", yytext);}

%%

int yywrap(){} 
int main(){
printf("Comienza Analizador Léxico \n");
printf("Integrantes:\n·Diego Rojas\n·Leandro Caloguerea\n·Camilo Muñoz\n");
printf("*********************\n\n\n");

yylex();

return 0;

}
