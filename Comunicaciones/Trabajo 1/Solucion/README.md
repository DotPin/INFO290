# Presentación de Información

**Compresor de Data**

***

## Descripción de Datos

Dentro de cada directorio, se almacenan tanto de librerías Python como los archivos fuente que permiten la ejecución del software Compresor, cuales se detallarán a continuación.

- [trans.py](https://github.com/DotPin/INFO290/blob/master/Comunicaciones/Trabajo%201/Solucion/Decodificador/trans.py): Archivo principal cual permite ejecutar el programa decodificador de datos junto con sus librerías correspondientes.

- [calculo.py](https://github.com/DotPin/INFO290/blob/master/Comunicaciones/Trabajo%201/Solucion/Decodificador/calculo.py) Archivo que calcula la parametrización de colores, medida de tiempo en procesamiento para su posterior calculo de error de compresión.

- [dct2.py](https://github.com/DotPin/INFO290/blob/master/Comunicaciones/Trabajo%201/Solucion/Decodificador/dct2.py) Calculo de la transformada discreta de cosenos, cual realiza la compresión de la data.

- [idct2.py](https://github.com/DotPin/INFO290/blob/master/Comunicaciones/Trabajo%201/Solucion/Decodificador/idct2.py) Código que permite realizar la transformada discreta de coseno decodificando la data ingresada, descomprimiendo sus parámetros.

- [codigo.py](https://github.com/DotPin/INFO290/blob/master/Comunicaciones/Trabajo%201/Solucion/Decodificador/calculo.py): Archivo prototipo cual realiza la función de transcripción de imágenes.

## Requerimientos de sistema

- SO Linux, Kubuntu 24.04
- Python

## Requerimientos de Software

- Instalación de librerías.
    - Image
    - ImageDraw
    - ImageFont
    - time
    - math
    - numpy
    - scipy

### Ejecución

- Ejecutar compresor de datos

```bash
$python3 trans.py <image>.png
```


  