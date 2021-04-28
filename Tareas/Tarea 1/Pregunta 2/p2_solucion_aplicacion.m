function [xk, k, error] = p2_solucion_aplicacion(tol, iterMax)
  
   %Esta funci�n se encarga de insertar los datos del problema de ingenier�a elegido en la funci�n BFGS
   %
   %Sintaxis: p2_solucion_aplicacion(tol, iterMax)
   %
   %Par�metros Iniciales: 
   %            tol = un n�mero positivo que representa a la tolerancia para el criterio: ||gradiente(f(x_k))|| <= tol
   %            iterMax = cantidad de iteraciones m�ximas
   %   
   %Par�metros de Salida:                           
   %            x_k = aproximaci�n de los valores de convergencia de la funci�n f
   %            k = n�mero de iteraciones realizados
   %            error = ||gradiente(f(x_k))||
   
   
   %Se inserta la ecuaci�n del problema de ingenier�a seleccionado en el metodo bfgs realizado en el archivo p2_bfgs.m
   [xk, k, error] = p2_bfgs('(10-m*5-b)**2 + (15-m*7.5-b)**2 + (25-m*8-b)**2 + (5-m*4-b)**2 + (30-m*10-b)**2', ['m' 'b'], tol, iterMax)
   
end
