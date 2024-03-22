import pygame
import random

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pesawat Tembakan")

# Warna
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Kecepatan pesawat
PLAYER_SPEED = 5

# Kecepatan peluru
BULLET_SPEED = 10

# Kecepatan musuh
ENEMY_SPEED = 3

# Ukuran pesawat
PLAYER_SIZE = (50, 50)

# Ukuran peluru
BULLET_SIZE = (10, 10)

# Ukuran musuh
ENEMY_SIZE = (50, 50)

# Posisi awal pesawat
player_x = SCREEN_WIDTH // 2 - PLAYER_SIZE[0] // 2
player_y = SCREEN_HEIGHT - PLAYER_SIZE[1] - 10

# Daftar peluru
bullets = []

# Daftar musuh
enemies = []

# Fungsi untuk menambahkan musuh
def add_enemy():
    enemy_x = random.randint(0, SCREEN_WIDTH - ENEMY_SIZE[0])
    enemy_y = -ENEMY_SIZE[1]
    enemy = pygame.Rect(enemy_x, enemy_y, ENEMY_SIZE[0], ENEMY_SIZE[1])
    enemies.append(enemy)

# Fungsi untuk menggambar pesawat
def draw_player():
    player = pygame.Rect(player_x, player_y, PLAYER_SIZE[0], PLAYER_SIZE[1])
    pygame.draw.rect(screen, WHITE, player)

# Fungsi untuk menggambar peluru
def draw_bullets():
    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, bullet)

# Fungsi untuk menggambar musuh
def draw_enemies():
    for enemy in enemies:
        pygame.draw.rect(screen, WHITE, enemy)

# Loop utama
running = True
while running:
    # Tangani event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Tambahkan peluru
                bullet_x = player_x + PLAYER_SIZE[0] // 2 - BULLET_SIZE[0] // 2
                bullet_y = player_y - BULLET_SIZE[1]
                bullet = pygame.Rect(bullet_x, bullet_y, BULLET_SIZE[0], BULLET_SIZE[1])
                bullets.append(bullet)

    # Pergerakan pesawat
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - PLAYER_SIZE[0]:
        player_x += PLAYER_SPEED

    # Pergerakan peluru
    for bullet in bullets[:]:
        bullet.move_ip(0, -BULLET_SPEED)
        if bullet.top < 0:
            bullets.remove(bullet)

    # Pergerakan musuh
    for enemy in enemies[:]:
        enemy.move_ip(0, ENEMY_SPEED)
        if enemy.top > SCREEN_HEIGHT:
            enemies.remove(enemy)
            add_enemy()

    # Bersihkan layar
    screen.fill(BLACK)

    # Gambar pesawat, peluru, dan musuh
    draw_player()
    draw_bullets()
    draw_enemies()

    # Perbarui layar
    pygame.display.flip()

# Keluar dari Pygame
pygame.quit()

