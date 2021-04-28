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

    
#este es el metodo de Steffensen
def stef(a):
    #Entrada valor a
    #Salida valor c
    
    #Aca se calcula un valor de c, es cual es el valor de y_k 
    #de la funcion de principal stef_Secant
    
    #Depende de g(a)
    #NOTA: g(a) != 0, esto no es necesario de verificar
    #ya que converge antes a la solucion.
    c=a-f(a)/g(a)
    return c
def g(a):
    #Entrada valor a
    #Salida valor c
    
    #Esta funcion es complementaria a stef(a).
    c=((f(a+f(a)))/(f(a)))-1
    return c
#-----------aca termina
    
#metodo Steffensen-Secant---------------
def stef_secant(f,x0,tol):
    #El metodo tiene como entradas:
    #Una funcion f
    #Valor inicial x0
    #la tolerancia tol, ingresada por el usuario. 
    
    #Las salidas son:
    #El valor de x solucion de la ecuacion
    #Las iteraciones necesarias hasta llegar a la tolerancia
    #El error asosciado a la solucion |f(x)|
    #Un grafico iteracionex (k) contra error.
    
    #Se le asigna el valor inicial a la variable interna -> a
    a=x0
    #valor inicial de y_k
    b=stef(x0)
    e=[]
    k=0
    error=tol+1
    #Entra al ciclo hasta que el error sea menor o la tolerancia.
    while  (error>tol):
        #Se calcula el valor de x
        x=a-((f(a))**3)/((f(a+f(a))-f(a))*(f(a)-f(b)))
        #se cambia el valor de a por la nueva x
        a=x
        #calcula una nueva y_k pero ahora con el valor de x
        b=stef(x)
        #se calcula el error
        error = abs(f(x))
        #se aumenta el contador de iteraciones
        k+=1
        #se agrega el error a un vector para graficar luego
        e=e+[error]
        #continua el ciclo
            
    #Grafica el valor de las distintas soluciones
    plt.title('Grafica de errores')
    plt.ylabel('Error')
    plt.xlabel('Iteraciones')
    plt.plot(e,  label='Steff-Sec')
    plt.legend(title='Metodos')
    plt.grid(axis='x', color='0.95')
    plt.grid(axis='y', color='0.95')
    plt.savefig("Graficas.pdf", bbox_inches='tight')
    #El valor de la ultima iteracion se muestra
    print("Steffensen-Secante")
    print("x = ",x)
    print("k = " ,k)
    print("error = ",error)
    print(" ")
#--------------------------------------------------------------------------

#pruebas
#------------------------------------------------------------------------------ 


stef_secant(f,6,pow(10, -10))