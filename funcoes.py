from tkinter import *
from tkinter import messagebox
import fourFn
import sys
import numpy as np

def BuscaUniforme(f, d, a, b):
    #inicia variaveis
    x = a
    xk = a
    k = 1
    ref = True
    resultados = []
    #inicia algoritmo
    fa = f.replace("x", str(x))
    fxk = fourFn.strToFunc(fa)
    #busca uniforme
    while(xk < b):
        try:
            xa = x
            x = xk
            xk += d
            fa = f.replace("x", str(xk))
            fx = fxk
            fxk = fourFn.strToFunc(fa)
            #print("x: " + str(x) + "xk: " + str(xk)+ "fx: " +str(fx) + "fxk: " + str(fxk))
        except Exception as e:
            messagebox.showwarning("Erro", e)
        else:
            dicit = [k, x, fx, xk, fxk, (fxk<fx)]
            resultados.append(dicit)

            if(not (fxk<fx) and not ref):
                xk = b
            if(not (fxk<fx) and ref):
                resultados.append("REFINAMENTO")
                d /= 10
                b = xk
                xk = xa 
                k = 0
                ref = False
                fa = f.replace("x", str(x))
                res = fourFn.strToFunc(fa)
        k += 1
    resultados.append("x* = " + str(x))
    return resultados

def BuscaDicotomica(f, d, a, b, ep):
    k = 1
    resultados=[]
    while((b-a) >= ep):
        x = ((a+b)/2)-d
        z = ((a+b)/2)+d
        fx = fourFn.strToFunc(f.replace("x", str(x))) 
        fz = fourFn.strToFunc(f.replace("x", str(z)))
        dic = [a, b, x, z, fx, fz, (fx>fz), (b-a)]
        resultados.append(dic)
        if(fx > fz):
            a = x
        else:
            b = z
        k+=1
    resultados.append("x* = "+str((a+b)/2))
    return resultados

def SecaoAurea(f, a, b, ep):
    k = 1
    resultados = []
    alpha = (-1+np.sqrt(5))/2
    beta = 1-alpha
    micra = a + beta*(b-a)
    labda = a + alpha*(b-a)
    while((b-a) >= ep):
        fu = fourFn.strToFunc(f.replace("x", str(micra)))
        fl = fourFn.strToFunc(f.replace("x", str(labda)))
        ap = [k, a, b, (b-a), micra, labda, fu, fl]
       # print(ap)
        if(fu > fl):
            a = micra
            micra = labda
            labda = a + alpha*(b-a)
            ap.append(">")
        elif(fu <= fl):
            b = labda
            labda = micra
            micra = a + beta*(b-a)
            ap.append("<")
        resultados.append(ap)
       # print(ap)
        k+=1
    resultados.append("x* = " + str((a+b)/2))
    return resultados

def fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        #print(n)
        return fibonacci(n-1) + fibonacci(n-2)

def SecaoFibonacci(f, a, b, ep):
    n = 0
    MaxIt = int((b-a)/ep)
    #print("max: " + str(MaxIt))
    fib = [0]
    while(fib[n] < MaxIt):
        fib.append(fibonacci(n))
        n += 1
    fib.remove(0)
    n-=1
    #print(fib)
    k = 0
    resultados = []

    while((b-a) >= ep):
        micra = a + (fib[n-k-2]/fib[n-k])*(b-a)
        labda = a + (fib[n-k-1]/fib[n-k])*(b-a)
        fu = fourFn.strToFunc(f.replace("x", str(micra)))
        fl = fourFn.strToFunc(f.replace("x", str(labda)))
        ap = [k, a, b, (b-a), micra, labda, fu, fl]

       # print(ap)
        if(fu > fl):
            a = micra
            micra = labda
            labda = a + (fib[n-k-1]/fib[n-k])*(b-a)
            ap.append(">")
        elif(fu <= fl):
            b = labda
            labda = micra
            micra = a + (fib[n-k-2]/fib[n-k])*(b-a)
            ap.append("<")
        resultados.append(ap)
       # print(ap)
        k+=1
    resultados.append("n = " + str(n))
    resultados.append("F[ ] = " + str(fib))
    resultados.append("x* = " + str((a+b)/2))
    return resultados



#print(BuscaUniforme("x^2", 0.2, -1, 1))
#print(BuscaDicotomica("x^2", 0.1, -1, 1, 0.01))
#print(SecaoAurea("x^2", -1, 1, 0.1))
#print(fibonacci(6))
#print(SecaoFibonacci("x^2", -5, 5, 0.1))