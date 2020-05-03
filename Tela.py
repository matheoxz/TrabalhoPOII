from tkinter import *
from tkinter import messagebox
import fourFn
import funcoes

def Click():
    try:
        f = funcao.get()
        d = float(delta.get())
        a = float(aEntry.get())
        b = float(bEntry.get())
        op = optionVar.get()
    except Exception as e:
        messagebox.showwarning("Erro", "Coloque todos os valores nos campos!")
    else:
        #abre nova janela
        resW = Toplevel()
        resW.title("Resultado")

        if( op == 0):
            #poe haders da tabela
            Label(resW, text = "k").grid(row = 0, column = 0)
            Label(resW, text = "x").grid(row = 0, column = 1)
            Label(resW, text= "f(x)").grid(row = 0, column = 2)
            Label(resW, text= "xk").grid(row = 0, column = 3)
            Label(resW, text= "f(xk)").grid(row = 0, column = 4)
            Label(resW, text= "f(xk) < f(x)?").grid(row = 0, column = 5)
            #executa funcao
            lista = funcoes.BuscaUniforme(f, d, a, b)
            r = 1
            c = 0
            for i in lista:
                if (i == "REFINAMENTO"):
                    Label(resW, text = i).grid(row = r, column = c)
                    r+=1
                    continue
                for j in i:
                    Label(resW, text = str(j)).grid(row = r, column = c)
                    c+=1
                c=0
                r+=1





root = Tk()
root.title("Trabalho 1")
#frames
optionsF = LabelFrame(root, text="Opções", )
dataF = LabelFrame(root, text="Dados")
#Variaveis
optionVar = IntVar()
graficoVar = IntVar()
#Radio Buttons
uniformeRB = Radiobutton(optionsF, text="Busca Uniforme", variable = optionVar, value = 0)
dicotomicaRB = Radiobutton(optionsF, text="Busca Dicotômica", variable = optionVar, value = 1)
aureaRB = Radiobutton(optionsF, text="Seçã Áurea", variable = optionVar, value = 2)
fibonacciRB = Radiobutton(optionsF, text="Busca de Fibonacci", variable = optionVar, value = 3)
bissecaoRB = Radiobutton(optionsF, text="Bisseção", variable = optionVar, value = 4)
newtonRB = Radiobutton(optionsF, text="Newton", variable = optionVar, value = 5)
#CheckBox
graficoCB = Checkbutton(root, text="Gerar Gráfico", variable = graficoVar)
#Entradas
funcao = Entry(dataF)
funcao.insert(0, "e^x-x^3+1")
delta = Entry(dataF)
delta.insert(0, "0.35")
aEntry = Entry(dataF, width=5)
aEntry.insert(0, "-1")
bEntry = Entry(dataF, width = 5)
bEntry.insert(0, "6")
#Botoes
botao = Button(root, text = "Calcular!", command = Click).grid(row= 6, column = 1, sticky = W+E)


#Inserções na tela
#Labels
funcaoLabel = Label(dataF, text = "min f(x) = ").grid(row= 1, column = 1)
deltaLabel = Label(dataF, text = "Δ = ").grid(row= 2, column = 1)
saLabel = Label(dataF, text = "s. a: { ").grid(row= 5, column= 1)
xLabel = Label(dataF, text = "≤x≤").grid(row= 5, column = 3)
#Entrys
funcao.grid(row = 1, column= 2, sticky=W+E, columnspan = 3)
delta.grid(row = 2, column= 2, sticky=W+E, columnspan = 3)
aEntry.grid(row= 5, column = 2, sticky=W+E)
bEntry.grid(row= 5, column = 4, sticky=W+E)
#Radio Buttons
uniformeRB.grid(row= 1, column= 3)
dicotomicaRB.grid(row= 2, column= 3)
aureaRB.grid(row= 3, column=3)
fibonacciRB.grid(row= 1, column=4)
bissecaoRB.grid(row=2, column=4)
newtonRB.grid(row=3, column=4)
#Frames
dataF.grid(row=0, column=0, sticky= W+E+N+S)
optionsF.grid(row=0, column=1, sticky= W+E+N+S)
#CheckButton
graficoCB.grid(row=6, column=0, sticky=W)


root.mainloop()