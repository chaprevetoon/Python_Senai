# MANIPULAÇÃO DOS EVENTOS
# JOGO LABIRINTO

import pygame  # importando a biblioteca Pygame

pygame.init() # Inicializa o Pygame



# COMENTE O CÓDIGO, EXPLIQUE COM SUAS PALAVRAS O QUE ESTA OCORRENDO EM CADA ESTRUTURA DO 
# CÓDIGO E VERIFIQUE O QUE OCORRE. 
# CONSULTE A BIBLIOTECA -> https://www.pygame.org/docs/





largura, altura = 400, 400
tela = pygame.display.set_mode((largura, altura))   # Defindo a largura e altura da janela onde irá rodar o jogo
pygame.display.set_caption("Labirinto")             # Nome da janela do jogo


preto = (0, 0, 0)
branco = (255, 255, 255)        # transformando as cores em variaveis para facilitar leitura do codigo posteriormente
vermelho = (255, 0, 0)


tamanho_celula = 40
labirinto = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 0, 1],         # montando o visial do labirinto (nesse caso onde tem 1 mostrará blocos pretos enquanto o  0 mostrará blocos brancos)
    [1, 1, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


x, y = 1 * tamanho_celula, 1 * tamanho_celula   
velocidade = 40

def desenhar_labirinto():
    for linha in range(len(labirinto)):
        for coluna in range(len(labirinto[linha])):                            # Fazendo o desenho do labirinto 
            cor = preto if labirinto[linha][coluna] == 1 else branco
            pygame.draw.rect(tela, cor, (coluna * tamanho_celula, linha * tamanho_celula, tamanho_celula, tamanho_celula))


executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:          
            executando = False


    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        novo_x = x - velocidade
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:
            x = novo_x
    if teclas[pygame.K_RIGHT]:
        novo_x = x + velocidade
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:           # Controle do "personagem"
            x = novo_x
    if teclas[pygame.K_UP]:
        novo_y = y - velocidade
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
            y = novo_y
    if teclas[pygame.K_DOWN]:
        novo_y = y + velocidade
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
            y = novo_y


    tela.fill(branco)       # Tela de fundo é branca

    
    desenhar_labirinto()        # chama o metodo mais cedo que fez o desenho do labirinto
    pygame.draw.rect(tela, vermelho, (x, y, tamanho_celula, tamanho_celula))


    pygame.display.flip()       # "Printa" esse desenho


    pygame.time.Clock().tick(10)        # limita a taxa de quadros


pygame.quit()           # Permite sair da janela.