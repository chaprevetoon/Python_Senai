import tkinter as tk




def display_pack():
    texto = input_.get()
    mostra_text.config(text=texto)

def display_grid():
    texto = input_.get()
    mostra_text.config(text=texto)



janela  =  tk.Tk()
janela.geometry('700x300')
janela.title('DISPLAY Pack')
janela.configure(bg = "white")


# pack() / # grid() / # place() / escolha um dos 3

# Exemplo com pack

texto = tk.Label(janela, text ='Isso é um texto', background='black', font=('Lao UI', 30), fg="white")
texto.pack(pady=10)


input_ = tk.Entry(janela,  font=(30), fg='purple')
input_.pack(pady=30)



btn = tk.Button(janela, text='Mostre o texto', font=(25), fg='white', bg='black', command=display_pack)
btn.pack(pady=20)



mostra_text = tk.Label(janela, text='')
mostra_text.pack(pady=20)
janela.bind("<Return>", lambda event: display_pack())




janela.mainloop()

# Exemplo com grid 

mostra_text1 = tk.Label(janela, text=' FKSDLFKÇLSDFK', fg='BLACK', bg='black', font=('arial', 15))
mostra_text1.grid(row=3, column=0, padx=10, pady=10)

texto = tk.Label(janela, text ='Isso é um texto', font=('arial', 20), fg="black", bg='white')
texto.grid(row=0, column=1, padx=10)

input_ = tk.Entry(janela,   fg='white',font=('arial',15), bg='black')
input_.grid(row=1, column=1, padx=10, pady=10)
# input_.bind("<Return>")


btn = tk.Button(janela, text='Mostre o texto', font=('arial',20), fg='yellow', bg='black', command=display_grid)
btn.grid(row=2, column=1, padx=10, pady=10)
janela.bind("<Return>", lambda event: display_grid())




mostra_text = tk.Label(janela, text='', fg='white', bg='black', font=('arial', 15))
mostra_text.grid(row=3, column=1, padx=10)



janela.mainloop()

# Place é pouco usado.