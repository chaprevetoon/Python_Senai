
# 1 - Faça um programa, utilizando while, que mostre 
# na tela os números de 0 a 1000.

n = 0
while n <= 1000:
    print(n)
    n = n  +  1

#2 -  Faça um sistema, utilizando while e listas, que 
# permita o usuário escrever o nome de 10 pessoas e os
# mostre na tela.

nomes = []

n = 0

while n < 10:
    nome = input('Digite um nome: ')
    print(f"Nome digitado: {nome}")
    n = n + 1

