# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 16:14:26 2020

@author: Kevin
"""
from sympy import pi
from sympy import *

def anSymbolic(f, T, a, b):
    
    from sympy import Symbol
    from sympy import integrate
    from sympy import sympify
    
    Symbol('n')
    t = Symbol('t')
    
    Tresp = T
    
    T = Symbol('T')
    
    fcos = 'cos(n * t * 2 * pi / T)'
    fcos = sympify(fcos)
    
    fcos = fcos.subs({'T': Tresp})
    fcos = f * fcos
    
    return integrate(fcos, (t, a, b), conds='none')


def bnSymbolic(f, T, a, b):
    
    from sympy import Symbol
    from sympy import integrate
    from sympy import sympify
    
    Symbol('n')
    t = Symbol('t')
    
    Tresp = T
    
    T = Symbol('T')
    
    fsen = 'sin(n * t * 2 * pi / T)'
    fsen = sympify(fsen)
    
    fsen = fsen.subs({'T': Tresp})

    fsen = f * fsen

    return integrate(fsen, (t, a, b), conds='none')



def Calculo_a0(f,T , a, b):
    from sympy import Symbol
    from sympy import integrate
    from sympy import sympify
    Symbol('n')
    t = Symbol('t')   
    
    return integrate(f, (t, a, b), conds='none')/T
  
a01 = Calculo_a0(2,2*pi ,0,pi)
a02 = Calculo_a0(-4,2*pi,pi,2*pi)    
an1 = anSymbolic(2, 2 * pi, 0, pi)
an2 = anSymbolic(-4, 2 * pi, pi, 2 * pi)
bn1 = bnSymbolic(2, 2 * pi, 0, pi)
bn2 = bnSymbolic(-4, 2 * pi, pi, 2 * pi)


def main():
    Periodo = 2*pi
    
    a0 = simplify((a01+a02))
    an = simplify((2/Periodo)*(an1+an2))
    bn = simplify((2/Periodo)*(an1+an2))
    
    print('a0 = ', a0)
    print('an = ', an)
    print('bn = ', bn)