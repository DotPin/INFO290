%Variables
clear all %% borra todo lo guardado
 n= 18000 ;   %Numero de iteraciones
t = 0;         %Tiempo inicial
%tf= 1800;
h = 0.1;     %Tamaño de paso
%n=(tf-ti)/h;
%t=ti:h:tf;
% reserva de memoria 
      A=[]; 
      B=[]; 
      C=[]; 
      D=[]; 
      E=[];
      K=[];
      L=[];
      M=[];
      N=[];
      O=[];
      P=[];
      Q=[];
      T=[];
%condiciones iniciales
x6 = 0;
x5 = 0;
x4 = 0;                      
x3 = 0;                      
x2 = 0;                      
x1 = 0;    

f  = 1300 ;    %fuerza, esta al final está dentro de las formulas

    
   %Variables Auxiliares como condiciones iniciales
        g = 0;        %variable auxiliar para x´6
        m = 0;        %variable auxiliar para x´5
        u = 0;        %Variable auxiliar para x'4
        v = 0;        %Variable auxiliar para x'3
        w = 0;        %Variable auxiliar para x'2
        z = 0;        %Variable auxiliar para x'1


for i=1:n
    g1  = g+(h*F12(t,g,m,u,v,w,z,x6,x5,x4,x3,x2,x1,f ));
    m1  = m+(h*F11(t,g,m,u,v,w,z,x6,x5,x4,x3,x2,x1,f ));
    u1  = u+(h*F10(t,g,m,u,v,w,z,x6,x5,x4,x3,x2,x1,f ));
    v1  = v+(h*F9(t,g,m,u,v,w,z,x6,x5,x4,x3,x2,x1,f ));
    w1  = w+(h*F8(t,g,m,u,v,w,z,x6,x5,x4,x3,x2,x1,f ));
    z1  = z+(h*F7(t,g,m,u,v,w,z,x6,x5,x4,x3,x2,x1,f ));
    x61 = x4+(h*F6(t,g,m,u,v,w,z,x6,x5,x4,x3,x2,x1,f ));
    x51 = x4+(h*F5(t,g,m,u,v,w,z,x6,x5,x4,x3,x2,x1,f ));
    x41 = x4+(h*F4(t,g,m,u,v,w,z,x6,x5,x4,x3,x2,x1,f ));
    x31 = x3+(h*F3(t,g,m,u,v,w,z,x6,x5,x4,x3,x2,x1,f ));
    x21 = x2+(h*F2(t,g,m,u,v,w,z,x6,x5,x4,x3,x2,x1,f ));
    x11 = x1+(h*F1(t,g,m,u,v,w,z,x6,x5,x4,x3,x2,x1,f ));
    
    g  = g1;
    m  = m1;
    u  = u1;
    v  = v1;
    w  = w1;
    z  = z1;
    x6 = x61;
    x5 = x51;
    x4 = x41;
    x3 = x31;
    x2 = x21;
    x1 = x11;
    t  = t+h;
    f  = 1300;
      A(end+1)=g; 
      B(end+1)=m;
      C(end+1)=u;
      D(end+1)=v;
      E(end+1)=w;
      K(end+1)=z;
      L(end+1)=x6;
      M(end+1)=x5;
      N(end+1)=x4;
      O(end+1)=x3;
      P(end+1)=x2;
      Q(end+1)=x1;
      T(end+1)=t;
   
    disp(['Iteración Euler número ' num2str(i) ':']);
    
    
    
end
   subplot(2,1,1)
    plot(T,L,'c.',T,M,'m.',T,N,'g.',T,O,'b.',T,P,'k.',T,Q,'r.');
        xlabel('t');
        ylabel('x1,x2,x3,x4,x5,x6');
        legend('x6','x5','x4','x3','x2','x1','Location','Southeast')
    title('posición: EULER')
    subplot(2,1,2)
    plot(T,A,'c.',T,B,'m.',T,C,'g.',T,D,'b.',T,E,'k.',T,K,'r.');
        xlabel('t');
        ylabel('velocidad');
        legend('x6','x5','x4','x3','x2','x1')
    title('velocidad: EULER')