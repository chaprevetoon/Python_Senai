import tkinter as tk

def soma():
    try:
        n1 = float(entry1.get())  #entry.get = input só que para o tkinter
        n2 = float(entry2.get())
        res = n1 + n2
        resultado_label.config(text=f'Resultado: {res}')
    except ValueError:
        resultado_label.config(text='Erro: entrada inválida')

def subtrair():
    try:
        n1 = float(entry1.get())
        n2 = float(entry2.get())
        res = n1 - n2
        resultado_label.config(text=f'Resultado: {res}')
    except ValueError:
        resultado_label.config(text='Erro: entrada inválida')

def multiplicar():
    try:
        n1 = float(entry1.get())
        n2 = float(entry2.get())
        res = n1 * n2
        resultado_label.config(text=f'Resultado: {res}')
    except ValueError:
        resultado_label.config(text='Erro: entrada inválida')

def dividir():
    try:
        n1 = float(entry1.get())
        n2 = float(entry2.get())
        if n2 == 0:
            resultado_label.config(text='Erro: divisão por zero')
        else:
            res = n1 / n2
            resultado_label.config(text=f'Resultado: {res}')
    except ValueError:
        resultado_label.config(text='Erro: entrada inválida')

janela = tk.Tk()
janela.title('Calculadora')
janela.geometry('300x250')

entry1 = tk.Entry(janela, width=10)
entry1.grid(row=0, column=0, padx=10, pady=10)

entry2 = tk.Entry(janela, width=10)
entry2.grid(row=0, column=1, padx=10, pady=10)

btn_soma = tk.Button(janela, text='+', width=5, command=soma)
btn_soma.grid(row=1, column=0, padx=5, pady=5)

btn_sub = tk.Button(janela, text='-', width=5, command=subtrair)
btn_sub.grid(row=1, column=1, padx=5, pady=5)

btn_mult = tk.Button(janela, text='*', width=5, command=multiplicar)
btn_mult.grid(row=1, column=2, padx=5, pady=5)

btn_div = tk.Button(janela, text='/', width=5, command=dividir)
btn_div.grid(row=1, column=3, padx=5, pady=5)

resultado_label = tk.Label(janela, text='Resultado:', fg='blue')
resultado_label.grid(row=2, column=0, columnspan=4, pady=20)

janela.bind('<Return>', soma)

janela.mainloop()
