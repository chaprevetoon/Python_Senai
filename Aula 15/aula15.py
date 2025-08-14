import pygame 



pygame.init()
tela = pygame.display.set_mode((500,500))


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             run = False
             pygame.quit() 
        tela.fill('blue')     
        pygame.draw.rect(tela, (255,0,0),(230,230,50,50)) 
        pygame.display.flip()    