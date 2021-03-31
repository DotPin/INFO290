

%Matriz A de valores

A=[-11.6 0 2.25 0;
    0 -11.6 0 2.25;
    2.25 0 -11.6 0;
    0 2.25 0 -11.5];

% Vector b

b=[-639 ; -639 ; -864 ; -864];

% Matriz D
D=zeros(4,4);
for i=1:1:4
    D(i,i)=A(i,i);
           
end

% Matriz U
F=zeros(4,4);
for c=2:1:4
    for f=c:1:4
        E(c,f) = A(c,f);
    end
end

% Matriz L
E = zeros(4,4)
for c=1:1:4
    for f=c:1:4
        E(f,c) = A(f,c);
    end
end

% Matriz Mgs y Vgs
Mgs=-inv(D+E)*F
Vgs= inv(D+E)*b

% Iteraciones para solucion del sistema
x=zeros(4,1);
for i=0:1:19
    x=Mgs*x+Vgs
end
