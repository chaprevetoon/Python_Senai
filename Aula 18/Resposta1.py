import tkinter as tk
import customtkinter


def somar():
    n1 = float(input_n1.get())
    n2 = float(input_n2.get())
    resultado = n1 + n2
    r.config(text=resultado)

def subt():
    n1 = float(input_n1.get())
    n2 = float(input_n2.get())
    resultado = n1 - n2
    r.config(text=resultado)

def multiplicar():
    n1 = float(input_n1.get())
    n2 = float(input_n2.get())
    resultado = n1 * n2
    r.config(text=resultado)


def dividir():
    n1 = float(input_n1.get())
    n2 = float(input_n2.get())
    resultado = float(n1) / float(n2)
    r.config(text=resultado)            






root  = tk.Tk()
root.geometry('330x500')
root.configure(bg= 'purple')


f  = tk.Frame(root)
f.grid(column=0, columnspan=5, pady=30)

tk.Label(f, text = 'CALCULADORA', font=('lato',15), fg='purple', bg='yellow').grid(row=0, column = 0,  pady=10)

tk.Label(root, text = 'numero 1', font=(15)).grid(row=1, column = 1,  pady=10)
tk.Label(root, text = 'numero 2', font=(15)).grid(row=1, column=3, pady=10)

f  = tk.Frame(root)
f.grid(column=0, columnspan=5, padx=20)
input_n1 = tk.Entry(f)
input_n1.grid(row=2, column=0, padx=10 , pady=10)

input_n2 = tk.Entry(f)
input_n2.grid(row=2, column=1,padx=10, pady=10)


f2 = tk.Frame(root)
f2.grid(column=1, columnspan=3, pady=20)



soma =  tk.Button(f2, text='+', font=(20), command=somar)
soma.grid(row=4, column=1,  padx=5, pady=10,)

sub =  tk.Button(f2, text='-', font=(20), command=subt)
sub.grid(row=4, column=2,  padx=5, pady=10)

mult =  tk.Button(f2, text='x', font=(20), command=multiplicar, )
mult.grid(row=4, column=3,  padx=5, pady=10)

div =  tk.Button(f2, text='/', font=(20),command=dividir,  )
div.grid(row=4, column=4, padx=5, pady=10)

r =  tk.Label(f2, text='=', font=('lato', 15), fg='purple')
r.grid(row=5, column=3, padx=5, pady=10)

btn1 = customtkinter.CTkButton(
    root,
    text='Divisão teste',
    border_color='yellow',
    border_width=5,
    border_spacing=5,
    corner_radius=100,
    text_color = 'purple',
    # bg_color = 'yellow',
    fg_color='yellow',
    hover_color = 'purple', 
    command =    dividir

    )
btn1.grid(row=6, column=1)

root.mainloop()