import tkinter as tk
import sqlite3

def enviar_dados():

    conexao = sqlite3.connect('banco2.db')

    c = conexao.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS pessoas(
            
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        email TEXT NOT NULL,
        endereço TEXT NOT NULL,
        trabalho TEXT NOT NULL,
        graducação TEXT NOT NULL           
        )
    ''')

    nome = input_nome.get()
    idade = input_idade.get()
    email = input_email.get()
    endereco = input_endereco.get()
    trabalho = input_trabalho.get()
    graduacao = input_graducacao.get()

    print("=== Dados do Cliente ===")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"E-mail: {email}")
    print(f"Endereço: {endereco}")
    print(f"Trabalho: {trabalho}")
    print(f"Celular: {graduacao}")
    
    c.execute('''INSERT INTO pessoas(nome, idade, email, endereço, trabalho, graducação)
            values (?,?,?,?,?,?)''',(nome, idade, email, endereco, trabalho, graduacao))
    conexao.commit()

    print("========================")

    c.execute('SELECT * FROM pessoas')
    dados = c.fetchall()

    for dados_tabela in dados:
       print(f'id {dados_tabela[0],dados_tabela[1], dados_tabela[2], dados_tabela[3], dados_tabela[4], dados_tabela[5], dados_tabela[6]}')

    conexao.close()



tela = tk.Tk()
tela.title("Banco de Dados")
tela.geometry("1000x500")

titulo = tk.Label(tela, text="Dados para o Banco de Dados", font=("Arial", 24), fg="blue")
titulo.pack(pady=20)

frame = tk.Frame(tela)
frame.pack(pady=10)

label_nome = tk.Label(frame, text="Nome:", font=("Arial", 14))
label_nome.grid(row=0, column=0, sticky='e', padx=10, pady=10)
input_nome = tk.Entry(frame, width=50, font=("Arial", 14))
input_nome.grid(row=0, column=1)

label_idade = tk.Label(frame, text="Idade:", font=("Arial", 14))
label_idade.grid(row=1, column=0, sticky='e', padx=10, pady=10)
input_idade = tk.Entry(frame, width=50, font=("Arial", 14))
input_idade.grid(row=1, column=1)

label_email = tk.Label(frame, text="E-mail:", font=("Arial", 14))
label_email.grid(row=2, column=0, sticky='e', padx=10, pady=10)
input_email = tk.Entry(frame, width=50, font=("Arial", 14))
input_email.grid(row=2, column=1)

label_endereco = tk.Label(frame, text="Endereço:", font=("Arial", 14))
label_endereco.grid(row=3, column=0, sticky='e', padx=10, pady=10)
input_endereco = tk.Entry(frame, width=50, font=("Arial", 14))
input_endereco.grid(row=3, column=1)

label_trabalho = tk.Label(frame, text="Trabalho:", font=("Arial", 14))
label_trabalho.grid(row=4, column=0, sticky='e', padx=10, pady=10)
input_trabalho = tk.Entry(frame, width=50, font=("Arial", 14))
input_trabalho.grid(row=4, column=1)

label_graducacao = tk.Label(frame, text="Graducacao:", font=("Arial", 14))
label_graducacao.grid(row=5, column=0, sticky='e', padx=10, pady=10)
input_graducacao = tk.Entry(frame, width=50, font=("Arial", 14))
input_graducacao.grid(row=5, column=1)

btn_enviar = tk.Button(tela, text="Enviar", font=("Arial", 16), bg="green", fg="white", command=enviar_dados)
btn_enviar.pack(pady=30)

tela.mainloop()
