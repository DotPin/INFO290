%{
    /*fichero LMA.y*/
    //#define YYSTYPE double
    #include <stdio.h>
    #include <stdlib.h>
    #include "arreglo.h"
    //int yylex();
%}


%union
{
int intval;
//int bf;
char *id;
}

%token <intval> ENTERO
%token <id> ID
%left PARTIR INICIAR METER SACAR MIRAR ID DATO FINALIZAR NL APAR CPAR COMA
%start LMA
%%
LMA :   PARTIR  {printf(">> El programa ha comenzado\n");}
        NL 
            inst 
        FINALIZAR {YYACCEPT;}
    ;
inst : inst NL inst
        | inst_iniciar
        | inst_meter
        | inst_sacar
        | inst_mirar
        | inst_dato
        ;
inst_iniciar : INICIAR APAR ID COMA ENTERO COMA ENTERO COMA ENTERO COMA ENTERO COMA ENTERO COMA ENTERO COMA ENTERO COMA ENTERO CPAR
            {iniciar($3,$5,$7,$9,$11,$13,$15,$17,$19);}
inst_meter : METER APAR ID  COMA ENTERO COMA ENTERO CPAR
            {meter($3,$5,$7);}
            ;
inst_sacar : SACAR APAR ID COMA ENTERO CPAR
            {sacar($3,$5);}
            ;
inst_mirar : MIRAR APAR ID CPAR
            {mirar($3);}
            ;
inst_dato  : DATO APAR ID COMA ENTERO CPAR
            {dato($3,$5);}
            ;

%%
int data_offset = 0;
int data_location() { return data_offset++; }
yyerror (s) /* Llamada por yyparse ante un error */
char *s;
{
printf ("%s SALIDA\n", s); /* Esta implementación por defecto nos valdrá/* Si no creamos esta función, habrá que enlazar con –ly en el */
}




int main()
{
    //ANTES DEL ANALISIS
    printf("\n****************************************************************\n");
    printf("\nAnalizador Lexico LMA\n");
    printf("\n****************************************************************\n");
    printf("\nIntegrantes:\t-Leandro Caloguerea\n");
    printf("\t\t-Diego Rojas\n");
    printf("\t\t-Felipe Soto\n");
    printf("\n****************************************************************\n");
    printf("\nTokens que acepta el analizador\n");
    printf("\nPalabras reservadas:\n");
    printf("\n-PARTIR\n");
    printf("-INICIAR(ID,d,d,d,d,d,d,d,d)\n");
    printf("-METER(ID,d,x)\n");
    printf("-SACAR(ID,x)\n");
    printf("-MIRAR(ID,x)\n");
    printf("-DATO(ID,x)\n");
    printf("-FINALIZAR\n");
    printf("\nIdentificadores(ID): L{letra}*{digito}+ \n"); 
    printf("\nConstantes enteras(d): digito+\n");
    printf("\ndigito: [0-9]\n");
    printf("\nposicion(x): [0-7]\n");
    printf("\nSimbolos: ( ) ,\n");
    printf("\n****************************************************************\n");
    printf("\nIniciando LMA, ingrese a continuacion PARTIR seguido de la tecla");
    printf("\n'enter' para comenzar a utilizar el programa: \n\n");
    //yylex();
    yyparse();
    //DESPUES DEL ANALISIS
    return 0;
}
