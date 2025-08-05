produtos = {
'1': 'livros',
'2': 'tablets',
'3': 'fones',
}

comprar = input(f'''
    Temos em nosso estoque esse produtos com esses valores:
    Item 1 -> Livros
    Item 2 -> Tablets
    Item 3 -> Fones
    Qual desse itens você deseja comprar?
    ''')

preço = {
'1': ['',20, 30, 40],
'2': ['',500, 600, 700],
'3':  ['',100, 200, 300],
}

pagar = input(f'''
    Qual dos 3 {produtos[comprar]} você deseja:
    O {produtos[comprar]} de R${preço[comprar][1]} (1)
    O {produtos[comprar]} de R${preço[comprar][2]} (2)
    O {produtos[comprar]} de R${preço[comprar][3]} (3)
    Escolha com base no numero entre (): 
    ''')

print(f'''
    Parabéns!!! Você acabou de comprar um {produtos[comprar]} por R$ {preço[comprar][int(pagar)]}.
    ''')


