from tkinter import *
from tkinter import messagebox
import fourFn
import sys
import numpy as np
import sympy as sympy
import math

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
    dic = ["-"]
    if(ep < 0.7):
        #valores de epsilon muito pequenos fazem muitas iterações e travam a execução
        ep = 0.7
    k = 1
    resultados=[]
    while((b-a) >= ep):
        x = ((a+b)/2)-d
        z = ((a+b)/2)+d
        fx = fourFn.strToFunc(f.replace("x", str(x))) 
        fz = fourFn.strToFunc(f.replace("x", str(z)))
        dic = [k, a, b, (b-a), x, z, fx, fz, (fx>fz)]
        resultados.append(dic)
        if(fx > fz):
            a = x
        else:
            b = z
        k+=1
        dic = [k, a, b, (b-a)]
    resultados.append(dic)
    resultados.append("x* = "+str((a+b)/2))
    return resultados

def SecaoAurea(f, a, b, ep):
    k = 1
    resultados = []
    ap = ["-"]
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
        ap = [k, a, b, (b-a)]
    resultados.append(ap)
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
    ap = ["-"]
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
        k+=1
        ap = [k, a, b, (b-a)]
       # print(ap)
        
    resultados.append(ap)
    resultados.append("n = " + str(n))
    resultados.append("F[ ] = " + str(fib))
    resultados.append("x* = " + str((a+b)/2))
    return resultados

def DerPrim(f):
    func_d1 = sympy.diff(f)
    f1 = str(func_d1)
    f1 = f1.replace("**", "^")
    f1 = f1.replace("exp", "e^")
    f1 = f1.replace(" ", "")
    return f1

def DerSeg(f):
    f = f.replace('e', 'E')
    f1 = DerPrim(f)
    f1 = str(f1)
    f1 = f1.replace("**", "^")
    f1 = f1.replace("exp", "e^")
    f1 = f1.replace(" ", "")
    f1 = f1.replace('e', 'E')
    func_d2 = sympy.diff(f1)
    f2 = str(func_d2)
    f2 = f2.replace("**", "^")
    f2 = f2.replace("exp", "e^")
    f2 = f2.replace(" ", "")
    return str(f2)

def Bissecao(f, a, b, ep):
    #calcula n iterações
    N=math.ceil(math.log(1/(ep/(b-a)),2))

    #inicia variáveis e vetor de resultados
    k=1
    ver = 'F'
    resultados = []
    ap = ["-"]

    #faz derivada e trata string
    f=f.replace("e", "E")
    f1=DerPrim(f)

    #calcula valor da derivada
    sf1 = fourFn.strToFunc(f1.replace('x', str((a+b)/2)))
    
    #começa iterações
    while(k<=N and sf1>10**(-10)):
        x=(a+b)/2
        sf1=fourFn.strToFunc(f1.replace("x", str(x)))
        if(sf1<0):
            a=x
            ver='F'
        elif(sf1>0):
            b=x
            ver='V'
        elif(sf1==0):
            ver='F'
        ap=[k, a, b, x, sf1, ver]
        resultados.append(ap)
        k+=1
    x=(a+b)/2
    ap=[k, a, b, x, sf1, ver]
    resultados.append(ap)
    resultados.append("N = " + str(N)+"  f'(x)= " + f1) 
    resultados.append("x* = " + str(x))
    return resultados

def max(x,y):
    if (x>y):
        return x
    else:
        return y
    
def Newton(f, a, ep):
    #inicia variaveis
    x=a
    k=1
    resultados = []
    condicao1 = True
    condicao2 = True

    f = f.replace("e", "E")
    f1 = DerPrim(f)
    sf1 = fourFn.strToFunc(f1.replace('x', '(' + str(x)+ ')'))

    f2 = DerSeg(f)
    sf2=fourFn.strToFunc(f2.replace('x', '(' + str(x) + ')'))
    
    if(abs(sf1)<ep):
        ap=[k, x, sf1, "-", "-", "-"]
        resultados.append(ap)
        resultados.append("f'(x)= " + str(sf1))
        resultados.append("x* = " + str(x))
        return resultados
    else: 
        while (condicao1 and condicao2 ):
            sf2=fourFn.strToFunc(f2.replace('x', str(x)))
            xp=x-sf1/sf2 
            if(sf2>10**(-10)):
                sf1=fourFn.strToFunc(f1.replace('x', str(xp)))
                sf2=fourFn.strToFunc(f2.replace('x', str(xp)))
                if(abs(sf1)>ep):
                    condicao1 = True
                    if((abs(xp-x)/max(sf2,1))>ep):
                        condicao2=True
                else:
                    condicao1=False
                    condicao2='-'
            x=xp
            ap=[k, x, sf1, sf2, condicao1, condicao2]
            resultados.append(ap)
            #if not (condicao1=='V' and condicao2=='V')
                   #break
            k+=1
            if(k > 50):
                break
        resultados.append("f'(x)= " + f1 + "f''(x)= " + f2)
        resultados.append("x* = " + str(x))
        return resultados



#print(BuscaUniforme("x^2", 0.2, -1, 1))
#print(BuscaDicotomica("x^2", 0.1, -1, 1, 0.01))
#print(SecaoAurea("x^2", -1, 1, 0.1))
#print(fibonacci(6))
#print(SecaoFibonacci("x^2", -5, 5, 0.1))