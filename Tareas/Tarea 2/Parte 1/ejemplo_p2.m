function [xk, k, error] = ejemplo_p2()
  
   %Esta funci�n se encarga de insertar los datos del ejercicio 1 del pdf Problemas numericos para la tarea
   %
   %Sintaxis: ejemplo_p2()
   %   
   %Par�metros de Salida:                           
   %            xk = aproximaci�n de la solucion del sistema de ecuaciones
   %            k = n�mero de iteraciones realizados
   %            error = ||(F(xk))||2
   
   tol = 10^-5;
   vars = ['x' 'y' 'z' 'w'];
   Fi = {'4*x-y+z-x*w', 'x-2*y+3*z-z*w', '-x+3*y-2*z-y*w', 'x^2+y^2+z^2-1'};
   x0 = [0.5; 0.5; 0.5; 0.5];
   iterMax = 50;
   
   [xk, k, error] = newton_raphson_nl(Fi, x0, vars, tol, iterMax)
   
end
