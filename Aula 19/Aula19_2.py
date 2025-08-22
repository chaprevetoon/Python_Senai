# importar a lib 
import sqlite3
# from tkinter import *



# criar o banco de dados
conexao = sqlite3.connect('banco.db')



# permitir usar o sql no arquivo python
c = conexao.cursor()


# criamos tabelas 


c.execute('''
    CREATE TABLE IF NOT EXISTS pessoas(
          
     id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,
     nome TEXT NOT NULL,
     idade INTEGER NOT NULL,
     cidade TEXT NOT NULL            
    )
''')



nome =  input('Nomes: ')
idade =  int(input('Idade; '))
cidade = input('Cidade: ')


# inserindo dados na tebela


c.execute('''INSERT INTO pessoas(nome, idade, cidade)
          values (?,?,?)''',(nome, idade, cidade))



#  atualizar o documento
conexao.commit()



# seleção de toda tabela
c.execute('SELECT * FROM pessoas')
# torna um lista 
dados = c.fetchall()


# iterado a lista  -  percorrendo a lista
for dados_tabela in dados:
    print(f'id {dados_tabela[0],dados_tabela[1], dados_tabela[2], dados_tabela[3]}')


# fechando a conexão
conexao.close()    



c = input('Enter para sair')