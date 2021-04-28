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
   vars = ['x'];
   Fi = {'x^2+1'};
   x0 = [0.5];
   iterMax = 50;
   
   [xk, k, error] = newton_raphson_nl(Fi, x0, vars, tol, iterMax)
   
end
