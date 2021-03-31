u=-8:0.5:8;
v=u;
[U,V] = meshgrid(u,v)
r = sqrt(U.^2+V.^2)+eps
w=sin(r)./r
mesh(w)
surf(w)
x = input("presione enter")
