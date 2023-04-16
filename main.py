import pygame
import tkinter as tk
from tkinter import messagebox
import sys
from player import Player
import locale

pygame.init()

# Detect keyboard language
lang, _ = locale.getdefaultlocale()
if lang.startswith("fr"):
    KEY_UP = pygame.K_z
    KEY_DOWN = pygame.K_s
    KEY_LEFT = pygame.K_q
    KEY_RIGHT = pygame.K_d
else:
    KEY_UP = pygame.K_w
    KEY_DOWN = pygame.K_s
    KEY_LEFT = pygame.K_a
    KEY_RIGHT = pygame.K_d

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 780
WINDOW_CAPTION = "The Legend of Zelda: Future"

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(WINDOW_CAPTION)

clock = pygame.time.Clock()

player_group = pygame.sprite.Group()
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, player_group)
player_group.add(player)

def confirm_quit():
    root = tk.Tk()
    root.withdraw()
    result = messagebox.askyesno("Quit Game", "Are you sure you want to leave without saving?")
    if result:
        pygame.quit()
        sys.exit()

while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            confirm_quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                confirm_quit()

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[KEY_UP]:
        player.rect.y -= 5
        if player.rect.bottom < 0:
            player.rect.top = SCREEN_HEIGHT
    if keys[KEY_DOWN]:
        player.rect.y += 5
        if player.rect.top > SCREEN_HEIGHT:
            player.rect.bottom = 0
    if keys[KEY_LEFT]:
        player.rect.x -= 5
        if player.rect.right < 0:
            player.rect.left = SCREEN_WIDTH
    if keys[KEY_RIGHT]:
        player.rect.x += 5
        if player.rect.left > SCREEN_WIDTH:
            player.rect.right = 0

    # Draw the screen
    screen.fill((255, 255, 255))
    player_group.draw(screen)
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

pygame.quit()
sys.exit()
