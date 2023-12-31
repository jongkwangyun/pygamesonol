import pygame

pygame.init()

background = pygame.display.set_mode((480, 360))
pygame.display.set_caption("SONOL")

x_pos = background.get_size()[0]//2 #240
y_pos = background.get_size()[1]//2 #180

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print('UP')
                y_pos = y_pos - 10
            elif event.key == pygame.K_DOWN:
                print('DOWN')
                y_pos = y_pos + 10
            elif event.key == pygame.K_RIGHT:
                print('RIGHT')
                x_pos = x_pos + 10
            elif event.key == pygame.K_LEFT:
                print('LEFT')
                x_pos = x_pos - 10
            
    background.fill((255,255,255))
    pygame.draw.circle(background, (0,0,255), (x_pos,y_pos), 5)
    #pygame.draw.circle(surface, color, center, radius)
    pygame.display.update()

pygame.quit()