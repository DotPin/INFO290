all:
	java -cp java-cup-11b.jar:. java_cup.Main as.cup  
	jflex al.flex
	javac -cp java-cup-11b-runtime.jar:. *.java
	java -cp java-cup-11b-runtime.jar:. Main
