import pygame
import pygame.locals
import pygame.font
import pygame.mixer

pygame.init()
pygame.mixer.init()
pygame.font.init()

WIDTH, HEIGHT = 1000, 600
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Example Game")
playerwidth = 100
playerheight = 100
playerimg = pygame.transform.scale(pygame.image.load("stickman.png"), (playerwidth, playerheight))
player_x, player_y = 100, 0
player_speed = 5

def move_player(x, y, oldx, oldy):
    global player_x, player_y
    player_x = oldx + x
    player_y = oldy + y

def draw_player():
    WIN.blit(playerimg, (player_x, player_y))

def draw():
    WIN.fill((255, 255, 255))
    draw_player()
    pygame.display.update()

def keys():
    p_keys = pygame.key.get_pressed()
    if p_keys[pygame.K_RIGHT] and player_x + playerwidth < WIDTH - player_speed:
        move_player(player_speed, 0, player_x, player_y)
    if p_keys[pygame.K_LEFT] and player_x > player_speed:
        move_player(-player_speed, 0, player_x, player_y)
    if p_keys[pygame.K_UP] and player_y > player_speed:
        move_player(0, -player_speed, player_x, player_y)
    if p_keys[pygame.K_DOWN] and player_y + playerheight < HEIGHT - player_speed:
        move_player(0, player_speed, player_x, player_y)

def main():    
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys()
        draw()

if __name__ == "__main__":
    main()