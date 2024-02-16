import pygame
import random
import math

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Warna
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Nama layar
pygame.display.set_caption("Space Invaders")

# Inisialisasi layar
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Pesawat ruang angkasa
player_img = pygame.image.load('player.png')
player_width = 64
player_height = 64
player_x = SCREEN_WIDTH / 2 - player_width / 2
player_y = SCREEN_HEIGHT - player_height - 10
player_dx = 0

# Musuh
enemy_img = pygame.image.load('enemy.png')
enemy_width = 64
enemy_height = 64
enemy_x = random.randint(0, SCREEN_WIDTH - enemy_width)
enemy_y = random.randint(50, 150)
enemy_dx = 3
enemy_dy = 40

# Peluru
bullet_img = pygame.image.load('bullet.png')
bullet_width = 16
bullet_height = 16
bullet_x = 0
bullet_y = 0
bullet_dy = 10
bullet_state = "ready"

# Fungsi untuk menggambar pesawat ruang angkasa
def draw_player(x, y):
    screen.blit(player_img, (x, y))

# Fungsi untuk menggambar musuh
def draw_enemy(x, y):
    screen.blit(enemy_img, (x, y))

# Fungsi untuk menggambar peluru
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x, y))

# Fungsi untuk mendeteksi tabrakan
def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt((enemy_x - bullet_x) ** 2 + (enemy_y - bullet_y) ** 2)
    if distance < 27:
        return True
    else:
        return False

# Loop utama permainan
running = True
while running:
    # Warna layar
    screen.fill(BLACK)

    # Periksa event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Pergerakan pesawat ruang angkasa
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_dx = -5
            elif event.key == pygame.K_RIGHT:
                player_dx = 5
            elif event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_x = player_x + player_width / 2 - bullet_width / 2
                    bullet_y = player_y
                    fire_bullet(bullet_x, bullet_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_dx = 0

    # Pergerakan pesawat ruang angkasa
    player_x += player_dx
    if player_x <= 0:
        player_x = 0
    elif player_x >= SCREEN_WIDTH - player_width:
        player_x = SCREEN_WIDTH - player_width

    # Pergerakan musuh
    enemy_x += enemy_dx
    if enemy_x <= 0:
        enemy_dx = 3
        enemy_y += enemy_dy
    elif enemy_x >= SCREEN_WIDTH - enemy_width:
        enemy_dx = -3
        enemy_y += enemy_dy

    # Pergerakan peluru
    if bullet_y <= 0:
        bullet_y = 0
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_dy

    # Deteksi tabrakan
    collision = is_collision(enemy_x, enemy_y, bullet_x, bullet_y)
    if collision:
        bullet_y = player_y
        bullet_state = "ready"
        enemy_x = random.randint(0, SCREEN_WIDTH - enemy_width)
        enemy_y = random.randint(50, 150)

    # Gambar pesawat ruang angkasa, musuh, dan peluru
    draw_player(player_x, player_y)
    draw_enemy(enemy_x, enemy_y)

    # Update layar
    pygame.display.update()

# Keluar Pygame
pygame.quit()
