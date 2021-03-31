from random import randint
sigue = True
sigue2 = True
cnt = 0
x = 0
mnd = ""
rst = ""
frase = ""
rsp = ""
with open ("d:\\log.txt",'w') as a:
    monto = 4000
    print("Su monto inicial es de {0}".format(monto))
    print("*"*50+("\n"))
    while sigue:
        if monto<1:
            print("\n")
            print("*"*41)
            print("A ud no le queda suficiente para apostar*")
            print("*"*41)
            sigue = False
            cnt = str(cnt)
            frase = ("Se quedó pato en la jugada "+cnt+"\n")
            a.write(frase)
        else:
            while sigue2:
                try:
                    x = int(input("Ingrese apuesta: "))
                    while x<1 or x>monto:
                        if x<1:
                            print("Error no está apostando")
                        else:
                            print("No tiene suficiente para apostar")
                        x = int(input("Ingrese otravez "))
                    sigue2 = False
                except ValueError:
                    print("Error si apuesta no es válida")
            mnd = input("Lance la moneda. Presione \"Intro\":")
            while mnd!= "":
                print("Error solo debe lanzar la moneda")
                mnd = input("Intente otravez. Presione \"Intro\":")
            cnt += 1
            mnd = randint(0,1)
            if mnd == 1:
                monto = monto - x
                x = (x*2)
                monto = monto + x
                print("Cara, ud. gana, Dobla a {0} tiene {1}".format(x,monto))
                rst = ("Cara ud. gana, Dobla")
            else:
                monto = monto - x
                x = (x*0)
                print("Sello, ud. Pierde, apuesta en {0} tiene {1}".format(x,monto))
                rst = ("Sello, ud. Pierde")
            cnt = str(cnt)
            x = str(x)
            monto = str(monto)
            frase = ("Jugada "+cnt+" apostó "+x+" resultando "+"\""+rst+"\""+" Le queda "+monto+"\n")
            a.write(frase) #hace registro de las partidas
            cnt = int(cnt)
            x = int(x)
            monto = int(monto)
            rsp = input("Continuar? si/no: ")
            rsp = rsp.upper()
            if rsp == "SI":
                sigue = True
                sigue2 = True
            else:
                sigue = False
            

with open("d:\\log.txt",'r') as b:
    print("\n")
    mnd = input("*"*59+"\n"+"Acontinuacion se hará lectura del registro, presione enter:"+"\n"+"*"*59+"\n")
    while mnd!="":
        mnd = input("*"*39+"\n"+"Solo presione enter para leer registro:"+"\n"+"*"*39+"\n")
    for linea in b:
        print (linea)
        
            
                    
                
        
