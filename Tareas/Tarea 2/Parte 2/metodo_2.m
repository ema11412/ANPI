function [xk, k, error] = metodo_2(F, x0, vars, tol, iterMax)
  
  %Esta funci�n se encarga de resolver un sistema de ecuaciones no lineales
  %
  %Sintaxis: metodo_2(F, x0, vars, tol, iterMax)
  %
  %Par�metros Iniciales: 
  %            F = es un vector de celdas que contiene strings
  %            x0 = es un vector columna que tiene los valores iniciales para la solucion
  %            vars = es una lista que incluye debe incluir todas las variables presentes en la funci�n
  %            tol = un n�mero positivo que representa a la tolerancia para el criterio: ||(f(xk))||2 < tol
  %            iterMax = cantidad de iteraciones m�ximas
  %   
  %Par�metros de Salida:                           
  %            xk = aproximaci�n de la solucion del sistema de ecuaciones
  %            k = n�mero de iteraciones realizados
  %            error = ||(F(xk))||2
  
  pkg load symbolic
  warning('off', 'all');

  cantVars = length(vars);

  xk = x0;

  for i = 1:cantVars
    symVars(i) = sym(vars(i));  
  endfor

  error = tol + 1 ;
  e = [];
  iteraciones = [];
  k = 1;

  while and(error > tol, k < iterMax)

    for i=1:cantVars
      func = matlabFunction(sym(F(i))); 
      fk = double(subs(func, symVars, xk));
      vFx(i,1) = fk;
    end
    
    error = norm(vFx, 2);
    e = [e error];
    J = [];
    
    for i=1:cantVars
      func = matlabFunction(sym(F(i)));
      Jk = jacobian(func, symVars);
      Je = double(subs(Jk, symVars, xk));
      J = [J Je];
    end
    
    Jx = reshape(J,[cantVars,cantVars]);
    Jx = Jx';
    
    yk = xk - (1/2) * (Jx \ vFx);
    
    J = [];
    
    for i=1:cantVars
      func = matlabFunction(sym(F(i)));
      Jk = jacobian(func, symVars);
      Je = double(subs(Jk, symVars, yk));
      J = [J Je];
    end
    
    Jy = reshape(J,[cantVars,cantVars]);
    Jy = Jy';

    xk = xk - Jy \ vFx;
    
    iteraciones = [iteraciones k];
    k = k + 1;
  
  end

  plot(iteraciones, e)

endfunction