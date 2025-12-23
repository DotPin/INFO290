%Variables
clear all %% borra todo lo guardado
n = 1000;     %Numero de iteraciones
t = 0;         %Tiempo inicial
h = 0.1;     %Tamaño de paso
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
    K1g  = F12(t,g,m,u,v,w,z,x6,x5,x4,x3,x2,x1,f );   
    K1m  = F11(t,g,m,u,v,w,z,x6,x5,x4,x3,x2,x1,f );
    K1u  = F10(t,g,m,u,v,w,z,x6,x5,x4,x3,x2,x1,f );
    K1v  = F9(t,g,m,u,v,w,z,x6,x5,x4,x3,x2,x1,f );
    K1w  = F8(t,g,m,u,v,w,z,x6,x5,x4,x3,x2,x1,f );
    K1z  = F7(t,g,m,u,v,w,z,x6,x5,x4,x3,x2,x1,f );
    K1x6 = F6(t,g,m,u,v,w,z,x6,x5,x4,x3,x2,x1,f );
    K1x5 = F5(t,g,m,u,v,w,z,x6,x5,x4,x3,x2,x1,f );
    K1x4 = F4(t,g,m,u,v,w,z,x6,x5,x4,x3,x2,x1,f );
    K1x3 = F3(t,g,m,u,v,w,z,x6,x5,x4,x3,x2,x1,f );
    K1x2 = F2(t,g,m,u,v,w,z,x6,x5,x4,x3,x2,x1,f );
    K1x1 = F1(t,g,m,u,v,w,z,x6,x5,x4,x3,x2,x1,f );
    
    K2g  = F12(t+h,g+h*K1g,m+h*K1m,u+h*K1u,v+h*K1v,w+h*K1w,z+h*K1z,x6+h*K1x6,x5+h*K1x5,x4+h*K1x4,x3+h*K1x3,x2+h*K1x2,x1+h*K1x1,f );   
    K2m  = F11(t+h,g+h*K1g,m+h*K1m,u+h*K1u,v+h*K1v,w+h*K1w,z+h*K1z,x6+h*K1x6,x5+h*K1x5,x4+h*K1x4,x3+h*K1x3,x2+h*K1x2,x1+h*K1x1,f );
    K2u  = F10(t+h,g+h*K1g,m+h*K1m,u+h*K1u,v+h*K1v,w+h*K1w,z+h*K1z,x6+h*K1x6,x5+h*K1x5,x4+h*K1x4,x3+h*K1x3,x2+h*K1x2,x1+h*K1x1,f );
    K2v  = F9(t+h,g+h*K1g,m+h*K1m,u+h*K1u,v+h*K1v,w+h*K1w,z+h*K1z,x6+h*K1x6,x5+h*K1x5,x4+h*K1x4,x3+h*K1x3,x2+h*K1x2,x1+h*K1x1,f );
    K2w  = F8(t+h,g+h*K1g,m+h*K1m,u+h*K1u,v+h*K1v,w+h*K1w,z+h*K1z,x6+h*K1x6,x5+h*K1x5,x4+h*K1x4,x3+h*K1x3,x2+h*K1x2,x1+h*K1x1,f );
    K2z  = F7(t+h,g+h*K1g,m+h*K1m,u+h*K1u,v+h*K1v,w+h*K1w,z+h*K1z,x6+h*K1x6,x5+h*K1x5,x4+h*K1x4,x3+h*K1x3,x2+h*K1x2,x1+h*K1x1,f );
    K2x6 = F6(t+h,g+h*K1g,m+h*K1m,u+h*K1u,v+h*K1v,w+h*K1w,z+h*K1z,x6+h*K1x6,x5+h*K1x5,x4+h*K1x4,x3+h*K1x3,x2+h*K1x2,x1+h*K1x1,f );
    K2x5 = F5(t+h,g+h*K1g,m+h*K1m,u+h*K1u,v+h*K1v,w+h*K1w,z+h*K1z,x6+h*K1x6,x5+h*K1x5,x4+h*K1x4,x3+h*K1x3,x2+h*K1x2,x1+h*K1x1,f );
    K2x4 = F4(t+h,g+h*K1g,m+h*K1m,u+h*K1u,v+h*K1v,w+h*K1w,z+h*K1z,x6+h*K1x6,x5+h*K1x5,x4+h*K1x4,x3+h*K1x3,x2+h*K1x2,x1+h*K1x1,f );
    K2x3 = F3(t+h,g+h*K1g,m+h*K1m,u+h*K1u,v+h*K1v,w+h*K1w,z+h*K1z,x6+h*K1x6,x5+h*K1x5,x4+h*K1x4,x3+h*K1x3,x2+h*K1x2,x1+h*K1x1,f );
    K2x2 = F2(t+h,g+h*K1g,m+h*K1m,u+h*K1u,v+h*K1v,w+h*K1w,z+h*K1z,x6+h*K1x6,x5+h*K1x5,x4+h*K1x4,x3+h*K1x3,x2+h*K1x2,x1+h*K1x1,f );
    K2x1 = F1(t+h,g+h*K1g,m+h*K1m,u+h*K1u,v+h*K1v,w+h*K1w,z+h*K1z,x6+h*K1x6,x5+h*K1x5,x4+h*K1x4,x3+h*K1x3,x2+h*K1x2,x1+h*K1x1,f );
    
    g1  = g+(h/2)*(K1g+K2g);  
    m1  = m+(h/2)*(K1m+K2m);
    u1  = u+(h/2)*(K1u+K2u);
    v1  = v+(h/2)*(K1v+K2v);
    w1  = w+(h/2)*(K1w+K2w);
    z1  = z+(h/2)*(K1z+K2z);
    x61 = x6+(h/2)*(K1x6+K2x6);
    x51 = x5+(h/2)*(K1x5+K2x5);
    x41 = x4+(h/2)*(K1x4+K2x4);
    x31 = x3+(h/2)*(K1x3+K2x3);
    x21 = x2+(h/2)*(K1x2+K2x2);
    x11 = x1+(h/2)*(K1x1+K2x1);
    
    
    u  = u1;
    v  = v1;
    w  = w1;
    z  = z1;
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
    
    disp(['Iteración Heun número ' num2str(i) ':']);
    
    
    
end

 subplot(2,1,1)
    plot(T,L,'y.',T,M,'m.',T,N,'g.',T,O,'b.',T,P,'k.',T,Q,'r.');
        xlabel('t');
        ylabel('x1,x2,x3,x4,x5,x6');
        legend('x6','x5','x4','x3','x2','x1','Location','Southeast')
    title('posición: HEUN')
    subplot(2,1,2)
    plot(T,A,'y.',T,B,'m.',T,C,'g.',T,D,'b.',T,E,'k.',T,K,'r.');
        xlabel('t');
        ylabel('velocidad');
        legend('x6','x5','x4','x3','x2','x1')
    title('velocidad: HEUN')