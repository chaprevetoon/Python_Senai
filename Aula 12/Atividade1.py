
# CRIE UMA FUNÇÃO PARA COMPARAR 2 NÚMEROS (par ou impar).
# UTILIZE VARIÁVEIS LOCAIS.

def par():
    print("Esse numero é par")

def impar():
    print("Esse numero é impar")

def impar_ou_par():
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        par()
    else:
        impar()

impar_ou_par()