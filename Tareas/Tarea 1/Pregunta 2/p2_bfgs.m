function [xk, k, error] = p2_bfgs(f, vars, tol, iterMax)

    %Esta funci�n se encarga de buscar el punto que minimiza una funci�n de varias variables
    %
    %Sintaxis: p2_bfgs(f, vars, tol, iterMax)
    %
    %Par�metros Iniciales: 
    %            f = es un string que representa a la funci�n f
    %            vars = es una lista que incluye debe incluir todas las variables presentes en la funci�n
    %            tol = un n�mero positivo que representa a la tolerancia para el criterio: ||gradiente(f(x_k))|| <= tol
    %            iterMax = cantidad de iteraciones m�ximas
    %   
    %Par�metros de Salida:                           
    %            x_k = aproximaci�n de los valores de convergencia de la funci�n f
    %            k = n�mero de iteraciones realizados
    %            error = ||gradiente(f(x_k))||

    pkg load symbolic
    
    func = matlabFunction(sym(f));
    cantVars = length(vars);
    
    #Se calcula el vector inicial xk de valores aleatorios mayores que cero
    for i = 1:cantVars
      symVars(i) = sym(vars(i));
      x0(i) = rand() * 10;
    endfor 
    xk = x0';   
   
    #Se calcula el gradiente de la funci�n y se eval�a el vector xk en ella para obtener gk
    g = gradient(func, symVars);
    gk = double(subs(g, symVars, x0));

    #Se calcula una matriz identidad nxn, donde n es la cantidad de variables presentes en la ecuaci�n
    bk = eye(cantVars);
   
    #Se definen los valores de alpha y epsilon, adem�s se calculan los valores de sigma1 y sigma2 de manera aleatoria,
    #donde sigma 1 debe ser menor a sigma2, ambos deben ser mayores que 0 y menores que 1, y sigma2 debe ser mayor a 0.5
    sigma1 = 2;
    sigma2 = 1;
    alpha = 1;
    epsilon = 1;
    
    while and(sigma1 > sigma2, sigma2 > 0.5)
      sigma1 = rand();
      sigma2 = rand();
    end
    
    #Se asigna el valor de k y el error
    k = 0;
    error = tol + 1;
    e = [];
    
    #Inicio del loop principal del programa
    while and(error > tol, k < iterMax)
      
      #Se calcula la matriz pk y se define el valor de lambdak, adem�s se crea una bandera y un contador, que se encargan de evitar
      #el caso de que no se llegue a encontrar un lambda y se encicle indefinidamente
      pk = bk**-1 * -gk;
      lambdak = 1;
      count = 1;
      check = false;
      
      #Inicio del loop del c�lculo del lambdak
      while true
        #Se calcula la inecuaci�n 2.6 del art�culo, el t�rmino de la derecha y el de la izquierda y se comparan
        #si se cumple, reinicia el contador y sale del while, adem�s reinicia el contador, si no se cumple divide
        #el lambdak actual entre 5 y suma 1 al contador, en caso de que el contador llegue a 11, el programa
        #activar� la bandera check y saldr� del while.
        a = xk + (lambdak * pk);
        izq1 = double(subs(func, symVars, a));
        der1 = (double(subs(func, symVars, xk)) + (sigma1 * lambdak * gk' * pk));
        #izq2 = double(subs(g, symVars, a))' * pk;
        #der2 = sigma2 * gk' * pk;
        if izq1 <= der1
          display('Lambda encontrado!!!')
          count = 1;
          break
        elseif count > 10
          display('Lambda no encontrado, terminando el proceso...')
          check = true;
          break
        else
          lambdak = lambdak / 5;
          count += 1;
          display(lambdak)
        end
       end
       
       #Si la bandera check esta activa, detiene el while principal del programa, dando fin a este.
       if check
         break
       end
       
       #Se realiza el c�lculo del vector xk1
       xk1 = xk + (lambdak * pk);
       
       #Se determina si es necesario calcular una nueva matriz bk, por medio de la ecuaci�n 2.10 del art�culo
       #en caso de que se cumpla la desigualdad, se determina el nuevo valor para bk, sino se queda igual     
       sk = xk1 - xk;
       gk1 = double(subs(g, symVars, xk1));
       yk = gk1 - gk;
           
       if (yk' * sk) / norm(sk)**2 >= epsilon * norm(gk)**alpha
         bk = bk - (((bk * sk) * (sk' * bk)) / (sk' * bk * sk)) + ((yk * yk') / (yk' * sk));
       end
       
       #Se calcula el error con la norma del gradiente     
       error = double(norm(subs(g, symVars, xk)));
       e = [e error];
       k = k + 1;

       #Se cambian los valores del vector xk1 a xk y del gradiente gk1 a gk
       xk = xk1;
       gk = gk1;
    end
    plot(1 : k, e) 
end

[xk, k, error] = p2_bfgs('(x-2)^2 + (y+3)^2 +x*y', ['x' 'y'], 10**-5, 25)
