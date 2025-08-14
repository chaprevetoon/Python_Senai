
print('===============Exercicio 1====================')
# Peça para o usuário digitar um número, verifique se um 
# número é positivo, negativo ou zero.

numero = int(input("Digite um número: "))
if numero == 0:
    print(f"{numero} é zero")
elif numero < 0:
    print(f"{numero} é um numero negativo" )
else:
    print(f"{numero} é um numero positivo")


print('===============Exercicio 2====================')
# Peça para o usuário digitar a idade, verifique se uma 
# pessoa pode votar com base na idade.

idade = int(input('Digite sua idade: '))
anos = 18 - idade
if idade >= 18:
    print('Parabens, você pode votar')
else:
    print('Desculpa, você ainda não pode votar. ' \
    f'Ainda faltam {anos} anos para isso.')

print('===============Exercicio 3====================')
# Declara uma variável com um número qualquer, determine
# se um número é par ou ímpar.

import random

n = random.randint(1, 100)
if n % 2 == 1:
    print(f'{n} é impar')
else:
    print(f'{n} é par')

 # # equilátero, isósceles ou escaleno


 l1 = int(input('lado 1: '))
 l2 = int(input('lado 2: '))
 l3 = int(input('lado 3: '))

 if l1 == l2 == l3 == l1:
     print('Equilatero')
 elif l1 != l2 != l3 != l1:
     print('escaleno')   
 else:
     print('isoceles')     


 n = int(input('Numero: '))

 if n % 5 == 0 and n % 7 == 0:
     print('é divisivel por 5 e  7 ')
 else:

 #     print('Não é')    
 n = int(input('Numero: '))


 if n > 0 and n > 10:
     print('Verdade')
 else:
     print('Erro')    

n = int(input('Numero: '))

if n % 3 == 0 or n % 5 ==0:
    print('Verdade')
else:
    print('False')    
