echo "Comenzando algoritmo de diferencias divididas"
for i in 1 2 3
do
 echo "."
 sleep 1
done
python3 valores2.py
python3 descomposicion.py
for i in 1 2 3
do
 echo "."
 sleep 1
done
echo "La duración de los gráficos será de 10 segundos para proseguir con el programa"
echo "Comenzando solucion de Cholesky"
for i in 1 2 3
do
 echo "."
 sleep 1
done
octave cholesky_2.m
octave cholesky_3.m
echo "Comenzando solucion con Gaus Seidel"
for i in 1 2 3
do
 echo "."
 sleep 1
done
octave GausSeidel.m
octave GausSeidel_2.m
