
meus_pro = []
def restaurante():
    menu = ['','SALADA', 'MACARRONADA', 'SANDUICHE', 'SORVETE']
    print('menu', menu)
    
    pedido = input('Deseja pedir? ')
    while pedido ==  's':
        escolhas  =  int(input('''
         MENU:                       
         1 SALADA
         2 MACARRONADA
         3 SANDUICHE
         4 SORVETE     '''))                                    
                             


        meus_pro.append(menu[escolhas]) 
        pedido = input('Deseja algo mais? ')
        print(meus_pro)
    else: 
        print('Obrigada volte sempre! ')

restaurante()

