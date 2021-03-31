def suma(lst,lst1):		# a = 1"_"2"_"3"_"4"_"5
	ln = len(lst)		# b = 6"_"7"_"8"_"9"_"0		
	n1 = ""
	n2 = ""
	rst = ""
	print(lst)
	print(lst1)
	for i in range (ln):
		if lst[i] != " ":
			n1 = n1 + lst[i]
			n2 = n2 + lst1[i]
		else:
			n1 = int(n1)
			n2 = int(n2)
			rst = rst + (" ") + str(n1 + n2) + (" ")
			n1 = ""
			n2 = ""
	n1 = int(lst[ln-1])
	n2 = int(lst1[ln-1])
	rst = rst + (" ") + str(n1 + n2) + ("\n")
	return rst

#*****************************************************************************
#****************Programa principal*******************************************

ach1 = ""
ach2 = ""
cnt1 = ""
with open("/numeros.txt",'w') as a:
#with open("/home/diego/Escritorio/numeros.txt",'w') as a:
	x = input("ingrese numeros con 1 espacio: ")
	a.write(x)
with open("/numeros2.txt",'w') as b:
#with open("home/diego/Escritorio/numeros2.txt",'w') as b:
	y = input("ingrese numeros con 1 espacio otravez: ")
	b.write(y)

with open("/numeros.txt",'r') as a:
        ach1 = a.readline()
with open("/numeros2.txt",'r') as b:
        ach2 = b.readline()
#with open("/home/diego/Escritorio/numeros.txt",'r') as a:
#with open("/home/diego/Escritorio/numeros2.txt",'r') as b:
cnt1 = suma(ach1,ach2)
with open("/numeros3.txt",'w') as c:
#with open("/home/diego/Escritorio/numeros2.txt",'w') as c:
	c.write(cnt1)
with open("/numeros3.txt",'r') as c:
#with open("/home/diego/Escritorio/numeros2.txt",'r') as c:
	for linea in c:
		print(linea, end="")












