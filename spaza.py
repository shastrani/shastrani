import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))

# make basics
pygame.display.set_caption("Madhir chod")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)
back = pygame.image.load("background.png")

# load img
player_img = pygame.image.load("rocket.png")

# player
playerX = 370
playerY = 480
playerX_change = 0

# enemy
enemy_img = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 4

for num in range(num_of_enemies):
    enemy_img.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(10, 50))
    enemyX_change.append(3)
    enemyY_change.append(20)

# ready = cant see da bullet, fire = bullet moving
bullet = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletY_change = 8
bullet_state = "ready"

# score
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
fontX = 10
fontY = 10

def score(x, y):
    score_ammount = font.render("score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score_ammount, (x, y))

# functions of players
def player(x, y):
    screen.blit(player_img, (x, y))


def enemy(x, y, num):
    screen.blit(enemy_img[num], (x, y))


def fire(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet, (x + 16, y + 10))

on = True

# loop
while on:
    screen.fill((0, 0, 0))
    screen.blit(back, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            on = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -4
            if event.key == pygame.K_RIGHT:
                playerX_change = 4
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    for num in range(num_of_enemies):
        if enemyX[num] >= 736:
            enemyX_change[num] = -3
            enemyY[num] += enemyY_change[num]
        elif enemyX[num] <= 0:
            enemyX_change[num] = 3
            enemyY[num] += enemyY_change[num]

        if enemyY[num] >= 100:
            enemyX[num] = random.randint(0, 736)
            enemyY[num] = random.randint(10, 50)

            score_value += 1

        enemyX[num] = enemyX[num] + enemyX_change[num]
        enemy(enemyX[num], enemyY[num], num)

    if bulletY <= 0:
        bullet_state = "ready"
        bulletY = 480

    if bullet_state == "fire":
        fire(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    score(fontX, fontY)
    pygame.display.update()