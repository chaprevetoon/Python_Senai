import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def conectar():
    conn = sqlite3.connect('myDataBase.db')
    return conn

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
       CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY NOT NULL,
        nome TEXT NOT NULL,
        idade INTEGER                                          
       )  
   ''')
    conn.commit()
    conn.close()

def inserir_usuarios():
    nome  = entry_nome.get()
    idade = entry_idade.get()
    entr_id = entry_id.get()
    

    if nome and idade:
        conn = conectar()
        c = conn.cursor()    
        c.execute('INSERT INTO usuarios (id, nome, idade) VALUES (?,?,?) ', (entr_id,nome, idade))
        conn.commit()
        conn.close()
        messagebox.showinfo('Sucesso', 'Dados inseridos!')
        entry_nome.delete(0,tk.END)
        entry_idade.delete(0,tk.END)
        entry_id.delete(0,tk.END)
        mostrar_usuarios()
    else:
        messagebox.showerror('Erro','Preencha corretamente!')    

def mostrar_usuarios():
    for row in tree.get_children():
        tree.delete(row)
    conn = conectar()
    c = conn.cursor()
    c.execute('SELECT * FROM usuarios')
    usuarios  =  c.fetchall()
    for usuario in usuarios:
        tree.insert("","end", values = (usuario[0], usuario[1], usuario[2]))
    conn.close()        


def eliminar_():
    selecao = tree.selection()
    if selecao:
        user_id = tree.item(selecao)['values'][0]
        conn = conectar()
        c = conn.cursor()
        c.execute('DELETE FROM usuarios WHERE id = ? ', (user_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo('Efetuado', 'Dados deletados!')
        mostrar_usuarios()
    else:
        messagebox.showinfo('Erro', 'Selecione corretamente')    

def atualizar():
    selecao = tree.selection()
    if selecao:
       user_id = tree.item(selecao)['values'][0]
       nome  = entry_nome.get()
       idade = entry_idade.get()
       

       if nome and idade:
          conn = conectar()
          c = conn.cursor()    
          c.execute('UPDATE usuarios SET  nome = ?, idade = ? WHERE id = ?',(nome, idade, user_id))
          conn.commit()
          conn.close()
          messagebox.showinfo('Dados', 'Atualização funcionou!')
          mostrar_usuarios()
       else:
           messagebox.showerror('Erro', 'Dados não foram atualizados!') 
    else:
        messagebox.showwarning('Atenção', 'Selecione corretamente') 




janela = tk.Tk()
janela.title('CRUD COM TKINTER E SQLITE 3')
# janela.geometry('250x430')

label_nome = tk.Label(janela, text = 'Nome', font=(30))
label_nome.grid()

entry_nome = tk.Entry(janela, font=(30))
entry_nome.grid()


label_idade = tk.Label(janela, text = 'idade', font=(30))
label_idade.grid()

entry_idade = tk.Entry(janela, font=(30))
entry_idade.grid()


label_id = tk.Label(janela, text = 'CPF', font=(30))
label_id.grid()

entry_id = tk.Entry(janela, font=(30))
entry_id.grid()


btn_salvar = tk.Button(janela, text='salvar', font=(30), command=inserir_usuarios)
btn_salvar.grid()

btn_deletar = tk.Button(janela, text='deletar', font=(30), command=eliminar_)
btn_deletar.grid()

btn_atualizar = tk.Button(janela, text='atualizar', font=(30), command=atualizar)
btn_atualizar.grid()



collumns = ('ID', 'NOME', 'IDADE')

tree = ttk.Treeview(janela, columns= collumns, show='headings')
tree.grid(row=10, column=0, columnspan=2)

for col in collumns:
    tree.heading(col, text=col)

criar_tabela()
mostrar_usuarios()


janela.mainloop()