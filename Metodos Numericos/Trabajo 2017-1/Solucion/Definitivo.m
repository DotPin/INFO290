%% Para poder ejecutar el programa es necesario importar la matriz de valores A con el vector B
% para ello debe ejecutarse antes el archivo Dif_finitas.py
% luego generará los archivos "matris A.csv" y "vector B.csv"
% y para ejecutarse deben estar en el mismo directorio.


A = dlmread("matriz_a",",")
B = dlmread("matriz_b")
n = length(B)
format short

plp = true;
  while plp
    nn = input("Ingrese el numero de error posible a iterar, debe ser menor que 0.05: ");
    if nn <0.05
      plp = false;
    end
  end

  
a = input("Ingrese el lado cuadrado de la superficie: ");
z = input("Ingrese la profundidad de la superficie: ");
a = a*2-2
z = z*2-2
  
% Matriz D
D=zeros(n,n);
for i=1:1:n
    D(i,i)=A(i,i);
           
end

% Matriz U
F=zeros(n,n);
for c=1:1:n
    for f=c+1:1:n
        F(c,f) = A(c,f);
    end
end

% Matriz L
E = zeros(n,n);
for c=1:1:n
    for f=c+1:1:n
        E(f,c) = A(f,c);
    end
end

% Matriz Mgs y Vgs
Mgs=-inv(D+E)*F
Vgs= inv(D+E)*B' 

% Iteraciones para solucion del sistema
x=zeros(n,1);
norm(Mgs,2);
norm((Mgs*x+Vgs - x),2);
printf ("Numero de iteraciones aproximadas a realizar")
k = ceil( log((nn*(1-norm(Mgs,2)))/norm((Mgs*x+Vgs - x),2))/log(norm(Mgs,2)) )

zz = input("Comienza el metodo iterativo, presione 'enter' ")

for i=0:1:k
      v = x;
      x=Mgs*x+Vgs
      x1 = x-v;
      e = norm(x1,2)/norm(x,2);
      if e < nn
	break
      end
end
printf("Solucion aproximada 'X' del sistema \n")
x
printf("Error relativo de corte \n")
e
printf("Cantidad de iteraciones realizadas \n")
i

matriz = zeros(a,a,z);
n
p = 0
for i=1:z
  for j=1:a
    for k=1:a
      p += 1
      matriz(k,j,i)= x(p)*-1;
    end
  end
end


printf("A continuación se mostrarán los valores representados en cada malla como conjunto solución de los nodos \n");
for i=1:z
  matriz(:,:,i)
end
disp('Matriz resuelta por Diferencias Finitas:');
%disp(matriz);
figure(2);
mesh(matriz);
title("Gráfico de Tº de una placa irregular 3D");
xlabel('Nodo posición y');
ylabel('Nodo posición x');
zlabel('Temperatura de la placa');
printf("Exportando resultados en archivo DF_X.csv \n");
xxx = input("Presione enter para terminar");