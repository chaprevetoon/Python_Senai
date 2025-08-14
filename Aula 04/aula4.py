print('Verificar se o aluno passou')
nome  =  input('Digite o nome do aluno: ')
nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
nota3 = float(input('Digite a nota 3: '))
media =  (nota1 +  nota2 +  nota3)/3
print('A média do aluno', nome, 'é ',round( media))

print(f'''
        SITUAÇÃO DO ALUNO   {nome}
        APROVADO  -  {media >= 7}
        RECUPERAÇÃO  -  {media >=5 and media <7 }
        REPROVADO   - {media <5}
''')
#f para concatenar as {} e ''' para deixar a formatação dessa forma
# \n tbm quebra linha ex.:
print('teste \n de \n quebra de linha')
