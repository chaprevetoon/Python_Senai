import random


# PAPEL TESOURA E PEDRA 


m_chute  = [0,1,2]
lista  =  ['Pedra','Papel', 'Tesoura']


computador =  random.choice(lista)
meu_chute =  int(input('Digite sua opção - Pedra 0, Papel 1, Tesoura 2: '))
comparacao =  computador == meu_chute
print('')
print('Minha escolha: ', lista[meu_chute])
print('Computador: ', computador)
etiquetas  = [0,1,2]


indice = lista.index(computador)


print('Escolha do ', computador)
print(f'''
{lista[meu_chute]} X {computador}
{indice == meu_chute} - Empate



{indice == 0 and meu_chute == 0} - Empate
{indice == 0 and meu_chute == 1} - Você ganhou 
{indice == 0 and meu_chute == 2} - Computador ganhou 


{indice == 1 and meu_chute == 1} - Empate 
{indice == 1 and meu_chute == 0} - Computador ganhou 
{indice == 1 and meu_chute == 2} - Você ganhou 


{indice == 2 and meu_chute == 1} - Computador ganhou 
{indice == 2 and meu_chute == 2} - Empate
{indice == 2 and meu_chute == 0} - Você ganhou 


''')