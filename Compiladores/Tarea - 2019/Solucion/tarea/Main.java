import java.util.*;
import java.io.*;

public class Main{

    public static void main(String[] args) {
        try {

        parser p = new parser(new Lexer(System.console().reader()));
        System.out.println("\n\nBienvenido/a a la consola Traductor dirigido por Sintaxis, ingrese \"editar\" para comenzar, y luego \"termino\" para cerrar el programa:");
        Object result = p.parse().value;      
        } catch (Exception e) {
            /* do cleanup here -- possibly rethrow e */
            e.printStackTrace();
        }
    
        }
}