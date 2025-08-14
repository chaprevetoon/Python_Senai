def saque(saldo, valorq_saque):
    ope = saldo - valorq_saque
    return ope

def saldo(saldo1):
    print('R$', saldo1)

def deposito(saldo, valor_dep):
    ope = saldo + valor_dep
    return ope     


def banco():
    print('Seja bem vindo(a) ao banco X')
    saldo1 = 10000
    escolha = input('''
    1 - saque
    2 - deposito
    3 - saldo''')      
    if escolha == '1':
       saque_user =  float(input('Saque: '))
       valor_final =  saque(saldo1, saque_user)
       print('Saldo R$', saldo1)
       print('Saque R$', saque_user)
       print('Em conta R$', valor_final)
    elif escolha == '2':
       dep_user =  float(input('Deposito: '))
       valor_final =  deposito(saldo1, dep_user)
       print('Saldo R$', saldo1)
       print('Deposito R$', dep_user)
       print('Em conta R$', valor_final)  
    elif escolha =='3':
       
       sal = saldo(saldo1)
       print('Saldo R$', saldo1)
                          


banco()
