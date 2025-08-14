#sistema de notas:
from colorama import just_fix_windows_console
from colorama import init
from colorama import Fore, Back, Style


init()
dados = {
'login_professor':'Carlos',
'senha':'123'
}

notas = []
nomes = []
medias = []
notasP = []

imprimir = []

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
                notas.extend([n1, n2])
                media = (n1 + n2) / 2
                medias.append(media)
                print(Fore.RED + 'Média', media)
                print(Fore.GREEN + 'alunos', nomes)
                print(Fore.RED + 'notas', notas)
                print(medias)
                
            # medias.append(sum(notas)/len(notas))
            # notasP.append(medias)
            # print(notasP)        
                    


    else:
       print('Tente novamente')
 
print('Conta bloqueada')        


input('Digite enter para sair! ')