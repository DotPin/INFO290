clear all
syms x y 
N=[1-x-y,2*x,2*y];

partex=diff(N,x); partey=diff(N,y);
KDX=int(int(transpose(partex)*partex,y,0,1-x),x,0,1)
KDY=int(int(transpose(partey)*partey,y,0,1-x),x,0,1)
% Ensamblar con Li, K=suma(LiT*KTri*Li)  KTri=KGX+KDY sol=inv(KD)*f 
