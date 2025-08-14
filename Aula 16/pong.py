import pygame 

pygame.init()
janela =  pygame.display.set_mode([500,500])
pygame.display.set_caption('JOGO PONG')

BRANCO = (255,255,255)
PRETO = (0,0,0)

raquete1_x, raquete1_y = 50,225
raquete2_x, raquete2_y = 450,225
bola_x, bola_y = 250,250

largura_raquete = 100
altura_raquete = 20
largura_bola = 20
altura_bola = 20
velocidade_raquete = 0.2
velocidade_bola_y = 0.1
velocidade_bola_x = 0.1

placar1 = 0
placar2 = 0

font  = pygame.font.SysFont(None, 55)


def desenhar():

    janela.fill(BRANCO)

    pygame.draw.rect(janela, PRETO, (raquete1_x, raquete1_y, altura_raquete, largura_raquete))
    pygame.draw.rect(janela, PRETO, (raquete2_x, raquete2_y,altura_raquete, largura_raquete ))
    pygame.draw.ellipse(janela,PRETO,(bola_x, bola_y,largura_bola,altura_bola))

    placa_texto =  font.render(f'{placar1}    X    {placar2}', True, PRETO)
    janela.blit(placa_texto,(150,20))
    

run =  True
while run:
    for event  in pygame.event.get():
        if event.type == pygame.QUIT:
           run = False
           

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]  and raquete1_y > 0:
        raquete1_y -= velocidade_raquete      
    if keys[pygame.K_s] and raquete1_y < 500 - altura_raquete:
        raquete1_y += velocidade_raquete
    if keys[pygame.K_UP] and raquete2_y > 0:
        raquete2_y -= velocidade_raquete
    if keys[pygame.K_DOWN] and raquete2_y < 500 - altura_raquete:
        raquete2_y += velocidade_raquete        

    bola_x += velocidade_bola_x
    bola_y += velocidade_bola_x

    if bola_y <= 0 or bola_y >= 500 - altura_bola:
        velocidade_bola_y =  -velocidade_bola_y

    if (raquete1_x < bola_x < raquete1_x + largura_raquete) and (raquete1_y < bola_y < raquete1_y + altura_raquete):
        velocidade_bola_x = -velocidade_bola_x


    if (raquete2_x < bola_x < raquete2_x + largura_raquete) and (raquete2_y < bola_y < raquete2_y + altura_raquete):
        velocidade_bola_x = -velocidade_bola_x

    if bola_x > 500 - largura_bola:
        placar1 += 1
        bola_x, bola_y = 250,250
        velocidade_bola_x = - velocidade_bola_x
    if bola_x < 0 -largura_bola:
        placar2  += 1
        bola_x, bola_y = 250,250
        velocidade_bola_x = - velocidade_bola_x

    desenhar()

    pygame.display.update()

pygame.quit()

    
           

