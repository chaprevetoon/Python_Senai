import tkinter as tk

def enviar_dados():
    nome = entry_nome.get()
    idade = entry_idade.get()
    email = entry_email.get()
    endereco = entry_endereco.get()
    celular = entry_celular.get()

    print("=== Dados do Cliente ===")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"E-mail: {email}")
    print(f"Endereço: {endereco}")
    print(f"Celular: {celular}")
    print("========================")

tela = tk.Tk()
tela.title("Cadastro de Clientes")
tela.geometry("1700x750")

titulo = tk.Label(tela, text="Formulário de Cadastro de Cliente", font=("Arial", 24), fg="blue")
titulo.pack(pady=20)

frame = tk.Frame(tela)
frame.pack(pady=10)

label_nome = tk.Label(frame, text="Nome:", font=("Arial", 14))
label_nome.grid(row=0, column=0, sticky='e', padx=10, pady=10)
entry_nome = tk.Entry(frame, width=50, font=("Arial", 14))
entry_nome.grid(row=0, column=1)

label_idade = tk.Label(frame, text="Idade:", font=("Arial", 14))
label_idade.grid(row=1, column=0, sticky='e', padx=10, pady=10)
entry_idade = tk.Entry(frame, width=50, font=("Arial", 14))
entry_idade.grid(row=1, column=1)

label_email = tk.Label(frame, text="E-mail:", font=("Arial", 14))
label_email.grid(row=2, column=0, sticky='e', padx=10, pady=10)
entry_email = tk.Entry(frame, width=50, font=("Arial", 14))
entry_email.grid(row=2, column=1)

label_endereco = tk.Label(frame, text="Endereço:", font=("Arial", 14))
label_endereco.grid(row=3, column=0, sticky='e', padx=10, pady=10)
entry_endereco = tk.Entry(frame, width=50, font=("Arial", 14))
entry_endereco.grid(row=3, column=1)

label_celular = tk.Label(frame, text="Celular:", font=("Arial", 14))
label_celular.grid(row=4, column=0, sticky='e', padx=10, pady=10)
entry_celular = tk.Entry(frame, width=50, font=("Arial", 14))
entry_celular.grid(row=4, column=1)

btn_enviar = tk.Button(tela, text="Enviar", font=("Arial", 16), bg="green", fg="white", command=enviar_dados)
btn_enviar.pack(pady=30)

tela.mainloop()
