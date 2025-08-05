
qt = int(input(f'''
Bem vindos ao Hotel Lago Luxe. Quarto para quantos clientes? (máximo de 3 clientes por quarto)
'''))
print('')
if qt == 1:
    nome = input('Qual o seu nome: ')
    print('')
    idade = int(input('Qual a sua idade: '))
    print('')
    if idade < 18:
        print("Desculpe mas você ainda não tem idade para ser o resposável pela reserva. Volte com um adulto.")
        quit()
    else:
        print(f'Seja muito bem vindo {nome}')
elif qt == 2:
    nomeR = input('Qual o nome do responsavel pela reserva: ')
    idadeR = int(input('Qual a sua idade: '))
    print('')
    if idadeR < 18:
        print("Desculpe mas você ainda não tem idade para ser o resposável pela reserva. Volte com um adulto.")
        quit()
    else:
        print(f'Seja muito bem vindo {nomeR}')
        print('')
        nomeA = input('Qual o nome da pessoa que te acompanha: ')
        idadeA = input('Qual a idade dela: ')
elif qt == 3:
    nomeRe = input('Quem será o responsavel: ')
    idadeRe = int(input('Qual a sua idade: '))
    print('')
    if idadeRe < 18:
        print("Desculpe mas você ainda não tem idade para ser o resposável pela reserva. Volte com um adulto.")
        quit()
    else:
        print(f'Seja muito bem vindo {nomeRe}')
        print('')
        nomeA1 = input('Qual o nome de uma das pessoas que te acompanha: ')
        idadeA1 = input('Qual a idade dela: ')
        print('')
        nomeA2 = input('Qual o nome da outra pessoa: ')
        idadeA2 = input('Qual a idade dela: ')
else:
    print("Desculpe mas não é possivel alocar essa quantidade de cliente.")
    quit()


quartos ={
    '1' : 'simples',
    '2' : 'duplo',
    '3' : 'luxo'
}

diaria = input(f'''
    Temos em nosso hotel esses tipos de quartos disponiveis:
    Quarto 1 -> Simples: R$ 100,00 por dia por pessoa.
    Quarto 2 -> Duplo: R$ 150,00 por dia por pessoa.
    Quarto 3 -> Luxo: R$ 250,00 por dia por pessoa.
    Qual desses quartos você deseja se hospedar?
    ''')
print(f"Você recervou o quarto {quartos[diaria]}")

dia = int(input(f"Por quantos dias deseja alugar o quarto {quartos[diaria]}? "))

if quartos[diaria] == 'simples':
    preço1 = (100 * dia) * qt
    print(f'Sua reserva foi para o quarto {quartos[diaria]} por {dia} dias e para {qt} pessoas')
    print(f'Total da reserva: {preço1}')
elif quartos[diaria] == 'duplo':
    preço2 = (150 * dia) * qt
    print(f'Sua reserva foi para o quarto {quartos[diaria]} por {dia} dias e para {qt} pessoas')
    print(f'Total da reserva: {preço2}')
elif quartos[diaria] == 'luxo':
    preço3 = (250 * dia) * qt
    print(f'Sua reserva foi para o quarto {quartos[diaria]} por {dia} dias e para {qt} pessoas')
    print(f'Total da reserva: {preço3}')