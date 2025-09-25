# Presentación de Información

**Traductor Dirigido por Sintaxis - Tipo Dibujo**

***

## Descripción de Datos

Dentro de éste directorio, se almacenan tanto de librerías JAVA como los archivos fuente que permiten la ejecución del software Traductor dirigido por Sintaxis tipo dibujo, cuales se detallarán a continuación.

- [al.flex](): Archivo para ser procesado en el Analizador Lexico, cual permite hacer la definición de tokens que se ingresarán en el software.

- [as.cup](): Archivo para ser procesado en el Analizador Sintáctico, cual permite hacer la definicion de instrucciones que serán procesadas para el Traductor dirigido por Sintaxis.

- java_cup-11b.jar: Analizador Sintáctico de Java cual procesa las instrucciones establecidas en algún archivo de tipo *.cup, para ser integradas en el proceso de Optimización de Código y por útlimo Generación de Código Objeto.

- java-cup-11b-runtime.jar: Generador de código objeto, cual permite entregar el/los archivo de ejecución de software.

- [Makefile](): Archivo de construcción automatizada, cual procesa todas las etapas de compilación de software.


## Compilación

Usando una ventana de terminal, en el mismo directorio donde se almacenan los archivos, debe ejecutarse se deben ejecutar los siguientes comandos

- Comando que permite el proceso de limpieza de archivos
 
```bash
$make clean
```

- Comando que permite el proceso de compilación y ejecución del software

```bash
$make
```

- Comando que permite el proceso de ejecución del software

```bash
$make exec
```