function [xk, k, error] = ejemplo_p1()
  
   %Esta función se encarga de insertar los datos del ejercicio de la diapositiva 16 del archivo Método Newton-Raphson - 1.pdf
   %
   %Sintaxis: ejemplo_p1()
   %   
   %Parámetros de Salida:                           
   %            xk = aproximación de la solucion del sistema de ecuaciones
   %            k = número de iteraciones realizados
   %            error = ||(F(xk))||2
   
   tol = 10^-5;
   vars = ['x' 'y' 'z'];
   Fi = {'cos(y)-cos(x)' , 'z^x - 1/y' , 'exp(x)-z^2'};
   x0 = [0.5; 0.5; 0.5];
   iterMax = 50;

   [xk, k, error] = metodo_1(Fi, x0, vars, tol, iterMax)

   [xk, k, error] = metodo_2(Fi, x0, vars, tol, iterMax)

end
