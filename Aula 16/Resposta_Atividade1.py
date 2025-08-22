# MANIPULAÇÃO DOS EVENTOS
# JOGO LABIRINTO

# importando uma lib
import pygame

# Inicializa o Pygame
pygame.init()



# COMENTE O CÓDIGO, EXPLIQUE COM SUAS PALAVRAS O QUE ESTA OCORRENDO EM CADA ESTRUTURA DO 
# CÓDIGO E VERIFIQUE O QUE OCORRE. 
# CONSULTE A BIBLIOTECA -> https://www.pygame.org/docs/




# variáveis que cria altura e largura da tela 
largura, altura = 400, 400

# atibuição de uma função do módulo do pygame que 
# cria uma tela
tela = pygame.display.set_mode((largura, altura))

# atibuição de uma função do módulo do pygame que 
# cria um título para a minha tela 
pygame.display.set_caption("Labirinto")

# tuplas que setam cor e tamanho na animação
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)

# variável que define o tamanho do personagem  

tamanho_celula = 40

# lista com mais dimensões, onde o personagem interage com o zeros

labirinto = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# 2 variáveis que determinam a posição 
x, y = 1 * tamanho_celula, 1 * tamanho_celula

# variável que determina a velocidade  velocidade 
velocidade = 40


# função que promove a renderização 

def desenhar_labirinto():
    # loop 
    # foor aninhado que itera a lista, ecessando todos o valores
    # da lista
    for linha in range(len(labirinto)):
        for coluna in range(len(labirinto[linha])):
            # variável que promove cor aos espaços da tela 
            cor = preto if labirinto[linha][coluna] == 1 else branco
            # função do módulo que desenha as formas na tela 
            pygame.draw.rect(tela, cor, (coluna * tamanho_celula, linha * tamanho_celula, tamanho_celula, tamanho_celula))

# loop 
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    # captura e verificação dos eventos de movimento
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        novo_x = x - velocidade
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:
            x = novo_x
    if teclas[pygame.K_RIGHT]:
        novo_x = x + velocidade
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:
            x = novo_x
    if teclas[pygame.K_UP]:
        novo_y = y - velocidade
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
            y = novo_y
    if teclas[pygame.K_DOWN]:
        novo_y = y + velocidade
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
            y = novo_y

    # função que pinta a tela de branco 
    tela.fill(branco)

    # função invocada  - labirinto
    desenhar_labirinto()

    # # função que cria o retagulo personagem  
    pygame.draw.rect(tela, vermelho, (x, y, tamanho_celula, tamanho_celula))

    # atualização da tela 
    pygame.display.flip()

    # frame count contagem de quadros
    pygame.time.Clock().tick(10)

# função de saída do pygame
pygame.quit()


  