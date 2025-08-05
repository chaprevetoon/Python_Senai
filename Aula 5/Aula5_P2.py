# Média  de alunos


lista_nomes = []
lista_aluno1 = []
lista_aluno2 = []
lista_aluno3 = []
lista_medias = []

aluno1, aluno2 , aluno3 = input('Nome: '),input('Nome: '),input('Nome: ')
lista_nomes.extend([aluno1,aluno2, aluno3])
# .extend é o mesmo que +=


n1 =float(input(f'Nota 1 aluno(a) {aluno1}: '))
n2 = float(input(f'Nota 2 aluno(a) {aluno1}: '))
n3 = float(input(f'Nota 3 aluno(a) {aluno1}: '))

n4 =float(input(f'Nota 1 aluno(a) {aluno2}: '))
n5 = float(input(f'Nota 2 aluno(a){aluno2}:'))
n6 = float(input(f'Nota 3 aluno(a) {aluno2}: '))

n7 =float(input(f'Nota 1 aluno(a) {aluno3}: '))
n8 = float(input(f'Nota 2 aluno(a){aluno3}: '))
n9 = float(input(f'Nota 3 aluno(a){aluno3}: '))

lista_aluno1 += (n1,n2,n3)
lista_aluno2 +=  (n4,n5,n6)
lista_aluno3 += (n7,n8,n9)
# += é o mesmo que o .extend

# notas de cada aluno: 
print(lista_nomes[0], 'Notas', aluno1)
print(lista_nomes[1], 'Notas', aluno2)
print(lista_nomes[2], 'Notas', aluno3)

media1 = sum(lista_aluno1)/len(lista_aluno1)
media2 = sum(lista_aluno2)/len(lista_aluno2)
media3 = sum(lista_aluno3)/len(lista_aluno3)





lista_medias.extend([media1, media2, media3])

print(f'''
aluno:                  |   media
{lista_nomes[0]}        |   {lista_medias[0]}
{lista_nomes[1]}        |   {lista_medias[1]}
{lista_nomes[2]}        |   {lista_medias[2]}



''')

maior = max(lista_medias)
indice = lista_medias.index(maior)

# qual a maior média
print('Maior média', max(lista_medias))

# Aluno com a maior médio
print('O aluno que tirou a maior mé dia foi o', lista_nomes[indice])