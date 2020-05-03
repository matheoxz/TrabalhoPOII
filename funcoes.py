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
            #cria dicionario da iteração
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
    return resultados




#print(BuscaUniforme("x^2", 0.2, -1, 1))