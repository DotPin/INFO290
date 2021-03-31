clear all %% borra todo lo guardado
n = 18000;     %Numero de iteraciones
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


for i = 1:n
    
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
    
    K2g  = F12(t+(h/2),g+(h/2)*K1g,m+(h/2)*K1m,u+(h/2)*K1u,v+(h/2)*K1v,w+(h/2)*K1w,z+(h/2)*K1z,x6+(h/2)*K1x6,x5+(h/2)*K1x5,x4+(h/2)*K1x4,x3+(h/2)*K1x3,x2+(h/2)*K1x2,x1+(h/2)*K1x1,f );   
    K2m  = F11(t+(h/2),g+(h/2)*K1g,m+(h/2)*K1m,u+(h/2)*K1u,v+(h/2)*K1v,w+(h/2)*K1w,z+(h/2)*K1z,x6+(h/2)*K1x6,x5+(h/2)*K1x5,x4+(h/2)*K1x4,x3+(h/2)*K1x3,x2+(h/2)*K1x2,x1+(h/2)*K1x1,f );
    K2u  = F10(t+(h/2),g+(h/2)*K1g,m+(h/2)*K1m,u+(h/2)*K1u,v+(h/2)*K1v,w+(h/2)*K1w,z+(h/2)*K1z,x6+(h/2)*K1x6,x5+(h/2)*K1x5,x4+(h/2)*K1x4,x3+(h/2)*K1x3,x2+(h/2)*K1x2,x1+(h/2)*K1x1,f );
    K2v  = F9(t+(h/2),g+(h/2)*K1g,m+(h/2)*K1m,u+(h/2)*K1u,v+(h/2)*K1v,w+(h/2)*K1w,z+(h/2)*K1z,x6+(h/2)*K1x6,x5+(h/2)*K1x5,x4+(h/2)*K1x4,x3+(h/2)*K1x3,x2+(h/2)*K1x2,x1+(h/2)*K1x1,f );
    K2w  = F8(t+(h/2),g+(h/2)*K1g,m+(h/2)*K1m,u+(h/2)*K1u,v+(h/2)*K1v,w+(h/2)*K1w,z+(h/2)*K1z,x6+(h/2)*K1x6,x5+(h/2)*K1x5,x4+(h/2)*K1x4,x3+(h/2)*K1x3,x2+(h/2)*K1x2,x1+(h/2)*K1x1,f );
    K2z  = F7(t+(h/2),g+(h/2)*K1g,m+(h/2)*K1m,u+(h/2)*K1u,v+(h/2)*K1v,w+(h/2)*K1w,z+(h/2)*K1z,x6+(h/2)*K1x6,x5+(h/2)*K1x5,x4+(h/2)*K1x4,x3+(h/2)*K1x3,x2+(h/2)*K1x2,x1+(h/2)*K1x1,f );
    K2x6 = F6(t+(h/2),g+(h/2)*K1g,m+(h/2)*K1m,u+(h/2)*K1u,v+(h/2)*K1v,w+(h/2)*K1w,z+(h/2)*K1z,x6+(h/2)*K1x6,x5+(h/2)*K1x5,x4+(h/2)*K1x4,x3+(h/2)*K1x3,x2+(h/2)*K1x2,x1+(h/2)*K1x1,f );
    K2x5 = F5(t+(h/2),g+(h/2)*K1g,m+(h/2)*K1m,u+(h/2)*K1u,v+(h/2)*K1v,w+(h/2)*K1w,z+(h/2)*K1z,x6+(h/2)*K1x6,x5+(h/2)*K1x5,x4+(h/2)*K1x4,x3+(h/2)*K1x3,x2+(h/2)*K1x2,x1+(h/2)*K1x1,f );
    K2x4 = F4(t+(h/2),g+(h/2)*K1g,m+(h/2)*K1m,u+(h/2)*K1u,v+(h/2)*K1v,w+(h/2)*K1w,z+(h/2)*K1z,x6+(h/2)*K1x6,x5+(h/2)*K1x5,x4+(h/2)*K1x4,x3+(h/2)*K1x3,x2+(h/2)*K1x2,x1+(h/2)*K1x1,f );
    K2x3 = F3(t+(h/2),g+(h/2)*K1g,m+(h/2)*K1m,u+(h/2)*K1u,v+(h/2)*K1v,w+(h/2)*K1w,z+(h/2)*K1z,x6+(h/2)*K1x6,x5+(h/2)*K1x5,x4+(h/2)*K1x4,x3+(h/2)*K1x3,x2+(h/2)*K1x2,x1+(h/2)*K1x1,f );
    K2x2 = F2(t+(h/2),g+(h/2)*K1g,m+(h/2)*K1m,u+(h/2)*K1u,v+(h/2)*K1v,w+(h/2)*K1w,z+(h/2)*K1z,x6+(h/2)*K1x6,x5+(h/2)*K1x5,x4+(h/2)*K1x4,x3+(h/2)*K1x3,x2+(h/2)*K1x2,x1+(h/2)*K1x1,f );
    K2x1 = F1(t+(h/2),g+(h/2)*K1g,m+(h/2)*K1m,u+(h/2)*K1u,v+(h/2)*K1v,w+(h/2)*K1w,z+(h/2)*K1z,x6+(h/2)*K1x6,x5+(h/2)*K1x5,x4+(h/2)*K1x4,x3+(h/2)*K1x3,x2+(h/2)*K1x2,x1+(h/2)*K1x1,f );

    K3g  = F12(t+(h/2),g+(h/2)*K2g,m+(h/2)*K2m,u+(h/2)*K2u,v+(h/2)*K2v,w+(h/2)*K2w,z+(h/2)*K2z,x6+(h/2)*K2x6,x5+(h/2)*K2x5,x4+(h/2)*K2x4,x3+(h/2)*K2x3,x2+(h/2)*K2x2,x1+(h/2)*K2x1,f );   
    K3m  = F11(t+(h/2),g+(h/2)*K2g,m+(h/2)*K2m,u+(h/2)*K2u,v+(h/2)*K2v,w+(h/2)*K2w,z+(h/2)*K2z,x6+(h/2)*K2x6,x5+(h/2)*K2x5,x4+(h/2)*K2x4,x3+(h/2)*K2x3,x2+(h/2)*K2x2,x1+(h/2)*K2x1,f ); 
    K3u  = F10(t+(h/2),g+(h/2)*K2g,m+(h/2)*K2m,u+(h/2)*K2u,v+(h/2)*K2v,w+(h/2)*K2w,z+(h/2)*K2z,x6+(h/2)*K2x6,x5+(h/2)*K2x5,x4+(h/2)*K2x4,x3+(h/2)*K2x3,x2+(h/2)*K2x2,x1+(h/2)*K2x1,f ); 
    K3v  = F9(t+(h/2),g+(h/2)*K2g,m+(h/2)*K2m,u+(h/2)*K2u,v+(h/2)*K2v,w+(h/2)*K2w,z+(h/2)*K2z,x6+(h/2)*K2x6,x5+(h/2)*K2x5,x4+(h/2)*K2x4,x3+(h/2)*K2x3,x2+(h/2)*K2x2,x1+(h/2)*K2x1,f ); 
    K3w  = F8(t+(h/2),g+(h/2)*K2g,m+(h/2)*K2m,u+(h/2)*K2u,v+(h/2)*K2v,w+(h/2)*K2w,z+(h/2)*K2z,x6+(h/2)*K2x6,x5+(h/2)*K2x5,x4+(h/2)*K2x4,x3+(h/2)*K2x3,x2+(h/2)*K2x2,x1+(h/2)*K2x1,f ); 
    K3z  = F7(t+(h/2),g+(h/2)*K2g,m+(h/2)*K2m,u+(h/2)*K2u,v+(h/2)*K2v,w+(h/2)*K2w,z+(h/2)*K2z,x6+(h/2)*K2x6,x5+(h/2)*K2x5,x4+(h/2)*K2x4,x3+(h/2)*K2x3,x2+(h/2)*K2x2,x1+(h/2)*K2x1,f ); 
    K3x6 = F6(t+(h/2),g+(h/2)*K2g,m+(h/2)*K2m,u+(h/2)*K2u,v+(h/2)*K2v,w+(h/2)*K2w,z+(h/2)*K2z,x6+(h/2)*K2x6,x5+(h/2)*K2x5,x4+(h/2)*K2x4,x3+(h/2)*K2x3,x2+(h/2)*K2x2,x1+(h/2)*K2x1,f ); 
    K3x5 = F5(t+(h/2),g+(h/2)*K2g,m+(h/2)*K2m,u+(h/2)*K2u,v+(h/2)*K2v,w+(h/2)*K2w,z+(h/2)*K2z,x6+(h/2)*K2x6,x5+(h/2)*K2x5,x4+(h/2)*K2x4,x3+(h/2)*K2x3,x2+(h/2)*K2x2,x1+(h/2)*K2x1,f ); 
    K3x4 = F4(t+(h/2),g+(h/2)*K2g,m+(h/2)*K2m,u+(h/2)*K2u,v+(h/2)*K2v,w+(h/2)*K2w,z+(h/2)*K2z,x6+(h/2)*K2x6,x5+(h/2)*K2x5,x4+(h/2)*K2x4,x3+(h/2)*K2x3,x2+(h/2)*K2x2,x1+(h/2)*K2x1,f ); 
    K3x3 = F3(t+(h/2),g+(h/2)*K2g,m+(h/2)*K2m,u+(h/2)*K2u,v+(h/2)*K2v,w+(h/2)*K2w,z+(h/2)*K2z,x6+(h/2)*K2x6,x5+(h/2)*K2x5,x4+(h/2)*K2x4,x3+(h/2)*K2x3,x2+(h/2)*K2x2,x1+(h/2)*K2x1,f ); 
    K3x2 = F2(t+(h/2),g+(h/2)*K2g,m+(h/2)*K2m,u+(h/2)*K2u,v+(h/2)*K2v,w+(h/2)*K2w,z+(h/2)*K2z,x6+(h/2)*K2x6,x5+(h/2)*K2x5,x4+(h/2)*K2x4,x3+(h/2)*K2x3,x2+(h/2)*K2x2,x1+(h/2)*K2x1,f ); 
    K3x1 = F1(t+(h/2),g+(h/2)*K2g,m+(h/2)*K2m,u+(h/2)*K2u,v+(h/2)*K2v,w+(h/2)*K2w,z+(h/2)*K2z,x6+(h/2)*K2x6,x5+(h/2)*K2x5,x4+(h/2)*K2x4,x3+(h/2)*K2x3,x2+(h/2)*K2x2,x1+(h/2)*K2x1,f ); 
    
    K4g  = F12(t+h,g+(h*K3g),m+(h*K3m),u+(h*K3u),v+(h*K3v),w+(h*K3w),z+(h*K3z),x6+(h*K3x6),x5+(h*K3x5),x4+(h*K3x4),x3+(h*K3x3),x2+(h*K3x2),x1+(h*K3x1),f );   
    K4m  = F11(t+h,g+(h*K3g),m+(h*K3m),u+(h*K3u),v+(h*K3v),w+(h*K3w),z+(h*K3z),x6+(h*K3x6),x5+(h*K3x5),x4+(h*K3x4),x3+(h*K3x3),x2+(h*K3x2),x1+(h*K3x1),f );   
    K4u  = F10(t+h,g+(h*K3g),m+(h*K3m),u+(h*K3u),v+(h*K3v),w+(h*K3w),z+(h*K3z),x6+(h*K3x6),x5+(h*K3x5),x4+(h*K3x4),x3+(h*K3x3),x2+(h*K3x2),x1+(h*K3x1),f );   
    K4v  = F9(t+h,g+(h*K3g),m+(h*K3m),u+(h*K3u),v+(h*K3v),w+(h*K3w),z+(h*K3z),x6+(h*K3x6),x5+(h*K3x5),x4+(h*K3x4),x3+(h*K3x3),x2+(h*K3x2),x1+(h*K3x1),f );   
    K4w  = F8(t+h,g+(h*K3g),m+(h*K3m),u+(h*K3u),v+(h*K3v),w+(h*K3w),z+(h*K3z),x6+(h*K3x6),x5+(h*K3x5),x4+(h*K3x4),x3+(h*K3x3),x2+(h*K3x2),x1+(h*K3x1),f );   
    K4z  = F7(t+h,g+(h*K3g),m+(h*K3m),u+(h*K3u),v+(h*K3v),w+(h*K3w),z+(h*K3z),x6+(h*K3x6),x5+(h*K3x5),x4+(h*K3x4),x3+(h*K3x3),x2+(h*K3x2),x1+(h*K3x1),f );   
    K4x6 = F6(t+h,g+(h*K3g),m+(h*K3m),u+(h*K3u),v+(h*K3v),w+(h*K3w),z+(h*K3z),x6+(h*K3x6),x5+(h*K3x5),x4+(h*K3x4),x3+(h*K3x3),x2+(h*K3x2),x1+(h*K3x1),f );   
    K4x5 = F5(t+h,g+(h*K3g),m+(h*K3m),u+(h*K3u),v+(h*K3v),w+(h*K3w),z+(h*K3z),x6+(h*K3x6),x5+(h*K3x5),x4+(h*K3x4),x3+(h*K3x3),x2+(h*K3x2),x1+(h*K3x1),f );   
    K4x4 = F4(t+h,g+(h*K3g),m+(h*K3m),u+(h*K3u),v+(h*K3v),w+(h*K3w),z+(h*K3z),x6+(h*K3x6),x5+(h*K3x5),x4+(h*K3x4),x3+(h*K3x3),x2+(h*K3x2),x1+(h*K3x1),f );   
    K4x3 = F3(t+h,g+(h*K3g),m+(h*K3m),u+(h*K3u),v+(h*K3v),w+(h*K3w),z+(h*K3z),x6+(h*K3x6),x5+(h*K3x5),x4+(h*K3x4),x3+(h*K3x3),x2+(h*K3x2),x1+(h*K3x1),f );   
    K4x2 = F2(t+h,g+(h*K3g),m+(h*K3m),u+(h*K3u),v+(h*K3v),w+(h*K3w),z+(h*K3z),x6+(h*K3x6),x5+(h*K3x5),x4+(h*K3x4),x3+(h*K3x3),x2+(h*K3x2),x1+(h*K3x1),f );   
    K4x1 = F1(t+h,g+(h*K3g),m+(h*K3m),u+(h*K3u),v+(h*K3v),w+(h*K3w),z+(h*K3z),x6+(h*K3x6),x5+(h*K3x5),x4+(h*K3x4),x3+(h*K3x3),x2+(h*K3x2),x1+(h*K3x1),f );   
    
    g1  = g+(h/6)*(K1g+(2*K2g)+(2*K3g)+K4g);
    m1  = m+(h/6)*(K1m+(2*K2m)+(2*K3m)+K4m);
    u1  = u+(h/6)*(K1u+(2*K2u)+(2*K3u)+K4u);
    v1  = v+(h/6)*(K1v+(2*K2v)+(2*K3v)+K4v);
    w1  = w+(h/6)*(K1w+(2*K2w)+(2*K3w)+K4w);
    z1  = z+(h/6)*(K1z+(2*K2z)+(2*K3z)+K4z);
    x61 = x6+(h/6)*(K1x6+(2*K2x6)+(2*K3x6)+K4x6);
    x51 = x5+(h/6)*(K1x5+(2*K2x5)+(2*K3x5)+K4x5);    
    x41 = x4+(h/6)*(K1x4+(2*K2x4)+(2*K3x4)+K4x4);
    x31 = x3+(h/6)*(K1x3+(2*K2x3)+(2*K3x3)+K4x3);
    x21 = x2+(h/6)*(K1x2+(2*K2x2)+(2*K3x2)+K4x2);
    x11 = x1+(h/6)*(K1x1+(2*K2x1)+(2*K3x1)+K4x1);
    
    
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
    
    disp(['Iteración número ' num2str(i) ':']);
   
    
end

 subplot(2,1,1)
    plot(T,L,'y.',T,M,'m.',T,N,'g.',T,O,'b.',T,P,'k.',T,Q,'r.');
        xlabel('t');
        ylabel('x1,x2,x3,x4,x5,x6');
        legend('x6','x5','x4','x3','x2','x1','Location','Southeast')
    title('posición: RK4')
    subplot(2,1,2)
    plot(T,A,'y.',T,B,'m.',T,C,'g.',T,D,'b.',T,E,'k.',T,K,'r.');
        xlabel('t');
        ylabel('velocidad');
        legend('x6','x5','x4','x3','x2','x1')
    title('velocidad: RK4')