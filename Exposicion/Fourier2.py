import numpy as np
import matplotlib.pyplot as plt
import numpy
from math import pi, cos, sin
from scipy.integrate import quad

def f(x):
    """
    Funcion a evaluar en el algoritmo de grafica 
    
    """
    if x > -pi and x < 0:
        return -4
    elif x >= 0 and x <= pi:
        return 2
    else:
        return 0

def fCos(x, n):
    """
    Funcion calcula integral principal x(t) cos (t)
    
    """
    return f(x)*cos((n*2*pi)/T*x)

def fSin(x, n):
    """
    Funcion calcula integral principal x(t) sin (t)

    """
    return f(x)*sin((n*2*pi)/T*x)

def a0():
    """
    Funcion calcula a0 numerico
    
    """
    return (1/T)*(quad(f,-T/2, T/2)[0])

def an(n):
    """
    Funcion calcula an numerico
    
    """
    return (2/T)*(quad(fCos, -T/2, T/2, args=(n), limit=500)[0])

def bn(n):
    """
    Funcion calcula bn numerico
    
    """
    return (2/T)*(quad(fSin, -T/2, T/2, args=(n), limit=500)[0])

def mapInputs(x,n):
    y = []
    for i in range (0, len(x)):
        y.append(fourier(x[i], n))
    return y

def fourier(x, n):
    """
    Funcion principal del programa:
            Datos iniciales x, valores a graficar, iteraciones n
    
    """    
    tmp = 0
    for i in range(1,n):
        if i == 1:
            tmp = a0()
        elif i != n:
            j = i - 1
            tmp += ( anArray[j] * cos(2*j * pi * x / T )) + ( bnArray[j] * sin(2*j * pi * x / T) )

    return tmp


T = 2*pi

anArray = []
bnArray = []

x = numpy.linspace(0,20,3000)

for i in range(0, 1000):
    anArray.append(an(i))
    bnArray.append(bn(i))

plt.figure(num="Serie de Fourier")

for i in range(1, 21):
    plt.title("Iteracion: " + str(i))

    plt.plot(x, mapInputs(x,2*i + 1), "m")
    plt.savefig("fourier.pdf", bbox_inches='tight')   
    plt.pause(0.000001)
    plt.clf()



plt.show()

"""

   ░██████╗██╗███╗░░░███╗██████╗░░█████╗░██╗░░░░░██╗░█████╗░░█████╗░
   ██╔════╝██║████╗░████║██╔══██╗██╔══██╗██║░░░░░██║██╔══██╗██╔══██╗
   ╚█████╗░██║██╔████╔██║██████╦╝██║░░██║██║░░░░░██║██║░░╚═╝██║░░██║   ########
   ░╚═══██╗██║██║╚██╔╝██║██╔══██╗██║░░██║██║░░░░░██║██║░░██╗██║░░██║
   ██████╔╝██║██║░╚═╝░██║██████╦╝╚█████╔╝███████╗██║╚█████╔╝╚█████╔╝
   ╚═════╝░╚═╝╚═╝░░░░░╚═╝╚═════╝░░╚════╝░╚══════╝╚═╝░╚════╝░░╚════╝░
   
"""

from sympy import pi
from sympy import *

def anSymbolic(f, T, a, b):
    """
    Funcion calcula an de manera simbolica (con n)
    
    Input: 
        f: funcion de variable f
        T: Periodo
        a: limite inferior
        b: limite superior
    Output:
        integral presente en an
    """    
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
    """
    Funcion calcula bn de manera simbolica (con n)
    
    Input: 
        f: funcion de variable f
        T: Periodo
        a: limite inferior
        b: limite superior
    Output:
        integral presente en bn
    """       
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
    """
    Funcion calcula a0
    
    Input: 
        f: funcion de variable f
        T: Periodo
        a: limite inferior
        b: limite superior
    Output:
        Valor de a0
    """   
    from sympy import Symbol
    from sympy import integrate
    from sympy import sympify
    Symbol('n')
    t = Symbol('t')   
    
    return integrate(f, (t, a, b), conds='none')/T
  


def main():
    """
    Funcion que realiza las llamadas al simbolico
    
    """   
    Periodo = 2*pi
    
    a01 = Calculo_a0(2,2*pi ,0,pi)
    a02 = Calculo_a0(-4,2*pi,pi,2*pi)    
    an1 = anSymbolic(2, 2 * pi, 0, pi)
    an2 = anSymbolic(-4, 2 * pi, pi, 2 * pi)
    bn1 = bnSymbolic(2, 2 * pi, 0, pi)
    bn2 = bnSymbolic(-4, 2 * pi, pi, 2 * pi)
    a0 = simplify((a01+a02))
    an = simplify((2/Periodo)*(an1+an2))
    bn = simplify((2/Periodo)*(bn1+bn2))
    
    print('a0 = ', a0)
    print('an = ', an)
    print('bn = ', bn)
    
main()
