%% Para poder ejecutar el programa es necesario importar la matriz de valores A con el vector B
%% de los archivos "matris A.csv" y "vector B.csv"
%% y para ejecutarse deben estar en el mismo directorio.
A = dlmread("matriz A.csv",",")
B = dlmread("vector B.csv")
n = length(B)
format short

%  plp = true;
%  while plp
%    nn = input("Ingrese el numero de error posible a iterar, debe ser menor que 0.05: ");
%    if nn <0.05
%      plp = false;
%    end
%  end
nn = 0.0001
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
Vgs= inv(D+E)*B 

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

matriz =zeros(8,13);
for i=1:1:13
   matriz(9,i)= 4;
end
for i=1:1:9
   matriz(i,1)= 4;
end
for i=1:1:12
   matriz(8,i+1)=x(i);
end
for i=1:1:12
   matriz(7,i+1)=x(i+12);
end
for i=1:1:9
   matriz(6,i+1)=x(i+24);
end
for i=1:1:8
   matriz(5,i+1)=x(i+33);
end
for i=1:1:3
   matriz(4,i+1)=x(i+41);
end

for i=1:1:2
   matriz(3,i+1)=x(i+44);
end
matriz(2,2)=x(47)
matriz
disp('Matriz resuelta por Diferencias Finitas:');
%disp(matriz);
figure(2);
surf(matriz');
title("Gráfico de Tº de una placa irregular 3D");
xlabel('Nodo posición y');
ylabel('Nodo posición x');
zlabel('Temperatura de la placa');
xxx = input("Presione enter para terminar")
