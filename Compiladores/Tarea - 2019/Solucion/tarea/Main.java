import java.util.*;
import java.io.*;

public class Main{

    public static void main(String[] args) {
        try {

        parser p = new parser(new Lexer(System.console().reader()));
        Object result = p.parse().value;      
        } catch (Exception e) {
            /* do cleanup here -- possibly rethrow e */
            e.printStackTrace();
        }
    
        }
}