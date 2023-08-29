import pygame

pygame.init()

background = pygame.display.set_mode((480, 360))
pygame.display.set_caption("SONOL")

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print('UP')
            elif event.key == pygame.K_DOWN:
                print('DOWN')
            elif event.key == pygame.K_RIGHT:
                print('RIGHT')
            elif event.key == pygame.K_LEFT:
                print('LEFT')

pygame.quit()