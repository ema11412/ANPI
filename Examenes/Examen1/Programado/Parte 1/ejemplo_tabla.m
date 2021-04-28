clc; clear
pkg load dataframe
pkg load symbolic

function [df] = derivar(f,x)
    %Utilice esta funcion para realizar los calulos de derivadas
    
    aux = strcat('@(x)',f); 
    f1 = str2func(aux);
    h=0.000000001;
    df = (f1(x + h) - f1(x)) / h;
endfunction

function [x,k]=newton(f,x0,tol,iterMax)  
    %Esta función aproxima la solución de la ecuación f(x)=0, utilizando el método de la newton
    %
    %Sintaxis:  newton(f,x0,tol,iterMax)
    % 
    %Parámetros Iniciales: 
    %Entra una funcion definida arriba, por el parametro de entrada x0 
    %utilizads en la formula recursiva          
    %            
    %            
    %Parámetros de Salida:                           
    %Muestra una grafica con los valores de el error 
    %Muestra la ultima iteracion y su valor calculado           
    %  
    aux = strcat('@(x)',f); % @x + función
    f1 = str2func(aux); % función string a ecuación

    x=[]; k=[]; error=[];

    k=0;
    error=tol+1;
    e=[];
        while and(error>tol,k<iterMax)
            k=k+1;
            if ((derivar(f,x0) == 0))
              break;  
            endif
            x= x0-(f1(x0)/(derivar(f,x0)));
            error=abs(f1(x));
            e=[e error];
            x0=x;
        endwhile
        %plot(1:k,e)
end

function [x,k]=steffensen(f,x0,tol,iterMax)  
    %Esta función aproxima la solución de la ecuación f(x)=0, utilizando el método de la newton
    %
    %Sintaxis:  steffensen(f,x0,tol,iterMax)
    % 
    %Parámetros Iniciales: 
    %Entra una funcion definida arriba, por el parametro de entrada x0 
    %utilizads en la formula recursiva          
    %            
    %            
    %Parámetros de Salida:                           
    %Muestra una grafica con los valores de el error 
    %Muestra la ultima iteracion y su valor calculado           
    %  
    aux = strcat('@(x)',f); % @x + función
    f1 = str2func(aux); % función string a ecuación
    x=[]; k=[]; error=[];
    k=0;
    error=tol+1;
    e=[];
        while and(error>tol,k<iterMax)
            if ((f1(x0+f1(x0))-f1(x0)) == 0)
              break; 
            endif
            k=k+1;
            x= x0-((f1(x0))^2/(f1(x0+f1(x0))-f1(x0)));
            error=abs(f1(x));
            e=[e error];
            x0=x;
        endwhile
        %plot(1:k,e)
end

function [x,k]=NewtonSteff(f,x0,tol,iterMax)  
    %Esta función aproxima la solución de la ecuación f(x)=0, utilizando el método de la newton
    %
    %Sintaxis:  NewtonSteff(f,x0,tol,iterMax)
    % 
    %Parámetros Iniciales: 
    %Entra una funcion definida arriba, por el parametro de entrada x0 
    %utilizads en la formula recursiva          
    %            
    %            
    %Parámetros de Salida:                           
    %Muestra una grafica con los valores de el error 
    %Muestra la ultima iteracion y su valor calculado           
    %  
    aux = strcat('@(x)',f); % @x + función
    f1 = str2func(aux); % función string a ecuación
    x=[]; k=[]; error=[];
    k=0;
    error=tol+1;
    e=[];
        while and(error>tol,k<iterMax)
            k=k+1;
            if ((derivar(f,x0)) == 0)
              break; 
            endif            
            xl=x0-(f1(x0)/(derivar(f,x0)));
            
            if ((derivar(f,x0))*(f1(x0)-f1(xl)) == 0)
              break; 
            endif            
            x=x0-((f1(x0))^2/((derivar(f,x0))*(f1(x0)-f1(xl))));
            error=abs(f1(x));
            e=[e error];
            x0=x;
        endwhile
        %plot(1:k,e)
end
x01=2;
x02=1;
x03=15;
%primera prueba atan(x)
[x11,k11]=newton('atan(x)',x01,10^-10,10);
[x21,k21]=steffensen('atan(x)',x01,10^-10,10);
[x31,k31]=NewtonSteff('atan(x)',x01,10^-10,10);
%segunda prueba sin(x)-x/2
[x12,k12]=newton('sin(x)-x/2',x01,10^-10,10);
[x22,k22]=steffensen('sin(x)-x/2',x01,10^-10,10);
[x33,k32]=NewtonSteff('sin(x)-x/2',x01,10^-10,10);
%tercera prueba 10*x*exp(-x^2)-1
[x13,k13]=newton('10*x*exp(-x^2)-1',x02,10^-10,10);
[x23,k23]=steffensen('10*x*exp(-x^2)-1',x02,10^-10,10);
[x33,k33]=NewtonSteff('10*x*exp(-x^2)-1',x02,10^-10,10);
%cuarta prueba x^6-36*x^5+450*x^4-2400*x^3+5400*x^2-4320*x+720
[x14,k14]=newton('x^6-36*x^5+450*x^4-2400*x^3+5400*x^2-4320*x+720',x03,10^-10,10);
[x24,k24]=steffensen('x^6-36*x^5+450*x^4-2400*x^3+5400*x^2-4320*x+720',x03,10^-10,10);
[x34,k34]=NewtonSteff('x^6-36*x^5+450*x^4-2400*x^3+5400*x^2-4320*x+720',x03,10^-10,10);
%quinta prueba x*log10(x)-1.2
[x15,k15]=newton('x*log10(x)-1.2',x01,10^-10,10);
[x25,k25]=steffensen('x*log10(x)-1.2',x01,10^-10,10);
[x35,k35]=NewtonSteff('x*log10(x)-1.2',x01,10^-10,10);

C = {"f(x)"          , "x0", "Raiz", "Iteracion NM", "Iteracion SM", "Iteracion NSM"; 
     "atan(x)"       , x01 , 0.00000000000000 , k11,k21,k31; 
     "sin(x)-x/2"    , x01 , 1.89549426703398 , k12,k22,k32;
     "10xexp(-x^2)-1", x02 , 1.67963061042845 , k13,k23,k33;
     "x^6-36x^5+.."  , x03 , 15.98287398060170, k14,k24,k34;
     "xlog10(x)-1.2" , x01 , 2.74064609597369 , k15,k25,k35};
dataframe (C)
