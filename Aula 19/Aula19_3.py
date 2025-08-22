import sqlite3
import tkinter as tk
from tkinter import messagebox


def conexao():
    conn =  sqlite3.connect('database.db')
    return conn


def criar_table():
    conex = conexao()
    c = conex.cursor()
    
    c.execute('''
      CREATE TABLE IF NOT EXISTS dados(
          cpf TEXT NOT NULL,
          email TEXT NOT NULL,
          nome TEXT NOT NULL            
        )''')
    conex.commit()
    conex.close()


# inserindo os dados 
def inserir_dados():
    # capturando do input do tkinter 
    # atribuindo a variaveis locais 
    nome  =  nome_input.get()
    cpf = CPF_input.get()
    email = email_input.get()

    # se existir todos os inputs
    if nome and cpf and email:
       conex = conexao()
       c = conex.cursor()
       c.execute('INSERT INTO dados (cpf, email, nome)values(?,?,?)', (cpf,email,nome))
       conex.commit()
       conex.close()
       # enquanto não clicar na caixa de mensagem não apaga
       messagebox.showinfo('Show', 'DADOS INSERIDOS COM SUCESSO!')
       # apaga os valores iseridos na tabela
       nome_input.delete(0,tk.END) #tk.END é o ultimo caracater digitado
       email_input.delete(0,tk.END)
       CPF_input.delete(0,tk.END)    
        
    else:
        # caso um dos inputs não estejam preenchidos 
        messagebox.showerror('erro',  'Preencha os dados corretamente!!')






root =  tk.Tk()

nome_label = tk.Label(root, text='Nome', font = (70))
nome_label.pack()

nome_input = tk.Entry(root, font=70)
nome_input.pack()

CPF_label = tk.Label(root, text='CPF', font = (70))
CPF_label.pack()

CPF_input = tk.Entry(root, font=70)
CPF_input.pack()

email_label = tk.Label(root, text='E - mail', font = (70))
email_label.pack()

email_input = tk.Entry(root, font=70)
email_input.pack()


btn = tk.Button(root,text='Criar_Tabela', command=criar_table, width=30)
btn.pack(pady=20)

btn_inserir_ = tk.Button(root,text='iNSERIR DADOS', command=inserir_dados, width=30)
btn_inserir_.pack(pady=20)


root.mainloop()