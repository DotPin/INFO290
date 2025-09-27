# Presentación de Información

**Traductor Dirigido por Sintaxis - LMA**

***

## Descripción de Datos

Dentro de cada directorio, se almacenan los archivos fuente que permiten la ejecución del Traductor Dirigido por Sintaxis tipo LMA, cuales se detallarán a continuación.

- [Tarea1.l](https://github.com/DotPin/INFO290/blob/master/Compiladores/Tarea%20-%202020/Solucion/Tarea1.l): Archivo cual almacena los diferentes lenguajes regulares cuales generan tokens ingresados por el usuario, permitiendo éstos ser procesados por Analizador Léxico.

- [LMA.y](https://github.com/DotPin/INFO290/blob/master/Compiladores/Tarea%20-%202020/Solucion/LMA.y): Archivo cual almacena el conjunto de producciones gramaticales que generan las instrucciones de los requerimientos solicitados, permitiendo que Analizador Sintáctico procese lo almacenado.

- [arreglo.h](https://github.com/DotPin/INFO290/blob/master/Compiladores/Tarea%20-%202020/Solucion/arreglo.h): Conjunto de procedimientos del programa principal que combina e invoca los archivos generados por el Analizador Léxico y Sintáctico, para la generación del código objeto cual ejecuta el software.

- [Makefile](https://github.com/DotPin/INFO290/blob/master/Compiladores/Tarea%20-%202020/Solucion/Makefile): Conjunto de procedimientos que automatizan la labor de compilación, ejecución y limpieza del software.


## Consideraciones

Los requerimientos del sistema establecidos anteriormente permitirán, la compilación del Traductor Dirigido por Sintaxis - LMA mediante GCC, generando el código objeto cual ejecuta el programa.

# Compilar archivo desde linux

- Ejecutar Analizador Léxico

```bash
$flex Tarea1.l
```

- Ejecutar Analizador Sintáctico

```bash
$bison -yd LMA.y
```

- Compilación para producción de código objeto

```bash
$gcc y.tab.c lex.yy.c -lfl -o salida
```

- Ejecución del programa

```bash
$./salida
```

## Compilación rápida

- Limpieza de directorio

```bash
$make clean
```

- Compilación + ejecución

```bash
$make
```

- Ejecución, si se encuentra todo compilado

```bash
$make run
```


