from scipy import integrate
import matplotlib.pyplot as plt
import numpy as np
from math import sin, cos




def fourier(f, n,T):
    t1=-T/2
    t2= T/2
    a = []
    b = []
    time = np.linspace(t1, t2, 100)
    a0 = (integrate.quad(f, t1, t2)[0])/(2*np.pi)
    for i in range(n):
        fc = lambda x: f(x) * cos((i+1) * x)
        fs = lambda x: f(x) * sin((i+1) * x)
        a.append((1 / T) * integrate.quad(fc, t1, t2)[0])
        b.append((1 / T) * integrate.quad(fs, t1, t2)[0])
    func = [np.array([a[k]*np.cos((k+1)*x) + b[k]*np.sin((k+1)*x) for k in range(0, len(a))]).sum() + a0 for x in time]
    plt.plot(time, func)
    plt.xlabel("$x$")
    plt.ylabel("$y$")
    plt.title("Aproximacion de Fourier")
    plt.show()
    


g = lambda x: x-x**2

k=1
n=20
while k<=n: 
    fourier(g, k,2)
    k+=1