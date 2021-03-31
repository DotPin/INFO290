function gs = GausSeidel(A,B,nn, p)
%  A = Matriz cuadrada
%  B = vector sistema AX=B
% nn =factor de error
%  p= norma subordinada 1,2,inf
%  programa ejecutarlo directo en programa corriendo octave:n>GausSeidel([Matriz],[Vector],error,NormaSubordinada):

%Matriz A de valores

n = length(B)


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
Mgs=-inv(D+E)*F
Vgs= inv(D+E)*B

% Iteraciones para solucion del sistema
x=zeros(n,1),

norm(Mgs,p)
norm((Mgs*x+Vgs - x),p)
k = log((nn*(1-norm(Mgs,p)))/norm((Mgs*x+Vgs - x),p))/log(norm(Mgs,p))

for i=0:1:19
    x=Mgs*x+Vgs
end

