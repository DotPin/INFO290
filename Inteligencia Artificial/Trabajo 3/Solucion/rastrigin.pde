// PSO de acuerdo a  (p.247 ss)

PImage surf; // imagen que entrega el fitness

// ===============================================================
Table table;
float d = 15; // radio del círculo, solo para despliegue

int puntos = 100;    //población de partículas
Particle[] fl; // arreglo de partículas

float gbestx=100, gbesty=100, gbest=100; // posición y fitness del mejor global
float w = 5000; // inercia: baja (~50): explotación, alta (~5000): exploración (2000 ok)
float C1 = 9.0, C2 =  21.0; // learning factors (C1: own, C2: social) (ok)
float custom_l=0, custom_g=1;    //factores influyentes en los optimos locales y globales donde dichos factores estan dentro de valores [0,1]
float maxv = 3; // max velocidad (modulo)

int evals = 0, evals_to_best = 0; //número de evaluaciones, sólo para despliegue
float criterio=0.0000001;    //parámetro en criterio de salida
int epocas=0;    //permite saber cuantas evoluciones lleva

float delta_w=1000,delta_c1=0,delta_c2=30, delta_custom_l=0, delta_custom_g=1;
boolean stop=false, tabla=true;  //parámetros en la creación de la tabla
int tope=650; //Valor irá variando según la cantidad de datos queramos mostrar en la ventana
float intervalo = (5.12*2)/tope, intervalo2 = (5.12*2)/250;    //intervalo de iteraciones

int variacion=0;    //permite el control de iteraciones para las variacion de parámetros C1,C2, W

float [][] xx;
float [][] yy;
float [][] z;

void reinicia(){
  gbestx=100; gbesty=1000; gbest=100; // posición y fitness del mejor global
  
  //w = delta_w; // inercia: baja (~50): explotación, alta (~5000): exploración (2000 ok)  <-----descomentar cuando se necesite experimantar con variaciones en W
  //C1 = delta_c1; C2 =  delta_c2; // learning factors (C1: own, C2: social) (ok)          <-----descomentar cuando se necesite experimantar con variaciones en C1,C2
 
  custom_l = delta_custom_l;
  custom_g = delta_custom_g;
  
  evals = 0; evals_to_best = 0; //número de evaluaciones, sólo para despliegue
  epocas=0;
}

void mesh(){
 float inicio=-5.12;
  xx = new float[tope][tope];
  yy = new float[tope][tope];
  for(int i=0; i<tope;i++){
    for(int j=0; j<tope;j++){
      xx[j][i] = inicio;
      yy[i][j] = inicio;
    }
    inicio = inicio + intervalo;
  }
  
}


void rastrigin_z(){
  mesh();
  z = new float[tope][tope];
  for(int i=0; i<tope;i++){
    for(int j=0; j<tope;j++){
      z[i][j] = (xx[i][j]*xx[i][j]-10*cos(2*PI*xx[i][j]))+ (yy[i][j]*yy[i][j]-10*cos(2*PI*yy[i][j])) + 20;
    }
  }
}

class Particle{
  float x, y, fit; // posición actual(x,y-vector)  y ajuste (x,y-fitness)
  float px, py, pfit=100; // position (p-vector) and ajuste local (p-fitness) mejor solucion local
  float vx, vy; //velocidad vectorial (v-vector)
  
  // ---------------------------- Constructor
  Particle(){
    x = random(width); y = random(height);
    vx = random(-1,1) ; vy = random(-1,1);
  }
  
  // ---------------------------- Evalúa partícula (Función de optimización)
  float Eval(){ 
    evals++;
    
    if (x>650) x=649;
    if (y>650) y=649;
    if (x<0) x=0;
    if (y<0) y=0;

    fit = z[int(x)][int(y)];

    if(fit <= pfit){ // actualiza local best si es mejor
      pfit = fit;
      px = x;
      py = y;
    }
    
    if (fit <= gbest){ // actualiza global best
      gbest = fit;
      gbestx = x;
      gbesty = y;
      evals_to_best = evals;  /*Parámetro que descubre el mejor valor optimizado*/
    };
    return fit; //retorna el mejor ajuste
  }
  
  // ------------------------------ mueve la partícula
  void move(){
  
    //actualiza velocidad (fórmula mezclada)
    vx = w * vx + custom_l*C1*(px - x) + custom_g*C2*(gbestx - x);
    vy = w * vy + custom_l*C1*(py - y) + custom_g*C2*(gbesty - y);
    
    // trunca velocidad a maxv (Arreglo del parámetro de la velocidad)
    float modu = sqrt(vx*vx + vy*vy);
    
    if (modu > maxv){
      vx = vx/modu*maxv;
      vy = vy/modu*maxv;
    }
    
    // update position
    x = x + vx;
    y = y + vy;
    
    // rebota en murallas
    if (x > width || x < 0) vx = - vx;
    if (y > height || y < 0) vy = - vy;
  }
  
  // ------------------------------ despliega partícula
  void display(){
    color c=surf.get(int(x),int(y)); 
    fill(c);
    ellipse (x,y,d,d);
    stroke(#ff0000);
    line(x,y,x-10*vx,y-10*vy);

  }
}

void despliegaBest(){
  fill(#0000ff);
  ellipse(gbestx,gbesty,d,d);
  PFont f = createFont("Arial",12,true);
  textFont(f,10);
  fill(#00ff00);
  text("Best fitness: "+str(gbest)+"\nEvals to best: "+str(evals_to_best)+"\nEvals: "+str(evals)+"\nEpocas: "+str(epocas)+"\nGlobal X:"+str(gbestx)+"\nGlobal Y:"+str(gbesty)+"\nC1: "+str(C1)+"\nC2: "+str(C2)+"\nW: "+str(w)+"\nCustom_local: "+str(custom_l)+"\nCustom_Global: "+str(custom_g),10,20);
}

void parada(){
  if (gbest< criterio){
    stop=true;
  }
}

void setup(){  
  rastrigin_z();
  size(650,650); //setea width y height (de acuerdo al tamaño de la imagen)
  if (tabla){
    CreaTabla();    //permite generar el objeto para exportar los datos.
    //dibuja();    //Importante si no se tiene la representación gráfica de la función objetivo
  }
  surf = loadImage("rastrigin.jpg");
  smooth();
  fl = new Particle[puntos];
  for(int i =0;i<puntos;i++)
    fl[i] = new Particle();
}

void draw(){ /*REPEAT*/
  
  parada();
  if (stop) {
    stop=false;
    llena_tabla();    //importante para la recopilacion de datos
    setup();
    reinicia();
  }
 
  image(surf,0,0);
 
  for(int i = 0;i<puntos;i++){ /*ACTUALIZA POSICIÓN DE PARTÍCULAS*/
    fl[i].display();
  }
  despliegaBest(); /*actualiza parámetros en salida*/
  
  //calcula, ajusta y actualiza el movimiento de las partículas
  for(int i = 0;i<puntos;i++){
    fl[i].move(); /*Update velocities y Move to the new position*/
    fl[i].Eval(); /* busca las mejores posiciones para las partículas y las actualiza*/
  }
  
  epocas++;
}
/*
void dibuja(){    // genera imagen de la función objetivo en 2D de la representación 3D, revisar grafica.m por octave
  background(0);
  for (int yy = 0; yy < tope; yy += 1) {
    for (int xx = 0; xx < tope; xx += 1) {
      stroke(z[xx][yy]);    //esta función determina el color del punto que grafica según la salida del rastrigin donde debería calcular su gradiante en color y dsp tirar a stroke
      point(xx, yy); //gráfica se encuentra desplazada pixeles hacia abajo y hacia la derecha 
    }
  }
  save("rastrigin.jpg");
}
*/

void delta2(){  //función que permite variar parámetro en óptimos locales y globales
  delta_custom_l += intervalo2 ;
  delta_custom_g -= intervalo2 ;
  if(delta_custom_l>1){
    saveTable(table, "data/datos_"+str(int(puntos))+"_"+str(int(w))+"_"+str(int(C1))+"_"+str(int(C2))+".csv");
    exit();
  }
}

/*
void delta(){    //funcion que permite hacer variar los parámetros de movimiento de cada partícula C1, C2, W, ademas de dar finalizacion del experimento y exportar datos
  variacion++;
  delta_c1 += 0.5;
  delta_c2 -= 0.5;
  if (variacion>59){
    delta_w = delta_w + 1000;
    delta_c1=0;
    delta_c2=30;
    variacion=0;
  }
  if (w==6000){
    saveTable(table, "data/datos.csv");
    exit();
  }
}*/

void llena_tabla(){    // permite integrar elementos de cada ciclo del experimento en grilla para una hoja de calculo
  TableRow fila = table.addRow();
  fila.setInt("Particulas", puntos);
  fila.setFloat("Inercia", w);
  fila.setFloat("C1", C1);
  fila.setFloat("C2", C2);
  fila.setFloat("custom_l", delta_custom_l);  //borrar línea en caso de escoger variaciones con respecto a C1,C2 y W
  fila.setFloat("custom_g", delta_custom_g);  //borrar línea en caso de escoger variaciones con respecto a C1,C2 y W
  fila.setFloat("Parada", criterio);
  fila.setFloat("Ajuste", gbest);
  fila.setFloat("Evaluaciones", evals_to_best);
  fila.setInt("Epocas", epocas);
  //delta();  // funcion de variación en C1, C2 y W
  delta2();
}

void CreaTabla(){    //genera el objeto de planilla de calculo
  table = new Table();
  table.addColumn("Particulas");
  table.addColumn("Inercia");
  table.addColumn("C1");
  table.addColumn("C2");
  table.addColumn("custom_l");    
  table.addColumn("custom_g");    
  table.addColumn("Parada");
  table.addColumn("Ajuste");
  table.addColumn("Evaluaciones");
  table.addColumn("Epocas");
  tabla=false;
  print("\nCrea Tabla");
}


/*
Algoritmo de Particle Swarm Optimization, Generación canónica por Jorge Maturana Ortiz
Editado por: Diego Rojas Asenjo.
*/
