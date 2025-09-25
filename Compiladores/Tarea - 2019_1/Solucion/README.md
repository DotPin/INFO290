# Presentación de Información

**Analizador Léxico**

***

## Descripción de Datos

Dentro de cada directorio, se almacenan los archivos fuente que permiten la ejecución del Analizador Lexico, cuales se detallarán a continuación.

- [Tarea1.lex]https://github.com/DotPin/INFO290/blob/master/Compiladores/Tarea%20-%202019_1/Solucion/Tarea1.lex): Archivo de tipo léxico cual almacena las restricciones del uso de tokens, usando Lenguaje Regular.


## Consideraciones

Los requerimientos del sistema establecidos anteriormente permitirán, la ejecución del Analizador Léxico con su posterior compilación mediante GCC, generando el código objeto cual ejecuta el programa.

# Compilar archivo desde linux

- Ejecutar comando

´´´bash
$flex Tarea1.flex
´´´

- Compilar archivo obtenido lex.yy.c

´´´bash
$gcc lex.yy.c -o <archivo>
´´´

- Ejecutar código objeto generado 

´´´bash
$./<archivo>
´´´

## Compilación rápida

- Limpieza de directorio

´´´bash
$make clean
´´´

- Compilación + ejecución

´´´bash
$make
´´´

- Ejecución, si se encuentra todo compilado

´´´bash
$make run
´´´


