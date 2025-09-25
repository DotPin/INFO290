links de utilidad:  
https://github.com/moy/JFlex/tree/master/jflex/examples  
https://github.com/moy/JFlex/tree/master/jflex/examples/cup  
http://jflex.de/manual.html  


PARA COMPILAR CUP:  
java -cp java-cup-11b.jar:. java_cup.Main as.cup  
PARA COMPILAR JFLEX:  
jflex al.flex  
PARA COMPILAR MAIN:  
javac -cp java-cup-11b-runtime.jar:. *.java  
PARA EJECUTAR MAIN:  
java -cp java-cup-11b-runtime.jar:. Main  


EN ESE MISMO ORDEN: CUP -> JFLEX -> MAIN

Para usar Traductor Dirigido por Sintaxis, usar comando e instancias "Make" en el directorio tarea
