# Arquivo criado pelo arquivo aula14.py

import os

#os.mkdir('Teste_Pasta') Para criar a Pasta

with os.scandir('C:/Users/Aluno/Desktop/Aluno/Aula 14') as teste:
    for pasta in teste:
        if pasta.is_dir() and pasta.name == 'Teste_Pasta':
            print(f'Diretorio encontrado: {pasta.name}')
            break
        if pasta.is_dir() and pasta.name != 'Teste_Pasta':
            print(f'Diretorio não encontrado')