import pygame
import random

pygame.init()

SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 1000

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Корабль")


picture = pygame.image.load("space1.jpg")

shipimg = pygame.image.load("ship.png")
ship_x = 800
ship_y = 850

def ship():
    screen.blit(shipimg, (ship_x, ship_y))

enemy_img = pygame.image.load("enemy.png")

def draw_enemies():
    for enemy_x, enemy_y, _ in enemies:
        screen.blit(enemy_img, (enemy_x, enemy_y))

bullet_x = None
bullet_y = None
bullet_speed = 5
bullet_fired = False

score = 0


initial_enemy_speed = 3
current_enemy_speed = initial_enemy_speed

enemies = []
def spawn_enemies(n, speed):
    for _ in range(n):
        enemy_x = random.randint(0, SCREEN_WIDTH - 100)
        enemy_y = random.randint(-200, -100)
        enemies.append((enemy_x, enemy_y, speed))

spawn_enemies(4, current_enemy_speed)

font = pygame.font.Font(None, 36)

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(picture, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not bullet_fired:
                bullet_x = ship_x + 50
                bullet_y = ship_y
                bullet_fired = True

    ship()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        ship_x -= 3
    if keys[pygame.K_RIGHT]:
        ship_x += 3

    ship_x = max(0, min(ship_x, SCREEN_WIDTH - shipimg.get_width()))

    for i, (enemy_x, enemy_y, enemy_speed) in enumerate(enemies):
        enemy_y += enemy_speed
        if enemy_y > SCREEN_HEIGHT:
            enemy_x = random.randint(0, SCREEN_WIDTH - 100)
            enemy_y = random.randint(-200, -100)
        enemies[i] = (enemy_x, enemy_y, enemy_speed)

    if bullet_fired:
        bullet_y -= bullet_speed
        if bullet_y < 0:
            bullet_fired = False

    for enemy_x, enemy_y, _ in enemies:
        if ship_x < enemy_x + 100 and ship_x + 100 > enemy_x and ship_y < enemy_y + 100 and ship_y + 100 > enemy_y:
            running = False

    for i, (enemy_x, enemy_y, _) in enumerate(enemies):
        if bullet_x and bullet_y and enemy_x < bullet_x < enemy_x + 100 and enemy_y < bullet_y < enemy_y + 100:
            enemies.pop(i)
            bullet_fired = False
            score += 1
            if len(enemies) == 0:
                current_enemy_speed += 0.5
                spawn_enemies(4, current_enemy_speed)
            break

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    draw_enemies()

    if bullet_fired:
        pygame.draw.rect(screen, (255, 0, 0), (bullet_x, bullet_y, 20, 20))

    pygame.display.flip()

pygame.quit()