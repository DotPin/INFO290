import java_cup.runtime.*;
import java.util.*;
%%

%class Lexer
%caseless
%cup
%line
%column

%init{

this.i = 0;
this.tabla = new Hashtable<String, Integer>();

%init}

%{   
    private Integer i;
    private Hashtable<String, Integer> tabla;
    
    private Symbol symbol(int type) {
        return new Symbol(type, yyline, yycolumn);
    }
    
    private Symbol symbol(int type, Object value) {
        return new Symbol(type, yyline, yycolumn, value);
    }

    private int get() {
        int aux;
        if (this.tabla.containsKey(this.yytext())) {
            aux = this.tabla.get(this.yytext());
        } else {
            this.tabla.put(this.yytext(), ++this.i);
            aux = this.i;
        }
        return aux;
    }
%}


ID = [a-zA-Z][a-zA-Z0-9]*

DIGITO = [0-9]+

LineTerminator = \r|\n|\r\n

WhiteSpace     = {LineTerminator} | [ \t\f]

EDITAR = editar
TERMINO = termino
C = rojo|verde|amarillo|azul|blanco
POS = pos
IZQ = izq
DER = der
ARR = arr
ABA = aba
DAVALOR = davalor
COLOR = color
%%

<YYINITIAL> {
{EDITAR}                        { return symbol(sym.EDITAR); }
{POS}                           { return symbol(sym.POS); }
{IZQ}                           { return symbol(sym.IZQ); }
{DER}                           { return symbol(sym.DER); }
{ARR}                           { return symbol(sym.ARR); }
{ABA}                           { return symbol(sym.ABA); }
{DAVALOR}                       { return symbol(sym.DAVALOR); }
{COLOR}                         { return symbol(sym.COLOR); }
{TERMINO}                       { return symbol(sym.TERMINO); }
"("                             { return symbol(sym.LPAREN); }
")"                             { return symbol(sym.RPAREN); }
","                             { return symbol(sym.COMMA); }
"="                             { return symbol(sym.EQUAL); }

{C}                             { return symbol(sym.C, yytext()); }
{DIGITO}                        { return symbol(sym.DIGITO, Integer.valueOf(yytext())); }
{ID}                            { return symbol(sym.ID, this.get()); }

{WhiteSpace}                    {  /* IGNORE */ }
}

[^]                    { throw new Error("Illegal character <"+yytext()+">"); }
