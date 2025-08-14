#meu_modulo.py

def soma(a,b):
    return a+b


def sub(a,b):
    return a - b


def mult(a,b):
    return a*b


def div(a, b):
    return a / b


# main.py

from meu_modulo import soma, div
import meu_modulo
import meu_modulo as md
from meu_modulo import *




n1= int(input('N1: '))
n2= int(input('N2: '))


print(soma(n1,n2))
print(div(n1,n2))



