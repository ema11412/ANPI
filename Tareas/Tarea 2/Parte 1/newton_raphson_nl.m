function [xk, k, error] = newton_raphson_nl(F, x0, vars, tol, iterMax)

  %Esta función se encarga de resolver un sistema de ecuaciones no lineales
  %
  %Sintaxis: newton_raphson_nl(F, x0, vars, tol, iterMax)
  %
  %Parámetros Iniciales: 
  %            F = es un vector de celdas que contiene strings de funciones
  %            x0 = es un vector columna que tiene los valores iniciales para la solucion
  %            vars = es una lista que incluye debe incluir todas las variables presentes en la función
  %            tol = un número positivo que representa a la tolerancia para el criterio: ||(F(xk))||2 < tol
  %            iterMax = cantidad de iteraciones máximas
  %   
  %Parámetros de Salida:                           
  %            xk = aproximación de la solucion del sistema de ecuaciones
  %            k = número de iteraciones realizados
  %            error = ||(F(xk))||2
  
  pkg load symbolic
  warning('off', 'all');

  error = tol + 1 ;
  e = [];
  iteraciones = [];

  cantVars = length(vars);

  xk = x0;

  for i = 1:cantVars
    symVars(i) = sym(vars(i));
  endfor
  
  k = 1;
  
  while and(error > tol, k < iterMax)
    
    for i = 1:cantVars
      func = matlabFunction(sym(F(i))); 
      fk = double(subs(func, symVars, xk));
      vF(i,1) = fk;
    endfor
    
    error = norm(vF, 2);
    e = [e error];
    J = [];
    
    for i = 1:cantVars
      func = matlabFunction(sym(F(i)));
      Jk = jacobian(func, symVars);
      Je = double(subs(Jk, symVars, xk));
      J=[J Je];
    endfor
    
    Jf = reshape(J,[cantVars,cantVars]);
    Jf = Jf';

    xk = xk - (Jf \ vF);
    
    iteraciones = [iteraciones k];
    k = k + 1;
  
  endwhile

  plot(iteraciones, e)

endfunction


