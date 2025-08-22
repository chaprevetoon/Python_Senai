import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


def IMC():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        if altura == 0:
            resultado_label.config(text='Erro: divisão por zero')
        else:
            imc = peso / (altura ** 2)
            resultado_label.config(text=f'Resultado: {imc:.2f}')
    except ValueError:
        resultado_label.config(text='Erro: entrada inválida')


def conectar():
    conn = sqlite3.connect('Banco_Avaliação.db')
    return conn


def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
       CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY NOT NULL,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        peso REAL NOT NULL,
        altura REAL NOT NULL,
        imc REAL NOT NULL         
       )  
   ''')
    conn.commit()
    conn.close()


def inserir_usuarios():
    nome = entry_nome.get()
    idade = entry_idade.get()
    peso = entry_peso.get()
    altura = entry_altura.get()
    entr_id = entry_id.get()

    if nome and idade and peso and altura and entr_id:
        try:
            peso = float(peso)
            altura = float(altura)
            imc = peso / (altura ** 2)
        except ValueError:
            messagebox.showerror('Erro', 'Peso ou altura inválidos!')
            return

        conn = conectar()
        c = conn.cursor()
        c.execute('INSERT INTO usuarios (id, nome, idade, peso, altura, imc) VALUES (?,?,?,?,?,?)',
                  (entr_id, nome, idade, peso, altura, imc))
        conn.commit()
        conn.close()
        messagebox.showinfo('Sucesso', 'Dados inseridos!')

        entry_nome.delete(0, tk.END)
        entry_idade.delete(0, tk.END)
        entry_peso.delete(0, tk.END)
        entry_altura.delete(0, tk.END)
        entry_id.delete(0, tk.END)
        resultado_label.config(text='Resultado:')
        mostrar_usuarios()
    else:
        messagebox.showerror('Erro', 'Preencha todos os campos!')


def mostrar_usuarios():
    for row in tree.get_children():
        tree.delete(row)
    conn = conectar()
    c = conn.cursor()
    c.execute('SELECT * FROM usuarios')
    usuarios = c.fetchall()
    for usuario in usuarios:
        tree.insert("", "end", values=(usuario[0], usuario[1], usuario[2], usuario[3], usuario[4], f"{usuario[5]:.2f}"))
    conn.close()


def eliminar_():
    selecao = tree.selection()
    if selecao:
        user_id = tree.item(selecao)['values'][0]
        conn = conectar()
        c = conn.cursor()
        c.execute('DELETE FROM usuarios WHERE id = ?', (user_id,))
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
        nome = entry_nome.get()
        idade = entry_idade.get()
        peso = entry_peso.get()
        altura = entry_altura.get()

        if nome and idade and peso and altura:
            try:
                peso = float(peso)
                altura = float(altura)
                imc = peso / (altura ** 2)
            except ValueError:
                messagebox.showerror('Erro', 'Peso ou altura inválidos!')
                return

            conn = conectar()
            c = conn.cursor()
            c.execute('UPDATE usuarios SET nome = ?, idade = ?, peso = ?, altura = ?, imc = ? WHERE id = ?',
                      (nome, idade, peso, altura, imc, user_id))
            conn.commit()
            conn.close()
            messagebox.showinfo('Sucesso', 'Atualização realizada!')
            mostrar_usuarios()
        else:
            messagebox.showerror('Erro', 'Preencha todos os campos!')
    else:
        messagebox.showwarning('Atenção', 'Selecione corretamente')


# GUI
janela = tk.Tk()
janela.title('CRUD COM TKINTER E SQLITE 3')

label_id = tk.Label(janela, text='CPF', font=(30))
label_id.grid()
entry_id = tk.Entry(janela, font=(30))
entry_id.grid()

label_nome = tk.Label(janela, text='Nome', font=(30))
label_nome.grid()
entry_nome = tk.Entry(janela, font=(30))
entry_nome.grid()

label_idade = tk.Label(janela, text='Idade', font=(30))
label_idade.grid()
entry_idade = tk.Entry(janela, font=(30))
entry_idade.grid()

label_peso = tk.Label(janela, text='Peso', font=(30))
label_peso.grid()
entry_peso = tk.Entry(janela, font=(30))
entry_peso.grid()

label_altura = tk.Label(janela, text='Altura', font=(30))
label_altura.grid()
entry_altura = tk.Entry(janela, font=(30))
entry_altura.grid()

resultado_label = tk.Label(janela, text='Resultado:', fg='blue')
resultado_label.grid(row=4, column=0, columnspan=2)

btn_salvar = tk.Button(janela, text='salvar', font=(30), command=inserir_usuarios)
btn_salvar.grid(row=1, column=0, columnspan=2)

btn_deletar = tk.Button(janela, text='deletar', font=(30), command=eliminar_)
btn_deletar.grid(row=1, column=1, columnspan=2)

btn_atualizar = tk.Button(janela, text='atualizar', font=(30), command=atualizar)
btn_atualizar.grid(row=1, column=2, columnspan=2)

# Tabela
colunas = ('ID', 'NOME', 'IDADE', 'PESO', 'ALTURA', 'IMC')
tree = ttk.Treeview(janela, columns=colunas, show='headings')
tree.grid(row=10, column=0, columnspan=6)

for col in colunas:
    tree.heading(col, text=col)

# Ativação automática do cálculo de IMC ao digitar
entry_peso.bind('<KeyRelease>', lambda event: IMC())
entry_altura.bind('<KeyRelease>', lambda event: IMC())

# Setup inicial
criar_tabela()
mostrar_usuarios()

janela.mainloop()
