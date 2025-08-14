print("=======Exercício 0========")
print("Escreva um programa que use a função range() para " \
"gerar os números pares de 2 a 20 e, em seguida, imprima " \
"cada número.")

lista = list(range(2,21,2))
print(lista)

###########################################

print("=======Exercício 1========")
print("Crie uma lista chamada numeros que contenha os números" \
"inteiros de 1 a 10 e imprima-a na tela.")

numeros = list(range(1,11))
print(numeros)

###########################################

print("=======Exercício 2========")
print("Acesse e imprima o terceiro elemento da lista `numeros`.")

print(numeros[2])

###########################################

print("=======Exercício 3========")
print("Adicione o número 9 à lista numeros e imprima a lista " \
"atualizada.")

numeros += ([9])
numeros.append(9) 
numeros.extend([9])
print(numeros)

###########################################

print("=======Exercício 4========")
print("Remova o número 5 da lista numeros e imprima a lista " \
"resultante.")

numeros.remove(5)
print(numeros)

###########################################

print("=======Exercício 5========")
print("Crie uma lista chamada carros contendo três nomes de " \
"carros diferentes. Em seguida, concatene essa lista com a" \
" lista numeros e imprima o resultado.")

print("Exemplo 1")
carros = list(["carro1", 'carro2', 'carro3'])
print(numeros, carros)

print("Exemplo 2")
numeros += carros
print(numeros)

print("Exemplo 3")
carros.extend(numeros)
print(carros)

print("Exemplo 4")
numeros.append(carros)
print(numeros)