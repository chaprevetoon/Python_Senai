
dado = {}

login = "Felipe"
senha = "123"

dado['login'] = [login]
dado['senha'] = [senha]



contador = 0

for contador in range(3):
    login = input('Login:  ')
    senha_login = input('Senha de login: ')
    while login in dado['login'] and senha in dado['senha']:
        aluno = input(f'''Nome do aluno será avaliado: ''')
        n1 = float(input("Digite a 1 nota: "))
        n2 = float(input("Digite a 2 nota: "))
        n3 = float(input("Digite a 3 nota: "))
        media = float((n1 + n2 + n3) / 3)
        print(f"A média do {aluno} é :", media)
        if media < 7:
            print(f"{aluno} foi Reprovado")
        else:
            print(f"{aluno} foi Aprovado")
        break
    else:
        print("Login ou senha incorreta")
else:
    print("conta bloqueada")