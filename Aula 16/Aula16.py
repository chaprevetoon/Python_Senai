import pygame
import sys


pygame.init()

width = 700
height = 500

tela = pygame.display.set_mode((width, height)) 

quandrado =  pygame.Rect(350,200, 150,70)
rectangulo2 = pygame.Rect(10,150, 50,50)

clock =  pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           pygame.quit() 
           sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                quandrado.move_ip([10,0])
            if event.key == pygame.K_LEFT:
                quandrado.move_ip([-10,0])
            if event.key == pygame.K_UP:
                quandrado.move_ip([0,-10])
            if event.key == pygame.K_DOWN:
                quandrado.move_ip([0,10])     

        
        tela.fill('red')
        pygame.draw.rect(tela,('green'), quandrado)
        pygame.draw.rect(tela,('white'), rectangulo2)
        pygame.display.update()


        # APLICAR UM 
        # RETANGULO ** 
        # ELIPSE ** 
        # DOCUMENTAÇÃO 
        # PESQUISA       


        pygame.display.flip()