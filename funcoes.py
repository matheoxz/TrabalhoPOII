from tkinter import *
from tkinter import messagebox
import fourFn
import sys

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


#print(BuscaUniforme("x^2", 0.2, -1, 1))
#print(BuscaDicotomica("x^2", 0.1, -1, 1, 0.01))