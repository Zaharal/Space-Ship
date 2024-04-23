import pygame
import random
pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Корабль")

ship_x = 500
ship_y = 800

bullet_x = None
bullet_y = None
bullet_speed = 1
bullet_fired = False


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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not bullet_fired:
                    bullet_x = ship_x + 50
                    bullet_y = ship_y
                    bullet_fired = True

   
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
        

    if not enemies:
        for _ in range(4):
            enemy_x = random.randint(0, SCREEN_WIDTH - 100)
            enemy_y = random.randint(-200, -100)
            enemy_speed = 0.4  
            enemy_color = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  
            enemies.append((enemy_x, enemy_y, enemy_speed, enemy_color))


    if bullet_fired:
        bullet_y -= bullet_speed
        if bullet_y < 0:
            bullet_fired = False


    for enemy_x, enemy_y, _, _ in enemies:
        if ship_x < enemy_x + 100 and ship_x + 100 > enemy_x and ship_y < enemy_y + 100 and ship_y + 100 > enemy_y:
            running = False
    
    for i, (enemy_x, enemy_y, _, _) in enumerate(enemies):
        if bullet_x and bullet_y and enemy_x < bullet_x < enemy_x + 100 and enemy_y < bullet_y < enemy_y + 100:
            enemies.pop(i)
            bullet_fired = False
            break


    screen.fill((0,0,0,))


    pygame.draw.polygon(screen, (255, 255, 255), [(ship_x, ship_y), (ship_x + 50, ship_y - 50), (ship_x + 100, ship_y)])
    pygame.draw.rect(screen, (255, 255, 255), (ship_x + 20, ship_y - 100, 60, 100))
    
    if bullet_fired:
        pygame.draw.rect(screen, (255, 0, 0), (bullet_x, bullet_y, 5, 5))

        
    for enemy_x, enemy_y, _, enemy_color in enemies:
        pygame.draw.rect(screen, enemy_color, (enemy_x, enemy_y, 100, 100))

    
    pygame.display.flip()

pygame.quit()