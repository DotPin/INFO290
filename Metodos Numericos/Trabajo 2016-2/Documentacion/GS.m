clear;clc
format short
%%  Importamos matriz y vector de valores del sistema Ax = B
A = dlmread("matriz A.csv",",")
B = dlmread("vector B.csv")
n = length(B)
X = zeros(n,1)
Error_eval = ones(n,1)

printf ('Entrando a diagonal dominante')
%%Evaluamos si la matriz A es diagonal dominante
for i = 1:n
    j = 1:n;
    j(i) = [];
    B = abs(A(i,j))
    Check(i) = abs(A(i,i)) - sum(B) % es la diagonal mas grande que la suma de las filas coordenadas?
    if Check(i) < 0
        fprintf('La matriz no es estrictamente diagonal dominante por fila %2i\n\n',i)
    end
end


%% Comenzando el metodo iterativo
printf ('Comenzando con GS')
iteracion = 0;
while max(Error_eval) > 0.001
    iteracion = iteracion + 1;
    Z = X;  % guarda el valor entrante para calcular el error despues
    for i = 1:n
        j = 1:n; % define un arreglo de coeficientes
        j(i) = []  % elimina el coeficiente desconocido de los faltantes
        Xtemp = X  % copia los desconocidos en una nueva variable
        Xtemp(i) = []  % eliminate the unknown under question from the set of values
        X(i) = (B(i) - sum(A(i,j) * Xtemp)) / A(i,i)
    end
    Xsolution(:,iteracion) = X
    Error_eval = sqrt((X - Z).^2);
end

%% Display Results
GaussSeidelTabla = [1:iteracion;Xsolution]'
MaTrIx = [A X B]
