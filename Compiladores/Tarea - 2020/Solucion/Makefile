all: 
	bison -yd LMA.y
	flex Tarea1.l
	gcc y.tab.c lex.yy.c -lfl -o salida
	./salida

run:
	./salida

clean:
	rm y.tab.c y.tab.h lex.yy.c salida