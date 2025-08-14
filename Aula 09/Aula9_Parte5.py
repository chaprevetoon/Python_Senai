dados = {}

print('Cadastre-se: ')

nome1  = input('Nome: ')
idade1 = int(input('Idade: '))
senha1 = input('Senha:')

nome2  = input('Nome: ')
idade2 = int(input('Idade: '))
senha2 = input('Senha:')

dados['nomes'] = [nome1,nome2]
dados['idades'] = [idade1, idade2]
dados['senhas'] = [senha1, senha2]


print('DADOS CADASTRADOS: ', dados)

# ------------


# login = input('Login:  ')
# senha_login = input('Senha de login: ')


for n in range(2):
    login = input('Login:  ')
    senha_login = input('Senha de login: ')
    if login in dados['nomes'] and senha_login in dados['senhas']:
        print('''Tipos de quartos 
            1 - Simples: R$ 100,00 por dia.
            2 - Duplo: R$ 150,00 por dia.
            3 - Luxo: R$ 250,00 por dia.
            ''')

        quartos =  ['',100.0,150.0,250.0]
        nomes_quartos = ['', 'Simples', 'Duplo','Luxo']

        quarto1 = int(input(f'Escolha o quarto {nome1} pelo ID 1 - 2 -3'))
        quant_dias1 = int(input(f'Quantidade Dias do {nome1}: '))
        calculo_1 = quartos[quarto1] * quant_dias1

        print(f'O cliente {nome1}, escolheu o quarto{nomes_quartos[quarto1]}')
        print(f'Total -  cliente {nome1}, R$ {calculo_1}')
    
        dados['quartos'] = [quartos[quarto1]]
    

        quarto2 = int(input(f'Escolha o quarto {nome2} pelo ID 1 - 2 -3'))
        quant_dias2 = int(input(f'Quantidade Dias do {nome2}: '))

        calculo_2 = quartos[quarto2] * quant_dias2
        print(f'O cliente {nome1}, escolheu o quarto{nomes_quartos[quarto1]}')   
        print(f'Total -  cliente {nome2}, R$ {calculo_2}')

        dados['quartos'] = [quartos[quarto1]]
        dados['entradas'] = [calculo_1,calculo_2]

        print('DADOS CADASTRADOS:', dados)

    else:
        print('Você digitou algo errado, tente novamente')    
else:
    print('Conta bloqueada!')