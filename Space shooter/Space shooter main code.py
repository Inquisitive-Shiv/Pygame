import pygame
from random import randint

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter")
running = True

# Trial
#surf = pygame.Surface((100,200))
#surf.fill('orange')
x = 100

# importing stuff
player_surf = pygame.image.load('images/player.png').convert_alpha()
player_rect = player_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

star_surface = pygame.image.load('images/star.png').convert_alpha()
star_position = [[randint(0,WINDOW_WIDTH),randint(0,WINDOW_HEIGHT)] for i in range (20)]

meteor_surface = pygame.image.load('images/meteor.png').convert_alpha()
meteor_rect = meteor_surface.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

laser_surf = pygame.image.load('images/laser.png').convert_alpha()

while running:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw the game
    display_surface.fill('grey20')
    for pos in star_position:
        display_surface.blit(star_surface, pos)
    if player_rect.right < WINDOW_WIDTH:    
        player_rect.left += 0.2

    display_surface.blit(meteor_surface, meteor_rect)
    
    display_surface.blit(player_surf, player_rect)
    pygame.display.update()
pygame.quit