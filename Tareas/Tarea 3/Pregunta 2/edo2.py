import time
import matplotlib.pyplot as plt
import numpy as np
from numpy import arange
import math
from sympy import *


 
def p(x):
    p=-1/x
    return p

def q(x):
    q=1/(4*x**2)-1
    return q

def f(x):
    f=0
    return f




def calcX(a,b,h):
    #Calcula el vector x
    i=1
    vec=[]
    k=a+h
    while k<b:
        vec += [a+i*h]
        k=k+h
        i+=1
    return vec

def Diagonal(q,h,x):
    #Calcula la diagonal
    d=[]
    for i in x:
        temp = 2+(h**2)*q(i)
        d+=[temp]
    return d

def Superior(p,h,x):
    #Calcula la parte superior de la diagonal
    S=[]
    i=0
    while i<len(x):
        temp = ((h/2)*p(x[i])-1)
        S+=[temp]
        i+=1
    return S 

def Inferior(p,h,x):
    #Calcula la parte inferior de la diagonal
    inf=[]
    i=0
    while i<len(x):
        temp = ((-1*h/2)*p(x[i])-1)
        inf+=[temp]
        i+=1
    return inf 

def vecB(p,f,h,y0,yn,x):
    #Calcula el vector vB
    vec=[]
    e0 = ((h/2)*p(x[0])+1)*y0
    eN = ((-h/2)*p(x[-1])+1)*yn
    
    i=0
    while i<len(x):
        if i==0:
            temp = (-1*h**2)*f(x[i]) + e0
            vec+= [temp]
            i+=1
        elif i==len(x)-1:
            temp = (-1*h**2)*f(x[i]) + eN
            vec+= [temp]
            i+=1
        else:
            vec+=[(-1*h**2)*f(x[i])]
            i+=1
    return vec


def agregarD(M,x):
    #Agrega diagonal a matriz
    i=0
    while i<len(M):
        j=0
        while j<len(M):
            if i==j:
                M[i][j] = x[j]
            j+=1
        i+=1
                
    return M

def agregarI(M,x):
    #Agrega parte inferior de la diagonal
    i=1
    while i<len(M):
        j=0
        if i==len(M)-1:

            M[i][i-1]=x[-2]
        while j<len(M)-1:
            if i==j:
                M[i][j-1] = x[j-1]
            j+=1
        i+=1
    return M

def agregarS(M,x):
    #Agrega parte superior de la diagonal
    i=0
    while i<len(M):
        j=0
        while j<len(M)-1:
            if i==j:
                M[i][j+1] = x[j+1]
            j+=1
        i+=1
    return M

def graficar():
    '''
    
    Esta funcion grafica las distintas aproximaciones y a su vez la solucion exacta
    
    '''
    plt.xlabel('$x$') 
    plt.ylabel('$y$') 
    plt.title('Solucion de la ecuacion diferencial') 
    plt.show()
    time.sleep(1.5)
    xi = arange(1, 6,0.01)
    y2 = (np.sin(6)*np.cos(xi) - np.cos(6)*np.sin(xi))/(np.sin(5)*(np.sqrt(xi)))
    plt.xlabel('$x$') 
    plt.ylabel('$y$') 
    plt.title('Solucion de la ecuacion diferencial') 
    plt.plot(xi, y2,label = "Exacta")
    plt.show()
    time.sleep(4)
    plt.xlabel('$x$') 
    plt.ylabel('$y$') 
    plt.title('Solucion de la ecuacion diferencial') 
    plt.plot(xi, y2,label = "Exacta")
    plt.plot(xk,yk, 'r--',label ="h=0.1")
    plt.show()
    time.sleep(1.5)
    plt.xlabel('$x$') 
    plt.ylabel('$y$') 
    plt.title('Solucion de la ecuacion diferencial') 
    plt.plot(xi, y2,label = "Exacta")
    plt.plot(xk,yk, 'r--',label ="h=0.1")
    plt.plot(xk1,yk1, 'b--',label ="h=0.01")
    plt.show()
    time.sleep(1.5)
    plt.xlabel('$x$') 
    plt.ylabel('$y$') 
    plt.title('Solucion de la ecuacion diferencial') 
    plt.plot(xi, y2,label = "Exacta")
    plt.plot(xk,yk, 'r--',label ="h=0.1")
    plt.plot(xk1,yk1, 'b--',label ="h=0.01")
    plt.plot(xk2,yk2, 'g--',label ="h=0.001")
    plt.legend(loc="upper right") 
    plt.show()
    time.sleep(5)



def edo2(p,q,f,h0,a,b,y0,yn):
    '''
    edo2: 
          Solucion de una ecuacion diferencial de 2do orden por el metodo
          de diferencias finitas.
          Forma matematica:
              y'' = py'+qy+f
              
    Sintxis:
          edo2(p,q,f,h,a,b,y0,yn);
          
    Valores de entrada:
          Funciones p(x), q(x) y f(x) las cuales conforman la ecuacion diferencial
          h: valor del paso
          a, b: extremos del intervalo donde se desea aproximar la solucion
          y0 , yn: Valores de los intervalos y0=y(a), yn=y(b)
          
    Valores de salida:
          Vectores x,y los cuales corresponden a los pares ordenados de la siguiente manera
          x=[x0,x1,x2,....,xn]
          y=[y0,y1,y2,....,yn]
          Pares -> (x0,y0),(x1,y1),(x2,y2),....,(xn,yn)
    
    Concideraciones:
          Se calcula mediante la solucion de una matriz trigonal, -ejemplo 3x3-
              [[a,b,0]
               [c,d,e]
               [0,g,h]
              ]
          La diagonal seria [a,d,h], la parte inferior de lka diagonal [c,d] y superior [b,e]
    '''
    #Aca se calcula los valores del vector x
    h=h0
    
    x=calcX(a,b,h)
    
    D = Diagonal(q,h,x)
    S = Superior(p,h,x)
    I = Inferior(p,h,x)
    
    matriz = np.zeros((len(D),len(D)))
    
    b = vecB(p,f,h,y0,yn,x)
    
    #agregamos los elementos a la matriz
    agregarD(matriz,D)
    agregarI(matriz,I)
    agregarS(matriz,S)
    
    #Resolvemos el sistema de la forma matriz*y=vB
    y=np.linalg.solve(matriz,b)
    #Agregamos los valores a y b
    x= x 
    #y=y.tolist()
    #Agregamos los valores y0, y0
    y= y 

    #Retornamos la solucion
    return x,y

a=1; b=6; h=0.1; y0=1; yn=0;
h1=0.01; h2=0.001; h3=0.0001;


xk,yk = edo2(p,q,f,h,a,b,y0,yn)
#xk1,yk1 = edo2(p,q,f,h1,a,b,y0,yn)
#xk2,yk2 = edo2(p,q,f,h2,a,b,y0,yn)

print(xk)
print(yk)

#graficar()
