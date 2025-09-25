# Presentación de Información

**Solución**

***

## Descripción de Datos

Dentro de cada directorio, se almacenan tanto de librerías JAVA como los archivos fuente que permiten la ejecución del software Traductor dirigido por Sintaxis, cuales se detallarán a continuación.

- Traductor dirigido por Sintaxis, de tipo "calculadora" cual desarrolla las operaciones básicas de la aritmética, usando números enteros, por ello usa un archivo de tipo A.S.(file *.cup) cual procesa las producciones de tokens, mientras que el A.L. forma parte del "Main".java para manejo de entradas del lenguaje regular. Por ello, este prototipo permite ingreso de instrucciones por consola.  [Calc1](https://github.com/DotPin/INFO290/tree/master/Compiladores/Tarea%20-%202019/Solucion/calc1) Prototipo calculadora nº1

- Traductor dirigido por Sintaxis, de tipo "calculadora" similar al anterior, con la diferencia que el A.L. (file *.jflex/flex) cual procesa las entradas del lenguaje regular, se encuentra separado del programa principal que toma los tokens, y que por medio del A.S. (file *.cup) procesa las producciones generadas por cada instrucción al sistema ingresadas, para este caso a través de un archivo. [Calc2](https://github.com/DotPin/INFO290/tree/master/Compiladores/Tarea%20-%202019/Solucion/calc2) Prototipo calculadora nº2

- Traductor Dirigido por Sintaxis, de tipo "graficador" cual permite ingreso de instrucciones para dibujar líneas de colores en una ventana gráfica. Para mayor detalle revisar [Enunciado](https://github.com/DotPin/INFO290/blob/master/Compiladores/Tarea%20-%202019/Enunciado) [Tarea](https://github.com/DotPin/INFO290/tree/master/Compiladores/Tarea%20-%202019/Solucion/tarea) 



## [Requerimientos de sistema](https://github.com/DotPin/INFO290/tree/master/Compiladores/Tarea%20-%202019#requerimientos-de-sistema)

## Consideraciones

Los requerimientos del sistema, como los archivos java-cup-11b-runtime.jar y java-cup-11b.jar deben estar presentes y satisfechos para la correcta ejecución de los softwares.

### Referencias

- [Java CUP](https://www2.cs.tum.edu/projects/cup/)
- [Java JFlex/Flex](https://www.jflex.de/)
- [JFlex Github](https://github.com/jflex-de/jflex)
- [Java CUP GitHub](https://github.com/ultimate-pa/javacup)
  