

%Matriz A de valores

%A=[-11.6 0 2.25 0;
%    0 -11.6 0 2.25;
%    2.25 0 -11.6 0;
%    0 2.25 0 -11.5];

% Vector b

%b=[-639 ; -639 ; -864 ; -864];

A = dlmread("matriz A.csv",",");
B = dlmread("vector B.csv");
n = length(B);


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
D
F
E
% Matriz Mgs y Vgs
Mgs=-inv(D+E)*F;
Vgs= inv(D+E)*B ;

% Iteraciones para solucion del sistema
x=zeros(n,1),

nn = 0.00001
norm(Mgs,2)
norm((Mgs*x+Vgs - x),2)
k = log((nn*(1-norm(Mgs,2)))/norm((Mgs*x+Vgs - x),2))/log(norm(Mgs,2))

for i=0:1:19
    x=Mgs*x+Vgs
end

