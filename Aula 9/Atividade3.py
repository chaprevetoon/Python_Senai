#sistema de notas:



dados = {
'login_professor':'Carlos',
'senha':'123'
}


notas = []
nomes = []
medias = []



for n in range(3):
    login =  input('Digite seu login')
    senha = input('Digite sua senha')


    
    if login  == dados['login_professor'] and senha == dados['senha']:
            for x in range(int(input('Quantidade de alunos'))):
                print('Bem vindo ao sistema de notas')
                nome = input('NOme do aluno')
                n1 = float(input('Nota do aluno'))
                n2 = float(input('Nota do aluno'))
                nomes.append(nome)
                notas.append(n1)
                notas.append(n2)
                media = sum(notas)/len(notas)
                medias.append(media)
                print('alunos', nomes)
                print('notas', notas)
                print('Medias', medias)



    else:
       print('Tente novamente')
print('Conta bloqueada')        



input('Digite enter para sair! ')