ach = ""
ld = 0
num = ""
cnt = 0
print(ach)
with open("/home/diego/Escritorio/numeros.txt",'r') as a:
	for linea in a:
		ld = len(linea)
		for i in range (ld):
			if linea[i]!=" ":
				num = num + linea[i]
			else:
				ach = ach + num + (" ")
				num = ""
		
	ach = ach + linea[ld-1] + ("\n")
with open("/home/diego/Escritorio/nm.txt",'w') as b:
	b.write(ach)		
print(ach)
	
