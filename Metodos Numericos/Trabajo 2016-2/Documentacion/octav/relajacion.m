A = dlmread("matriz A.csv",",")
B = dlmread("vector b.csv")
U = dlmread("real2.csv")
r = zeros(47,1)

%realizamos el sumado y guardado en la matriz U los elementros, preparando para la relajación sucesiva
c = 0
for i=1:1:47
  for j=1:1:47
    c = c + A(i,j)
    r(i) = c + B(i)


xx = input("suma de valores terminada, presione enter para continuar")
%Vector R preparado para el calculo de la ralajación sucesiva

o = norm(A,2) %se calcula la norma 2 del sistema lineal

%calculamos el peso w parala relajación sucesiva

w = 2/(1 +sqrt(q-o^2))

%realizamos la relajación sucesiva del sistema para aproximar los valores soluciones

xx = input("valor de la matriz U")
U

z=1
for i=1:4
  for j=2:6
    if ( U(i,j)<>0 )
      U(i,j) = U(i,j) + w*r(z)
    else
      U(i,j) = 0
      z = z + 1
    end
  end
end

xx = input("Valor de la matriz U, iterada")
U
