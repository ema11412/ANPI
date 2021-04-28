# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 08:08:18 2020

@author: Ema
"""
import  numpy, math     
import numpy as np
from sympy import *


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

def valoresTrigonal(a,b,n,t):
    x=[]
    i=0
    if t==1:
        while i<n:
            x+=[-1]
            i+=1
    else:
        while i<n:
            if i==0:
                x+=[(a/(a-b))]
                i+=1
            elif i==n-1:
                x+=[1]
                i+=1
            else:
                x+=[2]
                i+=1
    return x
    
def Trigonal(a,b,n):
    
    if a==b:
        return "error a debe ser diferente de b"
    if n<3:
        return "error n debe ser mayor o igual a 3"
    diag = valoresTrigonal(a,b,n,2)
    inf = valoresTrigonal(a,b,n,1)
    sup = valoresTrigonal(a,b,n,1)
    M = np.zeros((n,n))
    
    agregarD(M,diag)
    agregarI(M,inf)
    agregarS(M,sup)
    
    return M

def calcular_valP2(n):
    vec = []
    k=1
    while k <= n:    
        rk = ((2*k-1)*np.pi)/(4*n)
        dk = 1/(1-np.cos(2*rk))
        vec += [rk]
        k+=1
    return vec

def calcular_vecP2(n):
    vec = []
    vec_rk = []
    k=1
    while k <= n:    
        rk = ((2*k-1)*np.pi)/(4*n)
        vec_rk += [rk]
        k+=1
    
    for i in vec_rk:
        v_xk = []
        j=1
        while j <= n:
            xk = np.sin((j-1)*i)
            v_xk += [xk]
            j+=1
        vec+=[v_xk]
    
        
    return vec


def matriz(a,b,n):
    
    if a==b:
        return "error a debe ser diferente de b"
    if n<3:
        return "error n debe ser mayor o igual a 3"
    
    M = np.zeros((n,n))
    i=0
    while i<n:
        j=0
        while j<n:
            a1 = a*(i+1)-b
            a2 = a*(j+1)-b
            M[i][j] = min(a1,a2) 
            j+=1
        i+=1

    return M

def v_propios_m1(n):
    if n<3:
        return "error n debe ser mayor o igual a 3"    
    valPropios = calcular_valP2(n)
    vecPropios = np.array(calcular_vecP2(n))
    
    vecPropios = vecPropios.T
    

    return valPropios, vecPropios 
    
x,y = v_propios_m1(10)
print(x)
    
    