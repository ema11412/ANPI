import math
import matplotlib.pyplot as plt

#-- La funcion se definio en varias partes, las cuales se indican 
#-- Ademas en en documento escrito se especifica la formula matematica
#-- asociada a cada funcion. 

def f(d):
    #Esta es la funcion a calcular su raiz.
    #Valores iniciales
    x1=7
    x2=6
    
    #La variable de la funcion es d
    return (math.log10(x1/d))/(R()*math.log(10))+(d*(x2-d))/(C(d))


def R():
    #Funcion sigma_R
    #Se nos da los valores iniciales
    #(variable alpha)
    a=4
    #(variable sigma_dB)
    dB=4
    return (dB**2)/(10*a)**2

def S():
    #Funcion S, la cual es el area de un circulo
    #Se nos da el valor inicial de r
    r=10
    return math.pi*r**2

def G(d):
    #Funcion g(d) dada en el problema
    #Nos dan el valor inicial r
    r=10
    
    #La variable de la funcion es d
    return ((2*S())/(math.pi))*math.acos(d/(2*r))-d*math.sqrt(r**2-(d**2)/4)

def k():
    #Funcion k utilizada en el problema
    #valor inicial a dada en el problema (variable alpha en la especificacion)
    a=4
    return (10*a)/(math.log(10))

def C(d):
    #Funcion sigma_c
    #Valor inicial L (lamda)
    L=1
    
    #La variable de la funcion es d
    return ((G(d))**2)/(2*L*(k())**2)*(1/G(d)+1/S())


#metodos
#------------------------------------------------------------------------------
def biseccion(f,a,b,tol):
    #El metodo tiene como entradas:
    #Una funcion f
    #Valores a,b los cuales son valores iniciales.
    #la tolerancia tol, ingresada por el usuario. 
    
    #Las salidas son:
    #El valor de x solucion de la ecuacion
    #Las iteraciones necesarias hasta llegar a la tolerancia
    #El error asosciado a la solucion |f(x)|
    #Un grafico iteracionex (k) contra error.
    e=[]
    sol=[]
    #Teorema de Bolzano
    if(f(a)*f(b) > 0):
        print("No cumple con el teorema de Bolzano")
    else:
        k=0
        error=tol+1
        while  (error>tol):
            k+=1
            x=(b+a)/2
            error=abs(f(x))
            if(f(a)*f(x)<0):
                b=x
            else:
                a=x
            e=e+[error]
            sol = sol + [x]
            
    #Grafica el valor de las distintas soluciones
    plt.plot(e,  label='Biseccion')
    #El valor de la ultima iteracion se muestra
    print("Biseccion")
    print("x = ",x)
    print("k = " ,k)
    print("error = ",error)
    print(" ")

#------------------------------------------------------------------------------
def secante(f,x0,x1,tol):
    #El metodo tiene como entradas:
    #Una funcion f
    #Valores x0,x1, los cuales son valores iniciales.
    #la tolerancia tol, ingresada por el usuario. 
    
    #Las salidas son:
    #El valor de x solucion de la ecuacion
    #Las iteraciones necesarias hasta llegar a la tolerancia
    #El error asosciado a la solucion |f(x)|
    #Un grafico iteracionex (k) contra error.
    e=[]
    sol=[]
    k=0
    error=tol+1
    
    while (error>tol):
        xk= x1-((x1-x0)/(f(x1)-f(x0)))*f(x1)
        error=abs(f(xk))
        k+=1
        x0=x1
        x1=xk
        e=e+[error]
        sol = sol + [xk]

    #Grafica el valor de las distintas soluciones
    plt.plot(e,  label='Secante')
    #El valor de la ultima iteracion se muestra
    print("Secante")
    print("x = ",xk)
    print("k = " ,k)
    print("error = ",error)
    print(" ")

#------------------------------------------------------------------------------
def Secante(a, b):
    c = b - (b - a) * f(b) / (f(b) - f(a))  # Otorgar valor a x.
    return c
def Falsa_Posicion(f1,x0,x1,tol):
    #El metodo tiene como entradas:
    #Una funcion f
    #Valores x0,x1, los cuales son valores iniciales.
    #la tolerancia tol, ingresada por el usuario. 
    
    #Las salidas son:
    #El valor de x solucion de la ecuacion
    #Las iteraciones necesarias hasta llegar a la tolerancia
    #El error asosciado a la solucion |f(x)|
    #Un grafico iteracionex (k) contra error.
    e=[]
    sol=[]
    #Teorema de Bolzano
    if(f1(x0)*f1(x1) > 0):
        print("No cumple con el teorema de Bolzano")
    else:
        k=0
        error=tol+1
        x3=x0
        while  (error>tol):
            k+=1
            x2=Secante(x0, x1)
            
            if(f(x0)*f(x2)<0):
                x3 = Secante(x0, x2)
                x0=x1
                x1=x2
            elif(f(x1)*f(x2)<0):
                x3 = Secante(x1, x2)
                x0=x1
                x1=x2
            error=abs(f(x3))
            e=e+[error]
            sol = sol + [x3]

    #Grafica el valor de las distintas soluciones
    #Grafica el valor de las distintas soluciones
    plt.title('Grafica de errores')
    plt.ylabel('Error')
    plt.xlabel('Iteraciones')
    plt.plot(e,  label='Falsa Pos')
    #El valor de la ultima iteracion se muestra
    plt.legend(title='Metodos')
    plt.grid(axis='x', color='0.95')
    plt.grid(axis='y', color='0.95')
    plt.savefig("Graficas.pdf", bbox_inches='tight')
    print("Falsa pisicion")
    print("x = ",x3)
    print("k = " ,k)
    print("error = ",error)
    print(" ")
#------------------------------------------------------------------------------    
    
biseccion(f,6,6.5,pow(10, -10))

secante(f,6,6.5,pow(10, -10))

Falsa_Posicion(f,6,6.5,pow(10, -10))