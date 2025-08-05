

print('Mercado Y')
produtos = ['','Arroz', 'feijão','Carne','salgadinho']
precos = ['',10.50, 8.00,10.0,5.25]
print(f'''Produtos a venda', 
      {produtos[1]} R$ - {precos[1]}
      {produtos[2]} R$ - {precos[2]}
      {produtos[3]} R$ - {precos[3]}
      {produtos[4]} R$ - {precos[4]}
''')
carrinho = []
meu_total  = []


produto_1 = int(input('Escolha o produto pelo ID - 1 - 2 - 3 - 4'))
produto_2 = int(input('Escolha o produto pelo ID - 1 - 2 - 3 - 4'))


carrinho.append(produtos[produto_1])
carrinho.append(produtos[produto_2])


meu_total.append(precos[produto_1])
meu_total.append(precos[produto_2])


soma  =  sum(meu_total)
print('-------//------')
print(f'R$ {soma}')
print(f'''Seus produtos: 
      
      1 - {produtos[produto_1]}
      2 - {produtos[produto_2]}
      
      
      ''')