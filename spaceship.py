import pygame
import random

pygame.init()


SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Корабль")


ship_x = 500
ship_y = 800


enemies = []
for _ in range(4):
    enemy_x = random.randint(0, SCREEN_WIDTH - 100)
    enemy_y = random.randint(-200, -100)
    enemy_speed = 0.4  
    enemy_color = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  
    enemies.append((enemy_x, enemy_y, enemy_speed, enemy_color))


running = True
while running:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   
    keys = pygame.key.get_pressed()
    

    if keys[pygame.K_LEFT]:
        ship_x -= 1
    if keys[pygame.K_RIGHT]:
        ship_x += 1
    if keys[pygame.K_UP]:
        ship_y -= 1
    if keys[pygame.K_DOWN]:
        ship_y += 1

    for i, (enemy_x, enemy_y, enemy_speed, enemy_color) in enumerate(enemies):
        enemy_y += enemy_speed
        if enemy_y > SCREEN_HEIGHT:
            enemy_x = random.randint(0, SCREEN_WIDTH - 100)
            enemy_y = random.randint(-200, -100)
        enemies[i] = (enemy_x, enemy_y, enemy_speed, enemy_color)


    for enemy_x, enemy_y, _, _ in enemies:
        if ship_x < enemy_x + 100 and ship_x + 100 > enemy_x and ship_y < enemy_y + 100 and ship_y + 100 > enemy_y:
            running = False

    screen.fill((0,0,0,))


    pygame.draw.polygon(screen, (255, 255, 255), [(ship_x, ship_y), (ship_x + 50, ship_y - 50), (ship_x + 100, ship_y)])
    pygame.draw.rect(screen, (255, 255, 255), (ship_x + 20, ship_y - 100, 60, 100))

    for enemy_x, enemy_y, _, enemy_color in enemies:
        pygame.draw.rect(screen, enemy_color, (enemy_x, enemy_y, 100, 100))

    
    pygame.display.flip()

pygame.quit()


