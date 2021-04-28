# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 11:51:26 2020

@author: Ema
"""
import time
import matplotlib.pyplot as plt
import numpy as np
from numpy import arange
import math
from sympy import *
 

def p1(x):
    f=-1/x
    return f

def q1(x):
    f=1/(4*x**2)-1
    return f

def f1(x):
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
        temp = (h/2)*p(x[i])-1
        S+=[temp]
        i+=1
    return S 

def Inferior(p,h,x):
    #Calcula la parte inferior de la diagonal
    inf=[]
    i=0
    while i<len(x):
        temp = (-h/2)*p(x[i])-1
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
            temp = (-h**2)*f(x[i]) + e0
            vec+= [temp]
            i+=1
        elif i==len(x)-1:
            temp = (-h**2)*f(x[i]) + eN
            vec+= [temp]
            i+=1
        else:
            vec+=[(-h**2)*f(x[i])]
            i+=1
    return vec



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
    plt.show()
    time.sleep(1.5)
    plt.xlabel('$x$') 
    plt.ylabel('$y$') 
    plt.title('Solucion de la ecuacion diferencial') 
    plt.plot(xi, y2,label = "Exacta")
    plt.plot(xk,yk, 'r--',label ="h=0.1")
    plt.plot(xk1,yk1, 'b--',label ="h=0.01")
    plt.plot(xk2,yk2, 'g--',label ="h=0.001")
    plt.plot(xk3,yk3, 'y--',label ="h=10^-5")
    plt.legend(loc="upper right") 
    plt.show()
    time.sleep(5)

def Thomas(p1,q1,f1,h): 
    
    a=1; b=6; y0=1; yn=0;

    #Aca se calcula los valores del vector x
    x1=calcX(a,b,h)
    #Calculamos la diagonal de la matriz
    b   = Diagonal(q1,h,x1)
    #Calculamos el valor de la parte inferior de la matriz
    a = Inferior(p1,h,x1)
    #Calculamos el valor de la parte superior de la matriz
    c = Superior(p1,h,x1)
    #Calculamos el vector b que cumple la igualdad Ay=b
    d  = vecB(p1,f1,h,y0,yn,x1)
    

    n=np.shape(a)[0]  
 
    p = np.zeros(n) 
    q = np.zeros(n) 
    x  = np.zeros(n)  
 
    p[0]=c[0]/b[0]  
    for i in range(1,n-1,1):  
       p[i]=c[i]/(b[i]-a[i]*p[i-1])  
    
    
    q[0]=d[0]/b[0]  
    for i in range(1,n,1):  
       q[i]=(d[i]-a[i]*q[i-1])/(b[i]-a[i]*p[i-1])  


    x[n-1]=q[n-1]  
    for i in range(n-2,-1,-1):  
       x[i]=q[i]-p[i]*x[i+1]  
 
    return x1,x  

xk,yk = Thomas(p1,q1,f1,0.1);
xk1,yk1 = Thomas(p1,q1,f1,0.01);
xk2,yk2 = Thomas(p1,q1,f1,0.001);
xk3,yk3 = Thomas(p1,q1,f1,0.000001);

graficar()