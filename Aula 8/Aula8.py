import random

elementos = ['Pedra', 'Papel', 'Tesoura']
valor_aleatorio = random.choice(elementos)
chute  =  input(f'Escolha um: {elementos} : ')

if valor_aleatorio == chute:
   print('Empate') 
elif chute == 'Pedra' and valor_aleatorio=='Papel':
   print('A máquina escolheu', valor_aleatorio)
   print('A máquina ganhou')
elif chute == 'Papel' and valor_aleatorio == 'Tesoura':
   print('A máquina escolheu', valor_aleatorio)
   print('A máquina ganhou')  
elif chute == 'Tesoura' and valor_aleatorio == 'Pedra':
   print('A máquina escolheu', valor_aleatorio)
   print('A máquina ganhou')   

elif valor_aleatorio == 'Pedra' and chute=='Papel':
   print('A máquina escolheu', valor_aleatorio)
   print('Você ganhou')
elif valor_aleatorio == 'Papel' and chute == 'Tesoura':
   print('A máquina escolheu', valor_aleatorio)
   print('Você ganhou')  
elif valor_aleatorio == 'Tesoura' and chute == 'Pedra':
   print('A máquina escolheu', valor_aleatorio)
   print('Você ganhou')  










# idade  =  0

# if idade == 25:
#    print('Ele tem 25  anos')
# elif idade >=15 and idade <=17 :
#    print('Adolescente')
# elif idade > 0 and idade <=12:
#    print('Criança')
# elif idade >64:
#    print('Idoso') 
# else:
#    print('Teste') 

