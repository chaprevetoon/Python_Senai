numero  = int(input('Digite um número: '))
print('Qual operação gostaria de fazer?')
print('+ -> Soma | - -> Subtração | * -> Multiplicação | / -> Divisão: ')
op = input()
numero2 = int(input('Digite um número: '))

soma = numero + numero2

sub = numero - numero2

mult = numero * numero2

div = numero / numero2

if(op == '+'):
    print('A soma desses números é: ', soma)

if(op == '-'):
   print('A subtração desses números é: ', sub)

if(op == '*'):
    print('A multiplicação desses números é: ', mult)

if(op == '/'):
    print('A divisão desses números é: ', div)

