# DADOS PRIMITIVOS:

print(2, type(2))
print(2.2, type(2.2))
print(True, type(True))
print('Hello world!', type('Hello world!'))

# semântico
# somar 2 valores
# num1 = 10
# num2 = 20
# print(num1  num2)

# concatenar  == juntar

nome = 'Julia'
cumprimento =  'Olá, Seja bem vinda'

print(nome,cumprimento)
print(nome+' '+cumprimento)
print(f'{nome} {cumprimento}')
print('{} {}'.format(nome, cumprimento))
print('%s %s'%(nome,cumprimento))

# Escrita do usuario

numero  = int(input('Digite um número: '))
numero2 = int(input('Digite um número: '))

soma = numero + numero2

print(soma)
