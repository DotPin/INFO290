all: LMA.y Tarea1.l
	bison -yd LMA.y
	flex Tarea1.l
	gcc y.tab.c lex.yy.c -lfl -o salida