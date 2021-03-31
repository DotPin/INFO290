invertida = ""
c = ""
cnt = 0
with open("/home/diego/Escritorio/prueba.txt",'r') as a:
#with open("d:\\noticia.txt",'r') as a:
    for linea in a:
        print(linea, end ="")
        c = c + linea
        cnt += 1
    print("\n")
    print("*"*50+"\n")
with open("/home/diego/Escritorio/prueba.txt",'r') as a:
#with open ("d:\\noticia.txt")as a:
    linea = 0
    for leefrase in c:
            if linea==cnt-2:
                invertida = "\n" + leefrase + invertida
            else:
                invertida = leefrase + invertida
            linea += 1
print("Archivo invertido: ")
print("{0}".format(invertida))
with open("/home/diego/Escritorio/prueba2.txt",'w') as d:
#with open("d:\\noticia2.txt",'w') as d:
    d.write(invertida)
        
    
   
