import pygame
from random import randint

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter")
running = True
clock = pygame.time.Clock()

# Trial
surf = pygame.Surface((100,200))
surf.fill('orange')
x = 100

# importing stuff
player_surf = pygame.image.load('images/player.png').convert_alpha()
player_rect = player_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
player_direction = pygame.math.Vector2()
player_speed = 300

star_surface = pygame.image.load('images/star.png').convert_alpha()
star_position = [[randint(0,WINDOW_WIDTH),randint(0,WINDOW_HEIGHT)] for i in range (20)]

meteor_surface = pygame.image.load('images/meteor.png').convert_alpha()
meteor_rect = meteor_surface.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

laser_surf = pygame.image.load('images/laser.png').convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft = (20, WINDOW_HEIGHT - 20))


while running:
    dt = clock.tick() / 1000
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #input 
    keys = pygame.key.get_pressed()
    player_direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
    player_direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
    player_direction = player_direction.normalize() if player_direction else player_direction
    player_rect.center += player_direction * player_speed * dt

    # draw the game
    display_surface.fill('grey20')
    for pos in star_position:
        display_surface.blit(star_surface, pos)

    display_surface.blit(meteor_surface, meteor_rect)
    display_surface.blit(laser_surf,laser_rect)
    display_surface.blit(player_surf, player_rect.topleft)

    pygame.display.update()
pygame.quit
