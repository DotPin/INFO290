from random import randint
with open("\log.txt",'w') as a:
    sigue = True
    sigue2 = True
    cnt = 0
    rst = ""
    frase = ""
    rst2 = ""
    rst3 = 0
    while sigue:
        while sigue2:
            try:
                x = int(input("Ingrese el monto a apostar: "))
                while x<1:
                    print("Error el monto debe ser superior a $1")
                    x = int(input("Intente otravez: "))
                sigue2 = False
            except ValueError:
                print("Error ingreso no valido")
        mnd = input("Lance la moneda, presione \"L\"")
        mnd = mnd.upper()
        while mnd!="L":
            print("Error solo debe presionar \"L\"")
            mnd = input("Lance otravez")
            mnd = mnd.upper()
        rnd = randint(0,1)
        cnt += 1
        if rnd==0:
            print("Sello, Duplica")
            rst = ("Sello, Duplica")
            rst3 = rst3+(x * 2)
        else:
            print("Cara, pierde todo")
            rst = ("Cara, pierde todo")
            rst3 = 0
        cnt = str(cnt)
        rst3 = str(rst3)
        frase = ("Numero de jugada ")+cnt+(" ud. apostó ")+rst3+(" y ")+rst+("\n")
        cnt = int(cnt)
        rst3 = int(rst3)
        a.write(frase)
        rst2 = input("Seguir jugando? \"ingrese ok\": ")
        rst2 = rst2.upper()
        sigue2 = True
        if rst2!= "OK":
            sigue = False

print("*"*50)
print("A continuacion se hará una lectura de los resultados del juego")
with open("\log.txt",'r') as b:
    for linea in b:
        print(linea)
        
