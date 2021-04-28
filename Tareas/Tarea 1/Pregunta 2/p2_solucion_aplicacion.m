function [xk, k, error] = p2_solucion_aplicacion(tol, iterMax)
  
   %Esta función se encarga de insertar los datos del problema de ingeniería elegido en la función BFGS
   %
   %Sintaxis: p2_solucion_aplicacion(tol, iterMax)
   %
   %Parámetros Iniciales: 
   %            tol = un número positivo que representa a la tolerancia para el criterio: ||gradiente(f(x_k))|| <= tol
   %            iterMax = cantidad de iteraciones máximas
   %   
   %Parámetros de Salida:                           
   %            x_k = aproximación de los valores de convergencia de la función f
   %            k = número de iteraciones realizados
   %            error = ||gradiente(f(x_k))||
   
   
   %Se inserta la ecuación del problema de ingeniería seleccionado en el metodo bfgs realizado en el archivo p2_bfgs.m
   [xk, k, error] = p2_bfgs('(10-m*5-b)**2 + (15-m*7.5-b)**2 + (25-m*8-b)**2 + (5-m*4-b)**2 + (30-m*10-b)**2', ['m' 'b'], tol, iterMax)
   
end
