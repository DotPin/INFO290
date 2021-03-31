**************************************************************************
FUNCIONAMIENTO************************************************************
**************************************************************************

-Programa Jotoshop, este programa abre en una interfaz sencilla con un frame
de 2 paneles, en estos 2 paneles se desarrolla la aplicacion de filtros.

-En el panel nº1 se muestra la imagen original junto con los botones
para la ejecucion de los filtros en el panel nº 2.

-Para cada filtro se ha asignado un panel distinto que se ubica en la 2a
posicion del frame quedandose inactivo.

-Estos filtros por panel son: Negativo, Escala de Grises, Blanco y negro, 
Brillo y contraste, y redimencion.

	El Filtro de negativo, aplica el filtro en el panel nº2

	El filtro escala de grises, aplica automaticamente el filtro en el 
	panel nº2

	El filtro Blanco y negro, aplica al instante el filtro en el
	panel nº2.

	El filtro Brillo y Contraste, aplica este filtro de manera 
	progresiva con un Slider por separado con el contraste y son 
	aplicados por botones, "Pintar C" y "Pintar B", los rangos estan
	asignados por cada Slider de -100 a +100 dando el 0 como filtro 
	neutro.

	El filtro de Redimencion, aplica este filtro de manera progresiva
	con un Slider aumentando y reduciendo la imagen su tamaño, 
	seleccionandola con el objeto, y pindandose con el boton "Pintar",
	el rango es desde -10 a +10 dejando el 0 como el neutro de la imagen.

-El programa cuenta con un boton exit para salir del programa y cerrar el
proceso de carga de imagen que deja al estar abierto el programa, junto 
con el proceso de java.exe



**************************************************************************
AUTORES/DESARROLLADORES***************************************************
**************************************************************************


@Diego ROjas Asenjo, Estudiante Ingeniería Civil en Informática



**************************************************************************
LICENCIA******************************************************************
**************************************************************************


@Programa Desarrollado en codigo Java, uso demo ilimitado.


**************************************************************************
LISTADO DE BUGS***********************************************************
**************************************************************************

-el proceso sigue corriendo si cierra con el _EXIT_ON_CLOSE.
-La imagen si no abre es por la ruta dada para el BufferedImage 
 de la clase Filtro

**************************************************************************
REQUERIMIENTOS************************************************************
**************************************************************************

-Instalado el JDK/JRE versiones 1.5xxxx o superior
-SO Linux / WIndows 98,Me,Nt,2000,XP,Vista,W7.
-Agregado en las variables de entorno de desarrollo path carpeta /bin de
emulador o desarrollador Java.

**************************************************************************
INSTALACION/EJECUCION*****************************************************
**************************************************************************

-Instalado el JDK/JRE junto con las variables de entorno
-hubicar archivo .Jar en alguna localizacion a ejecutar, abrir ventana de 
 comandos
-buscar el archivo .jar en el directorio
-aplicar comando java -jar [nombre archivo].jar para ejecutar.



by ?a¢???T€?